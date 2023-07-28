#-*- coding:utf-8 -*

import addonHandler
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
import api
import ui
import scriptHandler
import winUser
import speech
import gui
import wx
import globalCommands
from time import sleep
from tones import beep
from NVDAObjects.IAccessible import IAccessible
from keyboardHandler import KeyboardInputGesture
import os, sys
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import translation, utis, sharedVars
del sys.path[-1]
translation.initTranslationWithEnglishFallback()

dlgCols = None

def manageColumns(self):
	global dlgCols
	utis.setSpeech(True)
	columnHeaders = getColumnHeaders()
	if len(columnHeaders) == 0 : return 
	if  len(columnHeaders) == 1:
		#TRANSLATORS: this is a message list without column headers
		ui.message(_("Column headers not found."))
		return
	if not dlgCols:
		dlgCols = manageColumnsDialog(gui.mainFrame)
	dlgCols.update(columnHeaders[:-1], columnHeaders[-1]) # column list, choose columns button on top the threadTree
	if not dlgCols.IsShown():
		gui.mainFrame.prePopup()
		dlgCols.Show()
		dlgCols.CenterOnScreen()  #<< Centre()
		gui.mainFrame.postPopup()

def getColumnHeaders():
	fo = api.getFocusObject()
	o = fo
	if o.role not in (controlTypes.Role.TREEVIEWITEM, controlTypes.Role.TABLEROW) : #treeviewItem, tablerow
		ui.message(_("Please select the message list or folder tree first."))
		return []
	#  à faire : vérifier qu'il s'agit bien de threadTree
	o = o.parent # threadTree ou folderTree
	if str(o.IA2Attributes.get("id")) == "folderTree" :
		# search for threadTree which is below folderTree
		while o :
			if str(o.IA2Attributes.get("id")) == "threadTree" :
				break
			o = o.next
		if not o :
			return []
		o.setFocus()

	#o=o.firstChild.lastChild # bouton entête "Choisir les colonnes à afficher"
	o=o.firstChild.firstChild # premier entête
	l = []
	while o :
		l.append(o)
		o = o.next
	return l


class ChooseColumns(IAccessible) :
	def initOverlayClass (self):
		if self.role  ==  controlTypes.Role.CHECKMENUITEM :
			if sharedVars.debug : sharedVars.log(self, " avand biendgest")
			self.bindGesture ("kb:rightarrow", "orderColumns") 
			self.bindGesture ("kb:tab", "tabOrder") 
			self.bindGesture ("kb:enter", "spaceCheck") 
			self.bindGesture ("kb:space", "spaceCheck") 

	def script_orderColumns(self, gesture) :
		utis.setSpeech(False)
		beep(440, 20)
		gesture.send()
		KeyboardInputGesture.fromName ("escape").send()
		wx.CallLater(50, manageColumns, self)
	# TRANSLATORS: message shown in Input gestures dialog for this script
	script_orderColumns.__doc__ = _("Opens a dialog to manage the order of columns")
	script_orderColumns.category = sharedVars.scriptCategory

	def script_tabOrder(self, gesture) :
		utis.setSpeech(False)
		KeyboardInputGesture.fromName ("escape").send()
		wx.CallLater(50, manageColumns, self)

	def script_spaceCheck(self, gesture) :
		KeyboardInputGesture.fromName ("enter").send()
		# trop bavard :speech.speakObject(self)
		if controlTypes.State.CHECKED in self.states :
			st = _("Checked, ")
		else :
			st = ("Non coché, ")
		ui.message(st + self.name)

	# cette fonction  est  appelé par le script_escape dans messageListItem.py
	def exitColumns(self, gesture) :
		global dlgCols
		if dlgCols :
			#beep(150, 30)
			dlgCols.Destroy()
			dlgCols = None
		gesture.send()


class manageColumnsDialog(wx.Dialog):
	clip = -1
	def __init__(self, parent):
		#TRANSLATORS: manage columns dialog title
		super(manageColumnsDialog, self).__init__(parent, title= _("Column layout"))
		# Build interface
		mainSizer = wx.BoxSizer(wx.HORIZONTAL)  #<<  VERTICAL

		#self.CheckListBox = wx.CheckListBox(self, wx.NewId(), style=wx.LB_SINGLE, size=(100, 60))
		self.listBox = wx.ListBox(self, wx.NewId(), style=wx.LB_SINGLE, size=(120, 170))  #<< size=(100, 60))
		mainSizer.Add(self.listBox, proportion=8, flag=wx.LEFT|wx.TOP|wx.BOTTOM, border=10)  #<<
		buttonsSizer = wx.BoxSizer(wx.VERTICAL)  #<< HORIZONTAL

		helpButtonID = wx.NewId()
		self.helpButton = wx.Button(self, helpButtonID, _("&Help"), size=(80,25))  #<<
		buttonsSizer.Add(self.helpButton, flag=wx.BOTTOM, border=10)  #<<

		optionsButtonID = wx.NewId()
		#TRANSLATORS: options button in the columns dialog
		self.optionsButton = wx.Button(self, optionsButtonID, _("&Columns ..."), size=(80,25))  #<< 
		buttonsSizer.Add(self.optionsButton, flag=wx.BOTTOM, border=10)  #<<
		#TRANSLATORS: close button in the columns dialog
		cancelButton = wx.Button(self, wx.ID_CANCEL, _("C&lose"), size=(80,25))  #<<
		buttonsSizer.Add(cancelButton)
		mainSizer.Add(buttonsSizer, flag=wx.ALL, border=10)  #<<
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		wx.CallAfter (self.CenterOnScreen)  #<<

		# events 
		self.listBox.Bind(wx.EVT_KEY_DOWN, self.onListKeyDown)
		self.Bind( wx.EVT_BUTTON, self.onHelpButton, id=helpButtonID)
		#self.Bind( wx.EVT_BUTTON, self.onUpButton, id=upButtonID)
		#self.Bind( wx.EVT_BUTTON, self.onDownButton, id=downButtonID)
		self.Bind( wx.EVT_BUTTON, self.onOptionsButton, id=optionsButtonID)
		self.Bind( wx.EVT_BUTTON, self.onCancelButton, id=wx.ID_CANCEL)

	def update(self, columns=None, chooseColumnsButton=None):
		if columns:
			self.columns = columns
			self.folder = columns[0].windowText # window title, To prevent errors if the user changes the folder while the dialog is open
			# The objects are sorted by their position on the screen, which not always corresponds to its index in children
			self.columns.sort(key=lambda o: o.location[0])
		if chooseColumnsButton:
			self.options = chooseColumnsButton
		self.listBox.SetItems([item.name for item in self.columns])
		self.listBox.SetSelection(0)

	def onListKeyDown(self, event) :
		keyCode = event.KeyCode
		isControl = (True if event.GetModifiers() == wx.MOD_CONTROL else False)
		if keyCode ==wx.WXK_LEFT:   
			wx.CallAfter(self.onOptionsButton, event)
			return
		if keyCode ==wx.WXK_SPACE :   
			wx.CallAfter(self.CitPaste)
			return

		if isControl and keyCode ==wx.WXK_UP:   
			wx.CallAfter(self.onUpButton, event, True)
			return
		if isControl and keyCode ==wx.WXK_DOWN:   
			wx.CallAfter(self.onDownButton, event, True)
			return
		if isControl and keyCode ==wx.WXK_PAGEUP :
			wx.CallAfter(self.onUpButton, event, True, 3)
			return
		if isControl and keyCode ==wx.WXK_PAGEDOWN :
			wx.CallAfter(self.onDownButton, event, True, 3)
			return

		if isControl and keyCode ==wx.WXK_HOME:   
			wx.CallAfter(self.onTopButton, event, True)
			return
		if isControl and keyCode ==wx.WXK_END :   
			wx.CallAfter(self.onBottomButton, event, True)
			return
		event.Skip()


	def CitPaste(self) :
		if self.clip ==  -1 : 
			# cut in clip
			self.clip = self.listBox.GetSelections()[0]
			wx.CallLater(50, ui.message,_("%s Cut") % self.columns[self.clip].name)
			return
		# paste opération
		destC = self.listBox.GetSelections()[0]
		if destC == self.clip :
			wx.CallLater(50, ui.message,_("Column %s cannot be moved on itself.") % self.columns[self.clip].name)
			return
		msg =  self.moveColumn(self.clip, destC)
		if msg :
			self.listBox.SetSelection(destC)
			self.Show()
			wx.CallAfter (self.CenterOnScreen)  #<<
			utis.setSpeech(True)
			wx.CallLater(20, ui.message, msg)
		else :
			beep(150, 100)

	def onUpButton(self, event, fromKey=False, number=1):
		c = self.listBox.GetSelections()[0]
		if number == 0 :
			destC = 0 # put column on top
		else :
			destC = max(0, c - number)
		if c == 0:
			wx.CallLater(50, ui.message,_("%s, is already the first column.") % self.columns[c].name)
			return
		utis.setSpeech(False)
		msg =  self.moveColumn(c, destC)
		if msg :
			self.listBox.SetSelection(destC)
			if not fromKey :
				self.upButton.SetFocus()
			self.Show()
			wx.CallAfter (self.CenterOnScreen)  #<<
			utis.setSpeech(True)
			wx.CallLater(20, ui.message, msg)
		else :
			beep(150, 100)

	def onDownButton(self, event, fromKey=False, number=1):
		c = self.listBox.GetSelections()[0]
		destC = min(c+number, len(self.columns) - 1)
		if c == len(self.columns)- 1 :
			#TRANSLATOR: this is the last column and can't be moved
			wx.CallLater(50, ui.message,_("%s, is already the last column.") % self.columns[c].name)
			return
		msg =  self.moveColumn(c, destC)
		if msg :
			self.listBox.SetSelection(destC)
			if not fromKey :
				self.downButton.SetFocus()
			self.Show()
			self.CenterOnScreen()  #<< Centre()
			#TRANSLATORS: a column goes after another column
			#beep(500, 5)
			wx.CallLater(20, ui.message, msg)
		else:
			beep(150, 100)


	def onTopButton(self, event, fromKey=False):
		return self.onUpButton(event, fromKey, number=0)

	def onBottomButton(self, event, fromKey=False):
		return self.onDownButton(event, fromKey, number=99)

	def onPageUppButton(self, event, fromKey=False):
		return self.onUpButton(event, fromKey, number=3)

	def onPageDownButton(self, event, fromKey=False):
		return self.onDownButton(event, fromKey, number=3)

	def onHelpButton(self, event):
		import os
		curAddon=addonHandler.getCodeAddon()
		lang = utis.getLang()
		helpPath=os.path.join(curAddon.path,"doc", lang, "Column layout.txt")
		# ui.message(helpPath)
		# os.startfile (helpPath)
		utis.showTextFile(helpPath, _("Help on Column layout"))
		return	

	def onOptionsButton(self, event):
		utis.setSpeech(False)
		self.Hide()
		# utis.setSpeech(True)
		wx.CallLater(10, self.showColumnPicker) 
	def showColumnPicker(self) :
		utis.setSpeech(True)
		self.options.doAction()

	def onCancelButton(self, event):
		global dlgCols
		self.Destroy()
		dlgCols = None

	def moveColumn(self, srcIndex, targIndex) :
		if self.columns[0].windowText != self.folder:
			#TRANSLATORS: the folder content has changed while this dialog was opened
			ui.message(_("Folder has changed, return to %s to manage columns or restart this dialog") % self.folder[:-22])
			return False
		self.Hide()
		try:
			# Location : RectLTWH(left=434, top=149, width=37, height=24)

			xSource = int(self.columns[srcIndex].location.left + self.columns[srcIndex].location.width / 2)
			ySource = int(self.columns[srcIndex].location[1]+self.columns[srcIndex].location[3]/2)
			srcName = self.columns[srcIndex].name
			# original : xTarget = self.columns[targIndex].location.left+self.columns[targIndex].locationwidth
			xTarget = int(self.columns[targIndex].location.left)
			targName = self.columns[targIndex].name
			if xSource < xTarget :
				xTarget +=  int(self.columns[targIndex].location.width)
				toRight = True # vers la droite
			else :
				xTarget +=7 
				toRight = False
			#print("Location : " + str(self.columns[targIndex].location))
		except TypeError:
			returnNone
		# begin drag
		i = 0 # setCursorPos counter
		wait = 0.0002  # interval between 2 setCurPos
		mod = 10 # modulo factor
		winUser.setCursorPos (xSource, ySource)
		if winUser.getKeyState(winUser.VK_LBUTTON)&32768:
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,1,None,None)
		sleep(0.001) 
		if toRight :
			while xSource<xTarget :
				xSource=(xTarget if xSource>xTarget or (xTarget- xSource)<20 else xSource+20)
				winUser.setCursorPos (xSource, ySource)
				i += 1
				if i % mod == 0 :
					beep(250, 1)
				sleep(wait)
				#old version sleep(0.001) 
		else : # toRight = False
			while xSource>xTarget :
				xSource=(xTarget if xSource<xTarget or (xSource- xTarget)<20  else xSource-20)
				winUser.setCursorPos (xSource, ySource)
				i += 1
				if i % mod == 0 :
					beep(440, 1)
				sleep(wait)  

		winUser.setCursorPos (xTarget,ySource)
		winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)
		# reload  the headers from threadTree
		headers =  []
		o=self.columns[srcIndex].parent.firstChild
		headers = []
		while o :
			headers.append(o)
			#ui.message("colonne  : " + o.name)
			o = 	o.next

		self.update(headers[:-1], headers[-1])
		self.clip = -1
		if toRight :
			mess =  u"{0} après {1}".format(srcName,targName)
		else :
			mess =  u"{0} avant {1}".format(srcName,targName)
		return mess

def file_path_to_url(path):
	"""
	converts an absolute native path to a FILE URL.

    Parameters
    ----------
    path : a path in native format

    Returns
    -------
    a valid FILE URL
    """
	try: from urllib import parse
	except Exception: from urllib.request import parse
	try : from urllib import pathname2url
	except : from urllib.request import pathname2url
#urllib.request.pathname2url.
	return parse.urljoin('file:', pathname2url(path))

