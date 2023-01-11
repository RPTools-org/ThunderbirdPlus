#-*- coding:utf-8 -*
# Thunderbird+ 4.0  for Thunderbird 102

from .py3compatibility import *
from nvdaBuiltin.appModules import thunderbird
from time import time, sleep
from datetime import datetime
try:
	from NVDAObjects.IAccessible.mozilla import BrokenFocusedState as IAccessible
except ImportError:
	from NVDAObjects.IAccessible import IAccessible
from tones import beep
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
import globalCommands, globalVars
from re import compile,IGNORECASE

# shared modules import
import addonHandler,  os, sys
addonHandler.initTranslation()
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import utis, sharedVars # , sendInput
# dbg = sharedVars.log
from  py3compatibility import *
from  py3compatibility import _unicode
del sys.path[-1]
sharedVars.scriptCategory = _curAddon.manifest['summary']

# Extension modules import
from . import messengerWindow, msgComposeWindow # , addressbookWindow

# UIA for Thunderbird+ 4.0
from UIAHandler import handler,UIA_HyperlinkControlTypeId, UIA_ControlTypePropertyId, TreeScope_Descendants, UIA_DocumentControlTypeId, UIA_LegacyIAccessibleKeyboardShortcutPropertyId, UIA_ButtonControlTypeId, IUIAutomationInvokePattern, TreeScope_Children
clientObject = handler.clientObject

from scriptHandler import getLastScriptRepeatCount
_timer = None


class AppModule(thunderbird.AppModule):
	objCompose = None # the unique object of the msgComposeWindow.MsgComposeWindow class 

	def __init__(self, *args, **kwargs):
		super(thunderbird.AppModule, self).__init__(*args, **kwargs)
		#super(AppModule, self).__init__(*args, **kwargs)
		self.lastIndex = 0
		self.Dialog = None
		# Thunderbird+
		self.wndClass = ""
		columnID= []
		lenColID = 0
		self.prevTitle    = "init"
		globalVars.TBStep = 5 # à supprimer
		#ui.message("TBStep : " + str(globalVars.TBStep))
		#self.curFrame = "messengerWindow"
		self.TTActivated = False
		self.needReading = False
		sharedVars.initSettingsMenu(self) # utiliser ensuite sharedVars.oSettings.*
		self.regExp_date =compile ("^(\d\d/\d\d/\d{4} \d\d:\d\d|\d\d:\d\d)$")
		self.regExp_nameListGroup, self.regExp_AnnotationResponse, self.regExp_mailAddress  =compile ("\[.*\]|\{.*\}"), compile ("re[ ]*:[ ]", IGNORECASE), compile ("\S+?@\S+?\.\S+")
		# self.regExp_listGroupName = compile ("\[(.*)\]") # |\{?*\}") # first occurrence of the list group name
		self.regExp_removeMultiBlank =compile (" {2,}")
		self.regExp_removeSymbols =compile ("\d+|&|_|@.+|=|\.| via .*")
		wx.CallLater(50, utis.getGroupingIndex)
		#wx.CallLater(25000, debugShow, self, True)

	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if sharedVars.objLooping : return
		role = obj.role
		# le bloc  ci-dessous empêche le ralentissement du mode rédaction
		# Niveau 1,  23 sur 24, name : Corps du message, role.INTERNALFRAME=115, IA2ID : content-frame Tag: editor, états : , FOCUSABLE, childCount  : 1 Chemin : role FRAME=34| i23, role-INTERNALFRAME=115, , IA2ID : content-frame , IA2Attr : id : content-frame, explicit-name : true, display : inline, tag : editor,  ;
		# Niveau 2,   0 sur 0, name : Corps du message, role.DOCUMENT=controlTypes.Role.DOCUMENT Tag: body, états : , FOCUSED, MULTILINE, FOCUSABLE, EDITABLE, childCount  : 6 Chemin : role FRAME=34| i23, role-INTERNALFRAME=115, , IA2ID : content-frame | i0, role-DOCUMENT=52,  , IA2Attr : explicit-name : true, display : block, tag : body, line-number: 2,;
		if  role == controlTypes.Role.DOCUMENT  and  controlTypes.State.EDITABLE in obj.states :
			sharedVars.curFrame = "msgcomposeWindow"
			# beep(300, 3)
			sharedVars.curTab = "comp"
			if sharedVars.virtualSpellChk :
				clsList.insert(0, msgComposeWindow.virtualSpellCheck.ThunderbirdEditDocument)
				#copyClsList(clsList) # copy to clip for testing
			return
		if role == controlTypes.Role.FRAME  : # and "Thunderb" in str(obj.name) : #obj.windowClassName: # or (self.curFrame == "messengerWindow" and self.curTab == "init") : # or not self.curFrame  :
			sharedVars.oCurFrame = obj
			# if sharedVars.debug : sharedVars.log(obj)
			sharedVars.curFrame = getFrameID(obj)
			# sharedVars.log(None, "frame courant : " + sharedVars.curFrame)
			if sharedVars.curFrame == "1messageWindow" :
				if role == controlTypes.Role.FRAME  : obj.name = "" 
			elif sharedVars.curFrame == "messengerWindow" :
				ct, n = messengerWindow.tabs.findCurTab(obj)
				if n > -1 : 
					sharedVars.curTab = messengerWindow.tabs.getTabType(ct.name, n, obj)

			if sharedVars.debug : sharedVars.log(obj, "Overlay normal section, obhjet {0}".format(sharedVars.curFrame))
		if role == controlTypes.Role.DIALOG :
			self.wndClass = obj.windowClassName
			if sharedVars.debug : sharedVars.log(obj, " Test Role Dialog : ")
			setDialogID(obj, self.wndClass)
			#return
		if role in (controlTypes.Role.WINDOW, controlTypes.Role.DIALOG, controlTypes.Role.FRAME) :
			if sharedVars.debug : sharedVars.log(obj, "frame courant : " + sharedVars.curFrame)

		# traitement des des frames
		#objID = utis.getIA2Attribute(obj)
		if sharedVars.curFrame == "messengerWindow" :
			if  role == controlTypes.Role.DOCUMENT and controlTypes.State.READONLY in obj.states  and controlTypes.State.FOCUSED in obj.states: 
				if sharedVars.curTab in ("main", "message") :
					obj.name = ""
					return
			if sharedVars.curTab == "main" :
				# Liste des colonnes à afficher role.CHECKMENUITEM=60, WindowClass : MozillaDropShadowWindowClass 
				# TB 102+ : no more IA2Attrbutes nor window class
				if role == controlTypes.Role.CHECKMENUITEM : # removed for menus optimizations -> in (controlTypes.Role.CHECKMENUITEM, controlTypes.Role.POPUPMENU) : # not useful here controlTypes.Role.MENUITEM, 
					o = obj.parent.parent
					if o and _("Choisir les col")  in str(o.name) :
						# beep(700, 20)
						clsList.insert (0,messengerWindow.columnManager.ChooseColumns)

				objID = ""
				if role == controlTypes.Role.LISTITEM   and utis.getIA2Attribute (obj.parent,"attachmentList"): 
					clsList.insert (0,messengerWindow.attachmentList.AttachmentList)
					return # évite conflit escape, alt+1 et alt+2 de messageListUtem
				# ui.message("avant test tree role " + str(role))
				if  sharedVars.prevObj == "1messageWindow" :
					sharedVars.prevObj = ""
					# beep(600, 30)
					# sleep(0.2)
					# beep(250, 30)
					# objID =  str(utis.getIA2Attribute(obj))
					# if  objID == "threadTree" :
						# api.setFocusObject(obj)
						# obj = api.getFocusObject() # globalVars.focusObject
						# role = controlTypes.Role.TABLEROW
						# ui.message("threadTree, role" + str(role))

				if role in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW) :
					objID = str(utis.getIA2Attribute(obj.parent))
					# ui.message(objID)

				if objID == "threadTree" or obj.role == controlTypes.Role.DOCUMENT  :
					clsList.insert(0, messengerWindow.folderTreeItem.FolderTreeItem)
					clsList.insert(0, messengerWindow.messageListRowCells.MessageListItemFields)
					#if sharedVars.debug : sharedVars.log(obj, "Insertion messageListITEm")
					#if messengerWindow.messageListItem.MessageListItem not in clsList :
					try : 
						clsList.insert(0, messengerWindow.messageListItem.MessageListItem)
						clsList.insert(0, messengerWindow.foldersList.FoldersListItem)
						#if sharedVars.debug : sharedVars.log(None, "Insertion messageListITEm depuis try")
						#beep(80, 20)
					except : pass  # if sharedVars.debug : sharedVars.log(obj, "Echec Insertion messageListITEm")
				elif objID == "folderTree" :
					clsList.insert(0, messengerWindow.folderTreeItem.FolderTreeItem)
					#if sharedVars.debug : sharedVars.log(obj, "Insertion folderListItem")
					clsList.insert(0, messengerWindow.foldersList.FoldersListItem)
			elif sharedVars.curTab == "sp:addons" :
				clsList.insert(0, messengerWindow.pageAddons.AddonsPage)
			# elif sharedVars.curTab == "sp:addressbook" :
				# à faire : assigner raccourcis aux boutons de création  de contact et de liste de diffusion
				# if role == controlTypes.Role.BUTTON :
					# ID = str(utis.getIA2Attribute(obj))
					# # level 6,       1 of 3, name : Nouveau contact, Role.BUTTON, IA2ID : toolbarCreateContact Tag: toolbarbutton, States :  Path : Role-FRAME| i46, Role-GROUPING, , IA2ID : tabpanelcontainer | i2, Role-PROPERTYPAGE, , IA2ID : addressBookTabWrapper0 | i0, Role-INTERNALFRAME, , IA2ID : addressBookTabBrowser0 | i0, Role-DOCUMENT,  | i0, Role-TOOLBAR,  | i1, Role-BUTTON, , IA2ID : toolbarCreateContact , IA2Attr : explicit-name : true, setsize : 4, display : -moz-box, id : toolbarCreateContact, posinset : 2, tag : toolbarbutton, class : toolbarbutton-1, , Actions : press,  ;
					# if ID == "toolbarCreateContact" :
						# #obj.keyboardShortcut = "alt+shift+c"
						# beep(800, 50)
		# elif sharedVars.curFrame == "msgcomposeWindow" :
		elif sharedVars.curFrame == "spellCheckDlg" :  # dialogue vérif orthographique
			if role == controlTypes.Role.EDITABLETEXT :
				#beep(440, 20)
				clsList.insert (0,msgComposeWindow.spellCheckDlg.SpellCheckDlg)
		#elif sharedVars.curFrame == "searchMailWindow" # rech avancée dans messages avec control-+shift+s
		# Overlay search box in quick filtering bar
			# path  : role GROUPING=56| i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i11, role-EDITABLETEXT=8,  
		if sharedVars.curTab == "main" and not sharedVars.TTnoFilterBar and obj.role == controlTypes.Role.EDITABLETEXT:
			qfb = (True if str(utis.getIA2Attribute(obj.parent)) == "mailContent"   else False)
			if qfb:
				setattr(obj, "pointedObj", None)
				#TRANSLATORS: additional description for the search field
				obj.description = _("(Appuyez sur flèche bas pour afficher plus d'options)")
				clsList.insert(0, SearchBox)
		# end of choose overlay

	# def event_NVDAObject_init(self, obj):
		# if sharedVars.curFrame != "1messageWindow" : return
		# if hasattr(obj, "value") :
			# obj.value = "object_init : role {0}, name {1}".format(str(obj.role), obj.value)
		# return
		# # if obj.role in (controlTypes.Role.WINDOW, controlTypes.Role.APPLICATION, controlTypes.Role.FRAME) :  # , controlTypes.Role.DOCUMENT) : 
		# sharedVars.log(obj, "object init  , " + sharedVars.curFrame)
		# if  sharedVars.curFrame == "1messageWindow" :
			# if  obj.role ==  controlTypes.Role.DOCUMENT : obj.name = "message " + obj.name
			# if  obj.role in (controlTypes.Role.WINDOW, controlTypes.Role.APPLICATION) : 			obj.name = ""
			# return
		# if obj.role == controlTypes.Role.FRAME : 
			# o = utis.findChildByIDRev(obj, "messagepane")
			# sharedVars.log(o,"recherche message pane")
			# if o : 
				# beep(500, 30)
				# obj.name = ""
		# return
		# if obj.role ==  controlTypes.Role.FRAME :
			# nm = str(obj.name)
			# if nm.startswith(_(u"Rédaction")) : return
			# if nm  == self.prevTitle : obj.name = self.prevTitle =""
			# else : self.prevTitle = nm
		# return
		# # if sharedVars.curFrame == "1messageWindow" and  obj.role in (controlTypes.Role.WINDOW, controlTypes.Role.APPLICATION, controlTypes.Role.FRAME) :  # , controlTypes.Role.DOCUMENT) : 
			# # if 		hasattr(obj, "name") : 
				# # if  _(u"Rédaction")  in obj.name : return # self.prevTitle = "in"
				# # if obj.name == self.prevTitle : obj.name = ""
				# # else : self.prevTitle = obj.name
				# # # obj.name = str(obj.role)

	# begin Thunderbird+ 
	# events and associated

	def TBExited() : # à supprimer ?
		# globalVars.TBStep = 0
		beep(150, 20)	

	def read1Message(self, obj) :
		speech.cancelSpeech()
		if sharedVars.oSettings.getOption("messengerWindow", "WithoutAutoRead") :
			ui.message(utis.cleanedWinTitle(self)) 
		else :
			messengerWindow.document.readDoc(obj, utis.cleanedWinTitle(self) )

	def focus1message(self, obj) :
		# speech.cancelSpeech()
		o = api.getFocusObject()
		if o.role == controlTypes.Role.DOCUMENT :
			beep(440, 30)
			messengerWindow.document.readDoc(o, _("sujet")) # o.name)
		else :
			ui.message(obj.name + ", " + str(o.name))
		# ui.message(str(o.role))
		# self.needReading = True

	def event_foreground(self, obj,nextHandler):
		# ui.message("foreground, name {0}, role {1}, curFrame {2} ".format(obj.name, str(obj.role), sharedVars.curFrame))
		# sharedVars.log(obj, " event foreground , " + sharedVars.curFrame)
		if obj and obj.role == controlTypes.Role.FRAME  :
			sharedVars.curFrame = getFrameID(obj)
			if sharedVars.curFrame == "messengerWindow" : 
				ct, n = messengerWindow.tabs.findCurTab(obj)
				if n > -1 :
					sharedVars.curTab = messengerWindow.tabs.getTabType(ct.name, n, obj)
			# elif sharedVars.curFrame == "1messageWindow" :
				# speech.cancelSpeech()
				# return # wx.CallAfter(self.focus1message, obj)
		nextHandler()

	def event_gainFocus (self,obj,nextHandler):
		role = obj.role
		# sharedVars.log(obj, " event gainFocus , " + sharedVars.curFrame)
		if sharedVars.curTab == "main"   and sharedVars.curFrame == "messengerWindow" :
			if role in (controlTypes.Role.TABLEROW, controlTypes.Role.TREEVIEWITEM) :   
				ID = str(utis.getIA2Attribute(obj.parent))
				if ID == "threadTree" :
					if sharedVars.lockEditMenu :
						utis.setSpeech(True)
						sharedVars.lockEditMenu = False
					if controlTypes.State.SELECTED not in obj.states : 
						# beep(600, 5)
						obj.doAction() 
						# sleep(0.2)
					# if role == controlTypes.Role.TREEVIEWITEM and  obj.IA2Attributes.get("level") == "1"   and obj.firstChild : # and "Col " in obj.name : # si  ligne de groupage par critère de tri
						# obj.name = buildGroupRowName(self, obj)
					# else :
					if sharedVars.testMode == False :
						obj.name =  buildRowName2(self, obj) # pour annonce filtrée de la ligne

			elif role == controlTypes.Role.MENUITEM and sharedVars.lockEditMenu :
				# beep(500, 30)
				# 2022-08-09désact  utis.setSpeech(False)
				sharedVars.lockEditMenu = False # added 2022-08-09
				KeyboardInputGesture.fromName ("escape").send() 
				wx.CallLater(25, KeyboardInputGesture.fromName ("n").send)
		elif  sharedVars.curFrame == "1messageWindow" :
			if hasattr(obj, "name") :
				if   "illa Thunde" in str(obj.name) :
					obj.name = u"…"
					# # obj.name = "gainFocus : role {0}, name {1}".format(str(obj.role), obj.name)
			if controlTypes.State.BUSY in obj.states :
				# if obj.role == controlTypes.Role.FRAME : obj.name = "m"# obj.role == controlTypes.Role.WINDOW
				return # beep(500, 25)	
			if  obj.role ==  controlTypes.Role.DOCUMENT : 
				obj.name = ""
				wx.CallLater(sharedVars.delayReadWnd, self.read1Message, obj)
			# elif  obj.role in (controlTypes.Role.FRAME, controlTypes.Role.WINDOW, controlTypes.Role.APPLICATION) : 			obj.name = ""
		try : nextHandler()
		except : return

	def event_focusEntered (self,obj,nextHandler):
		role, objID  = obj.role, utis.getIA2Attribute (obj)  
		# sharedVars.log(obj, " event focusEntered , " + sharedVars.curFrame)
		if sharedVars.curTab == "main" : # sharedVars.curFrame == "messengerWindow" : 
			# empêche annonce de "page de propriétés" etc
			if role == controlTypes.Role.PROPERTYPAGE :
				#if sharedVars.debug : sharedVars.log(obj, "Avant return")
				return # pas de nextHandler   pour ne pas entendre page de propriétés etc
			if objID == "threadTree" :
				self.ttActivated = True
				#if sharedVars.debug : sharedVars.log(obj, "Avant buildColumnID")
				self.buildColumnID (obj) 
				# Are  quick filter bar results displayed ?
				# threadTree path : i0, Role-PROPERTYPAGE, , IA2ID : mailContent | i2, Role-TREEVIEW, 
				# qfb path : i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i11, role-EDITABLETEXT=8
				o = utis.findChildByID(obj.parent,"qfb-results-label")
				if o and o.name :  utis.playSound("filter")
				return
		return nextHandler()

	def _get_statusBar(self):
		if sharedVars.curTab != "main" : 
			return  globalVars.foregroundObject.lastChild.previous
		o = globalVars.foregroundObject.lastChild.previous
		# 0 : en ligne, 1 : None, 2 :   non lus, 3 : total, 4 : 
		o.children[0].name = " " # supprime "actuellement en ligne
		n3 = str(o.children[3].name)
		if "filt" not in  n3 : # NVDA appelle 2 fois cette méthode
			o.children[3].name = n3  + ", " + getFilterInfos(self)
		return   o

	def buildColumnIDOld (self, obj):
		#beep(700, 30)
		sharedVars.objLooping = True
		o =( e for e in range (obj.firstChild.childCount-1))
		p =obj.firstChild.getChild
		self.columnID =[]
		for e in o :
			#if p(e) : self.columnID.append ((p(e).location[0],utis.getIA2Attribute (p(e))))  
			try : # try ajouté version 3.2
				if p(e) and int(p(e).location[2])>0: self.columnID.append ((p(e).location[0],utis.getIA2Attribute (p(e)))) 
				else : continue
			except :
				continue

		# sharedVars.log(None, "Avant tri : " + str(self.columnID))
		self.columnID.sort()
		self.columnID =[e[1] for e in self.columnID]
		# if sharedVars.debug : 
		# beep(100, 30)
		# sharedVars.log(None, str(self.columnID))
		sharedVars.objLooping = False

	def buildColumnID(self, oTT):
		try :
			# oTT must be the threadTree
			sharedVars.objLooping = True
			o =  oTT.firstChild.firstChild # first headers of threadTree
			# sharedVars.log(o, "Premier entete : ")
			self.columnID =[]
			while o and o.role == controlTypes.Role.TABLECOLUMNHEADER :
				if int(o.location[2]) > 0 :
					# append couple (location, IA2ID)
					self.columnID.append((o.location[0],utis.getIA2Attribute(o)))
				o = o.next
			# beep(100, 30)
			# sharedVars.log(None, "Avant tri : " + str(self.columnID))
			self.columnID.sort()
			self.columnID =[e[1] for e in self.columnID]
			# if sharedVars.debug : 
			# sharedVars.log(None, str(self.columnID))
		finally :
			self.lenColID = len(self.columnID) # for speed in buildRowName
			sharedVars.objLooping = False

	def event_alert (self,obj,nextHandler):
		fo = api.getFocusObject()
		if obj.childCount > 1 :
			# to cancel an alert, we do not call nextHandler() and we return directly
			msg = ""
			role = 0			
			o = obj.firstChild
			while o : 
				if hasattr(o, "name") : nm = str(o.name)
				else  : nm = "sans nom"
				#ui.message("ui.message :" + nm)
				if hasattr(o, "role") : role = o.role 
				else : role = -1
				if role == controlTypes.Role.LABEL : 
					if hasattr(o, "name") :
						msg = msg + str(o.name)
				o = o.next
			#print("ui.message alerte : " + msg)
			#print (u"évén alerte : " + msg)
			#Translators: alert : this is a draft
			if _("brouillon") in msg :
				return
				#Translator:  alert : Reply to sub thread. Occurs after   pressed control+r on collapsed thread with severa messages.
			elif _("réponses au sous-fil de di, ") in msg :  
				#Translators: Close button of the alert in TB
				oBtn = findButtonByName(obj, _("Fermer"))
				if oBtn :
					close = True
					#if sharedVars.oSettings.getOption("messengerWindow", "withoutReceipt") :
					if close :
						oBtn.doAction()
						if fo.role in (controlTypes.Role.TREEVIEWItem , controlTypes.Role.TABLEROW) : KeyboardInputGesture.fromName ("shift+f6").send() 
						return 
					else :
						wx.CallLater (30, focusAlert, msg, oBtn)
			#Translators: 2022-12-12 alert X @gmail.com has asked to be notified when you read this message.
			elif _("notification quand") in msg :  # demande accusé réception
				if sharedVars.oSettings.getOption("messengerWindow", "withoutReceipt") :
					return
					#Translators:  Ignore button in alert in TB
				oBtn = findButtonByName(obj, _("Ignorer"))
				if oBtn :
					wx.CallLater (30, focusAlert, msg, oBtn)
				nextHandler()
				return
				#Translators: alert : Thunderbird thinks this message is fraudulent
			elif _("ird pense que") in msg : # indésirable
				beep (200, 2)
				return
				#Translators: alert : remote content 
			elif _("contenu distant") in msg :
				# beep(120, 70)
				return
				# désact 2022-09-02 cette alerte s'affiche parfois quand html simple activé et contenu distant désactivé dans paramètres de TB
				# msg = u"%s Conseil : Ouvrez le menu Affichage, descendez sur Corps du ui.message et validez HTML simple dans le sous-menu " % msg 
				# oBtn = findButtonByName(obj, "Option")
				# wx.CallLater (30, focusAlert, msg, oBtn)
				# nextHandler()
				return
		# for addons install
		try:
			if api.getForegroundObject().simpleFirstChild.IA2Attributes["id"] == "notification-popup":
				#speech.cancelSpeech()
				o=api.getForegroundObject().simpleFirstChild.lastChild
				#ne fonctionne pas : api.setFocusObject(o)
				#o.setFocus ()
				wx.CallLater (30, focusAlert, msg, o)
				# unwanted here : o.doAction()
				nextHandler()
				return
		except (KeyError, AttributeError):
			pass	
		nextHandler()

	# gesture scripts

	def initObjCompose(self) :
		if self.objCompose is None :
			self.objCompose = msgComposeWindow.msgComposeWindow.MsgComposeWindow()
		self.objCompose.update()
		return

	def script_sharedEscape(self, gesture) :
		o=globalVars.focusObject 
		role = o.role
		# ui.message(str(role) + ", " + sharedVars.curFrame)
		if sharedVars.curFrame == "messengerWindow" :
			if sharedVars.oSettings.getOption("chichi", "mainNoEscape") : return gesture.send()
			if role == controlTypes.Role.LISTITEM  and hasattr(o, "script_escape") :  return o.script_escape(gesture) 
			if role == controlTypes.Role.TEXTFRAME :
				# return beep(200, 30)
				o = o.parent
				if "chrome://" in str(o.name) : 
					o, i =findTree(None, "folderTree")
					if o : return o.setFocus()
			if role in (controlTypes.Role.BUTTON, controlTypes.Role.LINK, controlTypes.Role.LANDMARK) : 
				if utis.findParentByID(o, controlTypes.Role.LANDMARK, "accountCentral") : 
					o, i =findTree(None, "folderTree")
					if o : return o.setFocus()
			if role in (controlTypes.Role.TREEVIEWITEM,  controlTypes.Role.TABLEROW) and not  hasattr (o, "script_escape") :
				# beep(250, 30)
				if str(utis.getIA2Attribute(o.parent)) == "threadTree" :  
					return utis.sendKey("shift+f6") # beep(600, 30)
		elif sharedVars.curFrame == "1messageWindow" :
			gesture.send()
			sharedVars.prevObj = "1messageWindow"
			sharedVars.curFrame = "messengerWindow"
			sharedVars.curTab = "main"
			# api.processPendingEvents()

			# sleep(0.1)
			# fo = api.getFocusObject() 
			# wx.CallLater(1000, ttResetFocus, api.getFocusObject())
			# if fo.role in (controlTypes.Role.TREEVIEWITEM, controlTypes.Role.TABLEROW)  and controlTypes.State.SELECTED not in  fo.states : 
				# # fo.doAction() # select
				# beep(440, 30)
			return
		elif sharedVars.curFrame == "msgcomposeWindow" :
			if role == controlTypes.Role.LISTITEM : #  of controlTypes.Role.COMBOBOX :
				# role : 35, ID : FormatToolbar, 
				o = o.parent.parent.parent
				if not o : return
				if utis.getIA2Attribute(o) == "FormatToolbar" :
					# role COMBOBOX=13 , IA2ID=ParagraphSelect , 
					wx.CallLater(100, msgComposeWindow.msgComposeWindow.focusDoc)

		# compose window close with escape
		close = sharedVars.oSettings.getOption("compose", "closeMessageWithEscape")
		if sharedVars.curFrame == "msgcomposeWindow" and close :
			#  cas particulier : pas de classe overlay et donc pas de script_ pour la fenêtre de rédaction 
			#if role in (controlTypes.Role.EDITABLETEXT, controlTypes.Role.DOCUMENT) : return KeyboardInputGesture.fromName ("control+w").send () #modifié pour fenêtre de lecture
			if role in (controlTypes.Role.EDITABLETEXT , controlTypes.Role.DOCUMENT) : return KeyboardInputGesture.fromName ("control+w").send () #modifié pour fenêtre de lecture
			else : return gesture.send()
		# message  headers controls
		if role in (controlTypes.Role.LISTITEM, controlTypes.Role.SECTION) : 
			if utis.findParentByID(o, controlTypes.Role.LANDMARK, "messageHeader") :
				return KeyboardInputGesture.fromName ("shift+f6").send () 
		# quick filter bar edit
		if role==controlTypes.Role.EDITABLETEXT and o.parent.role == controlTypes.Role.PROPERTYPAGE :
			if o.value is not None : ui.message(_(u"Mot-clé supprimé."))
			gesture.send()
			return 
			# quick filter bar edit
		if role==controlTypes.Role.EDITABLETEXT and o.parent.role in (controlTypes.Role.COMBOBOX,controlTypes.Role.INTERNALFRAME) and close :
			return KeyboardInputGesture.fromName ("control+w").send () 
		# doc in preview pane, propertypage or in separate window
		if role in (controlTypes.Role.LINK, controlTypes.Role.DOCUMENT) : 
			#sharedVars.debugLog = ""
			o2 = o
			while o2:
				#if sharedVars.debug : sharedVars.log(o2, " o2 : ", False)
				ID = str(utis.getIA2Attribute (o2))
				if ID == "mailContent" and o2.role == controlTypes.Role.PROPERTYPAGE : return KeyboardInputGesture.fromName ("shift+f6").send ()  # preview pane in main window 
				if  ID == "messagepane" and o2.parent.role == controlTypes.Role.FRAME : return KeyboardInputGesture.fromName ("control+w").send() # separate message window
				o2 = o2.parent
			if not o2 :  return
		if hasattr (o, "script_escape"): return o.script_escape(gesture)
		gesture.send ()	

	def script_sharedAltEnd(self, gesture) :
		msg = utis.getStatusBarText()
		if not msg : msg = _("Ligne d'état sans données")
		if sharedVars.curTab != "main" : 
			return ui.message(msg)

		fo = globalVars.focusObject
			# if focus in quick filter bar edit
		if fo.role==controlTypes.Role.EDITABLETEXT and fo.parent.role == controlTypes.Role.PROPERTYPAGE :
			msg = ""
		sayFilterInfos(self, sbar=msg)
	script_sharedAltEnd.__doc__ = _("Annonce la ligne d'état abrégée et les informations de filtrage de messages s'il y a lieu")
	script_sharedAltEnd.category = sharedVars.scriptCategory

	def script_sharedCtrlTab(self, gesture) :
		fo = globalVars.focusObject # api.getFocusObject()
		speech.cancelSpeech()
		#beep(440, 5)
		direct = (-1 if "shift" in gesture.modifierNames else 1)
		#self.curFrame = 
		sharedVars.curFrame = getFrameID(fo)
		#if sharedVars.curFrame == "msgcomposeWindow" : return 
		# if sharedVars.curFrame == "contactDialog" :
			# return addressbookWindow.contactDialog.changeContactTab(gesture)
		if sharedVars.curFrame !=  "messengerWindow" :  return gesture.send()
		messengerWindow.tabs.changeTab(self, fo, direct)
		wx.CallLater(100, focusPage, self, None, False)

	def script_sharedCtrlN(self, gesture) :
		speech.cancelSpeech()
		fo = globalVars.focusObject # api.getFocusObject()
		sharedVars.curFrame = getFrameID(fo)
		#if sharedVars.curFrame == "msgcomposeWindow" : return 
		# if sharedVars.curFrame == "contactDialog" :
			# return addressbookWindow.contactDialog.activateContactTab(gesture)
		if sharedVars.curFrame !=  "messengerWindow" :  return # gesture.send()
		mainKey = gesture.mainKeyName
		# 2022-12-09 localized replacement of if mainKey == "=" : mainKey = "0" # for control+=
		if mainKey == utis.gestureFromScanCode(13,"") : mainKey = "0" # for they at the left of backspace

		newTabIdx = int(mainKey) - 1
		if newTabIdx == -1 :  # control+0 - 1
			messengerWindow.tabs.showTabMenu(self, fo)
			wx.CallLater(100, focusPage, self, sharedVars.oCurFrame, False)			
			return
		# control+1 to control+9
		# beep(100, 30)
		messengerWindow.tabs.activateTab(self, fo, newTabIdx)
		wx.CallLater(100, focusPage, self, None, False)

	def script_sharedCtrlR(self, gesture) :
		global _timer
		# speed optimization for edit message window
		if sharedVars.curTab == "comp" :
			# beep(250, 5)
			return gesture.send()
		elif sharedVars.oSettings.getOption("chichi", "TTnoSmartReply") :
			return gesture.send()
		repeats = getLastScriptRepeatCount ()
		if _timer is not None:
			_timer.Stop()
			_timer = None
		# ui.message(u"répétitions " + str(repeats))
		# return
		if  sharedVars.curTab not in  ("main", "message") :
			return gesture.send()
		# beep(440, 20)
		fo = messengerWindow.messageListItem.checkFocus(globalVars.focusObject, gesture)
		if not fo:
			#beep(80, 60)
			return gesture.send() # necessary to return the gesture
		msgHeader = utis.getMessageHeadersFromFG(False)
		# OK sharedVars.debugMess(msgHeader, "premier entête")
		# return
		# if not msgHeader :
			# beep(100, 30)
			# return KeyboardInputGesture.fromName ("control+r").send()
		# beep(440, 20)
		_timer =  wx.CallLater(300, messengerWindow.messageListItem.smartReply, msgHeader, repeats)
	script_sharedCtrlR.__doc__ = _("Smart reply pour répondre à un destinataire ou à une liste de diffusion")
	script_sharedCtrlR.category = sharedVars.scriptCategory

	def  script_sharedAltEqual(self, gesture) : # native context menu of active tab
		if sharedVars.curFrame != "messengerWindow" : return
		messengerWindow.tabs.tabContextMenu(self, sharedVars.oCurFrame)

	def script_sendCtrlF4(self, gesture) :
		if sharedVars.curFrame == "msgcomposeWindow" :
			if gesture.mainKeyName == "backspace" and globalVars.focusObject.role == controlTypes.Role.DOCUMENT :
				import os
				curAddon=addonHandler.getCodeAddon()
				lang = utis.getLang()
				helpPath=os.path.join(curAddon.path, "doc", lang, "Control Backspace conflict.txt")
				os.startfile (helpPath)
				return	
			if gesture.mainKeyName == "w" : return gesture.send()
		elif sharedVars.curFrame == "messengerWindow" :
			if sharedVars.curTab == "main"  and not  sharedVars.oSettings.getOption("chichi",   "closeTBWithCtrlF4") : 
				n = messengerWindow.tabs.getTabCount()
				if n < 2 :
					beep(350, 10)
					return
			KeyboardInputGesture.fromName("control+f4").send()
			wx.CallLater(150, setCurTab, self)
		else :
			KeyboardInputGesture.fromName("control+w").send()
	script_sendCtrlF4.__doc__ = _("Envoie Control+F4 à la fenêtre courante.")
	script_sendCtrlF4.category=sharedVars.scriptCategory

	def script_sharedAltN(self, gesture) :
		# centralise  gestion des alt+chiffre  pour éviter conflits
		global _timer
		fo = globalVars.focusObject # api.getFocusObject()
		if hasattr(fo, "script_readAttachField") : return fo.script_readAttachField(gesture) # attachment list

		if fo.role not in (controlTypes.Role.UNKNOWN, controlTypes.Role.EDITABLETEXT, controlTypes.Role.BUTTON, controlTypes.Role.LISTITEM, controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW, controlTypes.Role.DOCUMENT) : 
			return gesture.send()
		#ui.message("curTab = " + sharedVars.curFrame)
		#beep(440, 20)
		repeats = getLastScriptRepeatCount ()
		#ui.message("repeat : " + str(repeats))
		if _timer is not None:
			_timer.Stop()
			_timer = None
		if sharedVars.curTab in ("main", "message") :
			#beep(440, 20)
			fo = messengerWindow.messageListItem.checkFocus(fo)
			if not fo:
				beep(337, 2)
				return
			msgHeader = utis.getMessageHeadersFromFG(False)
			#if sharedVars.debug : sharedVars.log(msgHeader, " messsageHeader ")
			if not msgHeader :
				if messengerWindow.messageListItem.getTreeID(globalVars.focusObject) == "threadTree" : return ui.message(_("Le volet des entêtes n'est pas affiché. Veuillez presser F8 puis réessayer"))
				else : return ui.message(_("Le volet des entêtes ne contient pas d'informations ou est absent"))
			if repeats == 1 : 
				#beep(440, 20)
				delay = 300 # affichage dialogue Copier dans le presse-papiers
			else : delay = 5 # elif repeats in (0, 2) : delay = 5 # annonce entête ou ouverture menu contextuel de la zone des entêtes
			_timer = wx.CallLater(delay, messengerWindow.messageListItem.readHeaders, fo, msgHeader, int(gesture.mainKeyName), repeats, delay) # key, repeatCount, delay
		elif sharedVars.curFrame == "msgcomposeWindow" :
			self.initObjCompose()
			self.objCompose.readField(gesture.mainKeyName, repeats)
		else : #autres frames
			beep(440, 20)
	script_sharedAltN.__doc__ = _("Dans la fenêtre principale,  1 appui : Alt+1  à 8: lit l'entête  du message, Alt+9 annonce le nombre de pièces jointes, 2 appuis : affiche l'entête dans une boîte d'édition ou pour Alt+9, atteint la liste des pièces jointes, 3 appuis : atteint l'entête dans la zone des entêtes. Dans la fenêtre de rédaction, Alt1 à 4, lit les entêtes,  2 appuis atteint l'entête.")
	script_sharedAltN.category=sharedVars.scriptCategory

	def script_sharedAltArrow(self, gesture) :
		# centralise  gestion des alt+flèches  pour éviter conflits
		#beep(440, 5)
		mainKey = gesture.mainKeyName
		o = api.getFocusObject() # globalVars.focusObject api.getFocusObject()
		role = o.role
		# la ligne ci-dessous est une optimisation pour la fenêtre de rédaction
		if role == controlTypes.Role.DOCUMENT and mainKey in ("leftArrow", "rightArrow") : return gesture.send() 

		if sharedVars.curTab == "main" :
			if role not in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW, controlTypes.Role.DOCUMENT) : return gesture.send()
			if mainKey == "leftArrow" :
				if utis.isChichi() : wx.CallLater(20, KeyboardInputGesture.fromName ("alt+f1").send) # commande chichi
				elif hasattr(o, "script_elementsList") : return o.script_elementsList(gesture) # foldersList dialog

			parID = str(utis.getIA2Attribute(o.parent))
			#if sharedVars.debug : sharedVars.log(o, "altArrow " + mainKey)
			if parID== "folderTree" :
				if mainKey == "downArrow" and hasattr(o, "script_altDown") : o.script_altDown(gesture)
				elif mainKey == "upArrow" and hasattr(o, "script_altUp") : o.script_altUp(gesture) 
			elif parID== "threadTree" :
				if mainKey in "upArrow,downArrow" : 
					try : messengerWindow.messageListItem.MessageListItem.script_readPreview(o, gesture)
					except :  messengerWindow.messageListItem.readPreview2(o, gesture)
				elif mainKey == "rightArrow" : wx.CallAfter(messengerWindow.messageListItem.gotoUnread, o, gesture)  
			elif role in  (controlTypes.Role.DOCUMENT, controlTypes.Role.LINK) :
				if mainKey in "upArrow,downArrow" : messengerWindow.document.Document.script_readDocument(o, gesture)
		elif role == controlTypes.Role.DOCUMENT  and sharedVars.curFrame == "msgcomposeWindow" :
			if mainKey in "upArrow,downArrow" : messengerWindow.document.Document.script_readDocument(o, gesture)
		elif  hasattr(o, "script_reportFocus") : # role == controlTypes.Role.EDITABLETEXT and sharedVars.curFrame == "spellCheckDlg" :
			return o.script_reportFocus(gesture)
		return gesture.send() 

	def script_sharedF4(self, gesture) :
		# lecture document 
		o = api.getFocusObject() # globalVars.focusObject api.getFocusObject()
		role = o.role

		if sharedVars.curTab in  ("main", "message") :
			if role not in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW, controlTypes.Role.DOCUMENT) : return gesture.send()

			parID = str(utis.getIA2Attribute(o.parent))
			#if sharedVars.debug : sharedVars.log(o, "altArrow " + mainKey)
			if parID== "folderTree" : 
				return gesture.send()
			elif parID== "threadTree" :
				try : messengerWindow.messageListItem.MessageListItem.script_readPreview(o, gesture)
				except : 
					api.setFocusObject(o)					
					messengerWindow.messageListItem.readPreview2(o, gesture)
					return # ui.message(str(o.role))
			elif role in  (controlTypes.Role.DOCUMENT, controlTypes.Role.LINK) :
				messengerWindow.document.Document.script_readDocument(o, gesture)
		elif role == controlTypes.Role.DOCUMENT  and sharedVars.curFrame == "msgcomposeWindow" :
			messengerWindow.document.Document.script_readDocument(o, gesture)
		return gesture.send() 
	script_sharedF4.__doc__ = _("Lecture filtrée du  document dans  le volet d'aperçu, l'onglet de lecture, la fenêtre de lecture ou de rédaction, depuis la liste de messages ou le document.")
	script_sharedF4.category = sharedVars.scriptCategory

	def script_sharedAltPageDown(self, gesture) :
		#beep(440, 20)
		fo = globalVars.focusObject
		if sharedVars.curTab in ("main", "message") :
			if gesture.mainKeyName == "pageDown"   : repeats = 1
			else : repeats = getLastScriptRepeatCount ()
			#messengerWindow.messageListItem.openListAttachment(fo, gesture)
			utis.openListAttachment2(fo, repeats)

	def script_showContextMenu(self, gesture) :
		global _timer
		repeats = getLastScriptRepeatCount ()
		if _timer is not None:
			_timer.Stop()
			_timer = None
		if sharedVars.curFrame == "messengerWindow" :
			oMenu = messengerWindow.menuMain.MainMenu(self)
			oMenu.showMenu(globalVars.focusObject)
		elif sharedVars.curFrame == "msgcomposeWindow" :
			if globalVars.focusObject.role != controlTypes.Role.DOCUMENT :
				_timer = None
				return
			if not sharedVars.oSettings.getOption("msgcomposeWindow", "onePress") : # not onePress to showMenu
				if repeats > 0 :
					oMenu = msgComposeWindow.menuCompose.ComposeMenu(self)
					_timer = wx.CallLater(10, oMenu.showMenu)
				elif repeats == 0 : # (dblPress and repeats== 0) or (not dblPress and repeats == 1) : 
					_timer = wx.CallLater(200, gesture.send)
			else : # menu with onePress
				if repeats > 0 :
					_timer = wx.CallLater(10, gesture.send)
				elif repeats == 0 : # (dblPress and repeats== 0) or (not dblPress and repeats == 1) : 
					oMenu = msgComposeWindow.menuCompose.ComposeMenu(self)
					_timer = wx.CallLater(200, oMenu.showMenu)
			return
		# elif sharedVars.curFrame == "addressbookWindow" :
			# globalVars.focusObject.script_showMenu(gesture)
	script_showContextMenu.__doc__ = _("Affiche le menu contextuel des actions  disponibles dans les différentes fenêtres de Thunderbird.")
	script_showContextMenu.category =sharedVars.scriptCategory

	def script_showOptionMenu(self, gesture) :
		global _timer
		#beep(440, 20)
		repeats = getLastScriptRepeatCount ()
		#ui.message("repeat : " + str(repeats))
		if _timer is not None:
			_timer.Stop()
			_timer = None
		if sharedVars.curFrame != "msgcomposeWindow" :
			sharedVars.oSettings.showOptionsMenu(sharedVars.curFrame) # menu dépendant du frame actif
		else :  # msgcomposeWindow
			if not sharedVars.oSettings.getOption("msgcomposeWindow", "onePress") : # not onePress to showMenu
				if repeats > 0 :
					_timer = wx.CallLater(10, sharedVars.oSettings.showOptionsMenu, sharedVars.curFrame)
				elif repeats == 0 : 
					_timer = wx.CallLater(200, gesture.send)
			else : # menu with onePress
				if repeats > 0 :
					_timer = wx.CallLater(10, gesture.send)
				elif repeats == 0 : # (dblPress and repeats== 0) or (not dblPress and repeats == 1) : 
					_timer = wx.CallLater(200, sharedVars.oSettings.showOptionsMenu, sharedVars.curFrame) # menu dépendant du frame acti
			return

	script_showOptionMenu.__doc__ = _("Affiche le menu contextuel des options de Thunderbird+")
	script_showOptionMenu.category = sharedVars.scriptCategory

	def script_sharedAltC(self,gesture):
		if sharedVars.curTab == "main" :
			wx.CallLater(10, messengerWindow.columnManager.manageColumns, self)
			return
		# if sharedVars.curFrame == "addressbookWindow" :
			# fo = globalVars.focusObject
			#if hasattr(fo, "script_setFocus_objMain") : return fo.script_setFocus_objMain(gesture)
		return gesture.send()
	script_sharedAltC.__doc__ = _("Agencement des colonnes dans la liste de messages.")
	script_sharedAltC.category = sharedVars.scriptCategory

	def script_sharedAltD(self,gesture):
		if sharedVars.curTab == "main" :
			wx.CallLater(10, messengerWindow.messageListItem.editDelay)
			return
		return gesture.send()
	script_sharedAltD.__doc__ = _("Affiche le dialogue d'édition du délai avant lecture du message de la fenêtre séparée de lecture.")
	script_sharedAltD.category = sharedVars.scriptCategory

	def script_previewPane(self, gesture) :
		# if sharedVars.curTab != "main" : return gesture.send()
		if globalVars.focusObject.role not in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW) : return gesture.send()
		KeyboardInputGesture.fromName ("f8").send()
		exp =  utis.getMessageHeadersFromFG(reportNotOpen=False)
		if exp :
			ui.message(_("Présent : volet des entêtes et du message."))
		else :
			ui.message(_("Absent : volet des entêtes et du message."))
	script_previewPane.__doc__ = _("Affiche ou masque le volet des entêtes et d'aperçu du message.")
	script_previewPane.category = sharedVars.scriptCategory

	def script_showHelp(self, gesture) :
		utis.showHelp()
	script_showHelp.__doc__ = _("Affiche l'aide de l'extension dans une page web")
	script_showHelp.category = sharedVars.scriptCategory

	def script_displayDebug(self, gesture) :
		# utis.listGestFromScanCodes()
		# return
		if sharedVars.curFrame == "messengerWindow" :
			utis.isChichi()
		sharedVars.debugLog += "\nChichi : " + str(sharedVars.chichi)
		debugShow(self, False)

	def script_initDebug(self, gesture) :
		sharedVars.testMode = (not sharedVars.testMode)
		mode = ("Activation" if sharedVars.testMode else u"Désactivation")
		sharedVars.debugLog = "TestMode = " + str(sharedVars.testMode) + "\n"
		ui.message(mode + _("du mode de test"))
	
	__gestures = {
		#"kb(desktop):NVDA+End": "statusBar",
		"kb:escape": "sharedEscape",
		"kb:alt+1": "sharedAltN",
		"kb:alt+2": "sharedAltN",
		"kb:alt+3": "sharedAltN",	
		"kb:alt+4": "sharedAltN",
		"kb:alt+5": "sharedAltN",
		"kb:alt+6": "sharedAltN",
		"kb:alt+7": "sharedAltN",
		"kb:alt+8": "sharedAltN",
		"kb:alt+9": "sharedAltPageDown", # attachments
		"kb:alt+pagedown":"sharedAltPageDown",
		"kb:alt+leftarrow": "sharedAltArrow",
		"kb:alt+rightarrow": "sharedAltArrow",
		"kb:alt+downarrow": "sharedAltArrow",
		"kb:alt+uparrow": "sharedAltArrow",
		"kb:f4": "sharedF4",
		"kb:shift+f4": "sharedF4",
		"kb:alt+End": "sharedAltEnd",
		utis.gestureFromScanCode(12, "kb:alt+") : "sharedAltEnd", # 2th  key at the left  of backspace
		"kb:control+tab": "sharedCtrlTab",
		"kb:control+shift+tab": "sharedCtrlTab",
		"kb:control+1": "sharedCtrlN",
		"kb:control+2": "sharedCtrlN",
		"kb:control+3": "sharedCtrlN",	
		"kb:control+4": "sharedCtrlN",
		"kb:control+5": "sharedCtrlN",
		"kb:control+6": "sharedCtrlN",
		"kb:control+7": "sharedCtrlN",
		"kb:control+8": "sharedCtrlN",
		"kb:control+9": "sharedCtrlN",
		"kb:control+0": "sharedCtrlN",
		utis.gestureFromScanCode(13, "kb:control+") : "sharedCtrlN", # 13 : first hey at the left of backspace
		utis.gestureFromScanCode(13, "kb:alt+") : "sharedAltEqual",
		"kb:alt+pageup": "sharedCtrlR", # smart reply
		"kb:control+r": "sharedCtrlR", # smart reply
		"kb:control+f4": "sendCtrlF4",
		"kb:control+w": "sendCtrlF4",
		"kb:control+backspace": "sendCtrlF4",
		utis.gestureFromScanCode(41, "kb:") :"showContextMenu", # 41 is the scancode of the key above Tab
		utis.gestureFromScanCode(41, "kb:shift+") :"showOptionMenu", 
		# _(u"kb:shift+control+²") :"showOptionMenu",
		# _(u"kb:control+²") :"showContextMenu",
		"kb:alt+c":"sharedAltC",
		"kb:alt+d":"sharedAltD",
		"kb:f8":"previewPane",
		"kb:control+f1": "showHelp",
		"kb:alt+f12": "displayDebug",
		"kb:windows+f12": "initDebug"
	}

class SearchBox(IAccessible):

	def script_nextOption(self, gesture):
		if not self.pointedObj:
			if int(self.appModule.productVersion.split(".")[0]) <= 68:
				self.pointedObj = self.parent.parent.firstChild
			else:
				self.pointedObj = self.parent.firstChild
		self.pointedObj = self.pointedObj.simpleNext
		isToolBarButton = False
		try:
			if self.pointedObj.IA2Attributes["tag"] == "toolbarbutton":
				isToolBarButton = True
				if "qfb-qs-" in self.pointedObj.IA2Attributes["id"]:
					self.pointedObj.name = _("Rechercher dans ")+self.pointedObj.name
		except (KeyError, AttributeError):
			pass
		while not isToolBarButton :
			try:
				self.pointedObj = self.pointedObj.simpleNext
				if self.pointedObj.IA2Attributes["tag"] == "toolbarbutton":
					isToolBarButton = True
					if "qfb-qs-" in self.pointedObj.IA2Attributes["id"]:
						self.pointedObj.name = _("Rechercher dans ")+self.pointedObj.name
			except:
				pass
			if not self.pointedObj or self.pointedObj.role == controlTypes.Role.TREEVIEW:
				#TRANSLATORS: message spoken when leaving the search box in Thunderbird
				ui.message(_('Sorti du champ de recherche'))
				self.pointedObj = self.parent.parent.firstChild
				gesture.send()
				return
		self.readCheckButton()

	def script_previousOption(self, gesture):
		if not self.pointedObj:
			api.setNavigatorObject(self)
			ui.message(controlTypes.role._roleLabels[self.role])
			if self.value:
				ui.message(self.value)
			return
		self.pointedObj = self.pointedObj.simplePrevious
		isToolBarButton = False
		try:
			if self.pointedObj.IA2Attributes["tag"] == "toolbarbutton":
				isToolBarButton = True
				if "qfb-qs-" in self.pointedObj.IA2Attributes["id"]:
					self.pointedObj.name = _("Rechercher dans ")+self.pointedObj.name
		except (KeyError, AttributeError):
			pass
		while not isToolBarButton :
			try:
				self.pointedObj = self.pointedObj.simplePrevious
				if self.pointedObj.IA2Attributes["tag"] == "toolbarbutton":
					isToolBarButton = True
					if "qfb-qs-" in self.pointedObj.IA2Attributes["id"]:
						#TRANSLATORS: Thunderbird search box name
						self.pointedObj.name = _("Rechercher dans ")+self.pointedObj.name
			except KeyError:
				pass
			except AttributeError:
				pass
			try:
				if not self.pointedObj or self.pointedObj == self.parent.parent.firstChild or "titlebar" in self.pointedObj.IA2Attributes["id"]:
					self.pointedObj = self.parent.parent.firstChild
					gesture.send()
					return
			except KeyError:
				pass
		self.readCheckButton()

	def script_pressButton(self, gesture):
		if self.pointedObj:
			if controlTypes.State.PRESSED in self.pointedObj.states:
				#TRANSLATORS: a button has been unchecked
				ui.message(_("décocher"))
			else:
				#TRANSLATORS: a button has been checked
				ui.message(_("cocher"))
			ui.message(self.pointedObj.name)
			api.moveMouseToNVDAObject(self.pointedObj)
			api.setMouseObject(self.pointedObj)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN,0,0,None,None)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP,0,0,None,None)

	def readCheckButton(self):
		if controlTypes.State.PRESSED in self.pointedObj.states:
			#TRANSLATORS: a button is checked
			state = _("coché")
		else:
			#TRANSLATORS: a button is not checked
			state = _("non coché")
		if self.pointedObj.description:
			ui.message("%s, %s, %s" % (self.pointedObj.name, state, self.pointedObj.description))
		else:
			ui.message("%s, %s" % (self.pointedObj.name, state))
		api.setNavigatorObject(self.pointedObj)

	def event_caret(self):
		if self.pointedObj:
			api.setNavigatorObject(self)
			self.pointedObj = None
			ui.message(controlTypes.role._roleLabels[self.role])

	# def event_stateChange(self, obj, nextHandler):
		# beep(500, 3)
		# nextHandler()

	__gestures = {
	"kb:downArrow": "nextOption",
	"kb:upArrow": "previousOption",
	"kb:Enter": "pressButton"
	}

def getIA2Attr (obj,attribute_value=False,attribute_name ="id"):
	r= hasattr (obj,"IA2Attributes") and attribute_name in obj.IA2Attributes.keys ()
	if not r :return ""
	r =obj.IA2Attributes[attribute_name]
	return r if not attribute_value  else r ==attribute_value

def findTree(obj, findID) :
	try :
		sharedVars.setLooping(True)
		# search for grouping : level 1,  46 of 49, Role.GROUPING, IA2ID : tabpanelcontainer Tag: tabpanels, States : , childCount  : 3 Path : Role-FRAME| i46, Role-GROUPING, , IA2ID : tabpanelcontainer , IA2Attr : display : -moz-deck, class : plain, tag : tabpanels, id : tabpanelcontainer, , Actions : click ancestor,  ;
		try : o = sharedVars.oCurFrame.getChild(sharedVars.groupingIdx)
		except : return None, 0
		while o :
			if o.role == controlTypes.Role.GROUPING :
				break
			o = o.next
		if not o : return None, 1
		# search  level 2,   0 of 3, Role.PROPERTYPAGE, IA2ID : mailContent Tag: box, States : , OFFSCREEN, childCount  : 5 Path : Role-FRAME| i46, Role-GROUPING, , IA2ID : tabpanelcontainer | i0, Role-PROPERTYPAGE, , IA2ID : mailContent , IA2Attr : display : -moz-box, id : mailContent, tag : box, , Actions : click ancestor,  ;
		# we are on the main Tab if property page  is not offscreen
		try :
			o = o.firstChild # propertypage
		except : return None, 2
		if controlTypes.State.OFFSCREEN in o.states : return None, 3 
			#  , path : : role FRAME=34| i31, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i1, role-TREEVIEW=20, , 
		# cherche premier controle utilisable
		o = o.firstChild
		while o :
			# if sharedVars.debug : sharedVars.log(o, "boucle rech controle")
			if str(utis.getIA2Attribute(o)) == findID :
				break
			o = o.next
		if not o :
			return None, 4
		# if sharedVars.debug : sharedVars.log(o, "a retourner")
		return o, 5
	finally :
		sharedVars.setLooping(False)
def setCurTab(appMod, oFrame=None) :
	if oFrame is None : oFrame = globalVars.foregroundObject
	sharedVars.curFrame = getFrameID(oFrame)
	ct , n = messengerWindow.tabs.findCurTab(oFrame)
	if n > -1  : 
		sharedVars.curTab = messengerWindow.tabs.getTabType(ct.name, n, oFrame)
		# ui.message("Onglet " + ct.name)
		ui.message("Onglet ")
	else : #appMod.curTab = 
		sharedVars.curTab = "not found"

# def setCurTab(appMod) :
	# fo = api.getFocusObject()
	# appMod.curFrame = sharedVars.curFrame = getFrameID(fo)
	# ct , n = messengerWindow.tabs.findCurTab(fo)
	# if n > -1  : 
		# appMod.curTab = sharedVars.curTab = messengerWindow.tabs.getTabType(ct.name, n)
		# ui.message("Onglet " + ct.name)
	# else : appMod.curTab = sharedVars.curTab = "not found"

def findPPFromFrame(o) :
	try :
		sharedVars.setLooping(True)
		if sharedVars.debug : sharedVars.log(o, "findPP")
		# Chemin : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent , IA2Attr : id : mailContent, 
		o = o.lastChild
		if sharedVars.debug : sharedVars.log(o, "lastChild de frame")
		while o :
			if sharedVars.debug : sharedVars.log(o, "boucle")
			if o.role == controlTypes.Role.GROUPING : # grouping
				break
			o = o.previous
		if  not o : 
			if sharedVars.debug : sharedVars.log(o, "grouping non trouver")
			return None
		o = o.firstChild # propertyPage	return o
		return o
	finally :
		sharedVars.setLooping(False)

def debugShow(appMod, auto) :
	sharedVars.log(globalVars.focusObject.parent, " focusObject.parent ", sharedVars.debug)
	sharedVars.log(globalVars.focusObject, " focusObject : ", sharedVars.debug)
	#sharedVars.debugLog += "\ncurFrame : {0}, curTab : {1},".format(appMod.curFrame, sharedVars.curTab) + "\n"
	sharedVars.debugLog += "\ncurTab : {0}, curFrame : {1},".format(sharedVars.curTab, sharedVars.curFrame) + "\n"
	# à revoir
	if auto :
		if globalVars.TBStep > 2 : return

	ui.browseableMessage (message = sharedVars.debugLog, title = _("Journal TB+4"), isHtml = False)
	if not auto : 
		sharedVars.debugLog = ""

from keyboardHandler import KeyboardInputGesture
def focusPage(appMod, frame=None, inStartup=False) :
	# beep(150, 30)
	# sharedVars.log(api.getFocusObject(), u"Entrée focusPage")
	if frame : fo = frame
	else : fo = api.getFocusObject()
	# if sharedVars.debug : sharedVars.log(fo, "focus object, inStartup : " + str(inStartup))
	if  sharedVars.curTab == "main" :
		if fo.role in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW, controlTypes.Role.DOCUMENT) : 
			return 
		treeID = "folderTree"
		while fo :
			if fo.role == controlTypes.Role.FRAME :
				break
			fo = fo.parent
		# if sharedVars.debug : sharedVars.log(fo, " avant findTree")
		fo, i = findTree(fo, treeID)
		if fo :
			fo.doAction()
			fo.setFocus()
			# if sharedVars.debug : sharedVars.log(fo, "Objet focus : ")
	elif sharedVars.curTab == "message" and fo.role == controlTypes.Role.FRAME :
		try :
			fo = findMessage(fo)
			if fo : fo.setFocus()
		except : pass
	elif sharedVars.curTab == "sp:downloads" and fo.role == controlTypes.Role.FRAME :
		wx.CallLater(100, ui.message, fo.name) 
		utis.sendKey("tab", 6)
	elif sharedVars.curTab == "sp:addons" and fo.role == controlTypes.Role.FRAME :
		wx.CallLater(50, speech.cancelSpeech) # ui.message, fo.name) 
		utis.sendKey("tab", 3)
		sleep(0.2)
		api.processPendingEvents()
		fo = api.getFocusObject()
		if sharedVars.debug : sharedVars.log(fo, "onglet addons focused ")
		fo = findAddonsSubTab(fo)
		if fo : 
			fo.doAction()
			fo.setFocus()
	elif sharedVars.curTab == "sp:addonsearch" : # and fo.role == controlTypes.Role.FRAME :
		# beep(200, 40)
		wx.CallLater(50, speech.cancelSpeech) # ui.message, fo.name) 
		sleep(4)
		utis.sendKey("tab", 6) # focus document
		sleep(0.2)
		api.processPendingEvents()
		fo = api.getFocusObject()
		#if sharedVars.debug : sharedVars.log(fo, "onglet addonsearch focused ")
	elif sharedVars.curTab == "sp:accounts" and fo.role == controlTypes.Role.FRAME :
		#wx.CallLater(100, ui.message, fo.name) 
		utis.sendKey("tab", 4)
	elif sharedVars.curTab == "sp:preferences" and fo.role == controlTypes.Role.EDITABLETEXT :
		speech.cancelSpeech()
		wx.CallLater(600, ui.message, _("Préférences"))  # il faudrait lire la barre de titre
		utis.sendKey("shift+tab", 4)
	elif sharedVars.curTab == "sp:addressbook" and fo.role == controlTypes.Role.DOCUMENT:
		speech.cancelSpeech()
		wx.CallLater(600, ui.message, _("Address Book"))  # il faudrait lire la barre de titre
		utis.sendKey("shift+tab", 4)
	# Comment by Rui Fontes: Don't understand what the code below does... It seems not necessary...
	#if sharedVars.curTab == "main" : 
		#filterSound()
	#speech.cancelSpeech()
	#if fo.role == controlTypes.Role.DOCUMENT: return
		#o = utis.findChildByID(obj, "messagepane")
		#if o : 
			# beep(400, 40)
			#try: 
				#o.firstChild.setFocus()
				#beep(400, 40) 
			#except : 
				#beep(120, 40)
				#pass

def trackTab(appMod, frame, tab, name, idx) :
	tt = messengerWindow.tabs.getTabType(name, idx, frame)
	if tt == "loading" :
		hwFG = winUser.getForegroundWindow()
		name = winUser.getWindowText(hwFG)
		if sharedVars.debug : sharedVars.log(None, "Rappel trackTab avec " + name)
		wx.CallLater(50, trackTab, appMod, frame, tab, name, idx)
		return
	globalVars.TBStep = 3
	sharedVars.curTab  = tt
	wx.CallLater(100, focusPage, appMod, frame) 
	if sharedVars.debug : sharedVars.log(None, "TrackTab curTab=" + sharedVars.curTab)

def findMessage(o) :
	# Chemin : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i12, role-INTERNALFRAME=115, , IA2ID : messagepane | i0, role-DOCUMENT=52,  
	# o doit avoir le role 34
	o = findPPFromFrame(o)
	if sharedVars.debug : sharedVars.log(o, "findMessage PropertyPage")
	o = o.firstChild
	while o :
		if o.role == controlTypes.Role.SECTION and utis.getIA2Attribute(o, "messagepane") : # rolle section avec document
			if sharedVars.debug : sharedVars.log(o, u"findMessage Section  trouvée")
			break
		o = o.next
	o = o.firstChild  # document 
	if sharedVars.debug : sharedVars.log(o, u"findMessage doit être role document") 
	return   o

def findAddonsSubTab(o) :
	if o.role != controlTypes.Role.DOCUMENT : return None
	# | i0, role-SECTION=86, , IA2ID : full 
	#| i0, role-SECTION=86, , IA2ID : sidebar 
	#| i0, role-TABCONTROL=23, , IA2ID : categories 
	#| i1, role-TAB=22,  , IA2Attr : 
	return o.firstChild.firstChild.firstChild.getChild(1)

def getParentByRole(obj, role) :
	while obj :
		if obj.role == role :
			return obj
		obj = obj.parent
	return None

def getFrameID(o) :
	# o is the frame object
	# language independant version and optimizes for main Windows and compose window
	try :
		sharedVars.objLooping = True
		if not o or o.role !=  controlTypes.Role.FRAME :
			o =  globalVars.foregroundObject
		t = o.name
		ID = str(utis.getIA2Attribute(o.firstChild))
		f = ID
		# sharedVars.log(o.firstChild, str(o.name)) 
		if ID == "emailAddressPopup" :
			# main windows or separate mail window
			if o.childCount < 40 :
				f ="1messageWindow"
			else : 		f = "messengerWindow"
			# cc = o.childCount
			# if cc > 49 : return "messengerWindow"
			# elif cc < 27 : 
				# f ="1messageWindow"
				# return f
		elif ID ==  "mailContext" :
			t = "comp"
			f=  "msgcomposeWindow"
		elif ID == "folderPropTabs" :
			f = "folderprops"
		elif ID == "filterNameLabel" : 
			f = "filterRules"
			t = "filter"
		elif ID == "activityContainer" :
			f = "activities"
		elif ID == "False" :
			ID = utis.getIA2Attribute(o)
			if ID : 
				f =  str(ID)
	finally :
		sharedVars.curFrame = f
		sharedVars.curTabe = t
		sharedVars.objLooping = False
		return f

# normal function
# functions for event alert
def focusAlert (message, oButton) :
	speech.cancelSpeech()
	speech.speak ([message])
	if oButton :
		oButton.setFocus()

def findButtonByName(o, nm) :
	o = o.firstChild
	while o :
		r = (o.role if hasattr(o, "role") else 0)
		if r == 9 :
			if nm in str(o.name) : return o
		o = o.next
	return None

def buildGroupRowName(appMod, oRow):
	try : o = oRow.firstChild
	except :  return oRow.name
	l  = ""
	while o :
		if hasattr(o, "name") :
			if "Col" not in o.name : l += o.name
		o = o.next
	if not l : return oRow.name
	return "+ " + l

def buildRowName2(appMod, oRow):
	try :
		sharedVars.objLooping = True
		# oCells : table Cells , children of table row
		options = sharedVars.oSettings.getOption("messengerWindow") # all options of tehe section
		listGroupName = options.as_bool ("listGroupName")
		cleanNames = options.as_bool ("namesCleaned")
		# v4.0.1
		# addSep = options.as_bool ("separateCols")
		colSepar = (", " if options.as_bool ("separateCols") else "")
		
		junkStatusCol = options.as_bool ("junkStatusCol")
		# playSound_unread = False #options.as_bool ("playsound_unread")
		
		# col IDs from thunderbird.appModule.buildColumnID() 
		# cells 	 of names or values 
		#if sharedVars.debug : sharedVars.log(oRow)
		#return oRow.name
			# beep(700, 2)
			# sharedVars.log(oRow, "* lenColID : {0}, LenCells : {1}, ColID : {2}, Name : {3}".format(lenColID, lenCells, str(appMod.columnID), oRow.name))
		#TRANSLATORS: "Réduit " stands for a collapsed branch in the  tree  in the message panel. In portugese : recolhido
		if controlTypes.State.COLLAPSED in oRow.states : l = _("Réduit ")
		else : l = ""
		i = 0
		try : o = oRow.firstChild
		except : return oRow.name
		while o  : 
			if  i < appMod.lenColID : 
				ID = appMod.columnID[i]
			else : ID ="unk"
			s = str(o.name) + " "
			# # if sharedVars.testMode :
				# message ("colonne : " + str(ID) + ", chaine  : " + str(s))
			if ID =="statusCol" :  
				if s=="statusCol " : s=_("Non lu ")
				elif s==_("Lu ") : s=" "
			elif ID == "attachmentCol" :
				if s != " " : s = _("PJ") + colSepar
			elif ID =="junkStatusCol" :
				if s=="100 "  and junkStatusCol: s = _(" indésirable ")
				elif s=="100 "  and  not junkStatusCol: s = " "
				elif s=="0 ": s=" "
			elif ID == "subjectCol" :
				if  ID in s : s = _("pas de sujet")
				s=removeResponseMention (appMod, s,1).strip (" -_*#").replace(" - "," ")
				# listgroup name repeats
				grp = utis.strBetween(s, "[", "]")
				# api.copyToClip("groupe " + grp)
				if grp :
					s= appMod.regExp_nameListGroup.sub (" ",s)
					if  not listGroupName :
						s =  grp + " : " +  s 
				#  v4.0.1 add separator 
				s = s + colSepar
			elif ID in ("dateCol","receivedCol") :
				if  ID in s : s = ""
			elif ID in ("correspondentCol","senderCol","recipientCol") :  # clean
				if ID in s : s = ""
				elif cleanNames : # nettoyage adresse mail
					s = appMod.regExp_removeSymbols.sub (" ",s) 
					# v4.0.1 add col separator
				s =s.strip() + colSepar
			elif id =="junkStatusCol"  and s== "100 " and junkStatusCol : s = _(" indésirable ")
			l +=  s + " "
			i += 1
			o = o.next
		return  appMod.regExp_removeMultiBlank.sub (" ",l.strip())
	finally :
		sharedVars.objLooping = False

def removeResponseMention (appMod,s,mode):
	mode = sharedVars.oSettings.responseMode
	if not mode : return s
	s , n= appMod.regExp_AnnotationResponse.subn(" ",s)
	if  mode == 1 : # "responseMentionGroup"
		s=(str (n) if n>1 else "")+(_("Ré ") if n else "")+s
	elif   mode == 3 : # "messengerWindow", "responseMentionDelColon" 
		s="Re"*n+" "+s
	return s 

def getDocType(o) :
	if o.role != controlTypes.Role.DOCUMENT : return -1
	o = o.parent.parent
	if not o : return -1
	if o.role == controlTypes.Role.FRAME : return 1 # doc in separate window
	elif controlTypes.Role.PROPERTYPAGE : return 0
	return -1

def filterSound() :
	# fullPath : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i11, role-EDITABLETEXT=8,  ,  
	o=globalVars.foregroundObject # frame
	o = utis.findChildByIDRev(o, "tabpanelcontainer") # role grouping
	o = utis.findChildByID(o,"mailContent") # property page
	o = utis.findChildByID(o,"qfb-results-label")
	if o and o.name : utis.playSound("filter")

def sayFilterInfos(appMod, sbar="") :
	from speech import speakSpelling 
	# fullPath : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i11, role-EDITABLETEXT=8,  ,  
	o=globalVars.foregroundObject # frame
	o = utis.findChildByIDRev(o, "tabpanelcontainer") # role grouping
	o = utis.findChildByID(o,"mailContent") # property page
	o = utis.findChildByID(o,"qfb-results-label")
	if not o or not o.name : return ui.message(sbar + _("Pas de filtrage  rapide."))
	ui.message (sbar + str(o.name) + _(" filtrés"))
	st= o.next.value
	if st is None : ui.message (_("Zone de recherche vide. "))
	else :
		ui.message(_("Expression entrée: %s")  %st)
		if len(st)>1 :speakSpelling (st) 
	# otpion buttons
	o=o.parent.firstChild.next
	iMax = 20
	i, k, st=0, 0,""
	while i<iMax and o.role!=28 : 
		if o.role== 9 : 
			if 16 in o.states : 
				st=st+o.name+", "
				k = k+1
		o = o.next 
		i = i+1
	if k==0 :
		ui.message( _("Aucune option  activée. "))
	else :
		ui.message(_("Les options activées sont: ") + st)		

def getFilterInfos(appMod) :
	# fullPath : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i11, role-EDITABLETEXT=8,  ,  
	o=globalVars.foregroundObject # frame
	o = utis.findChildByIDRev(o, "tabpanelcontainer") # role grouping
	o = utis.findChildByID(o,"mailContent") # property page
	o = utis.findChildByID(o,"qfb-results-label")
	if not o :  return _("Pas de filtrage  rapide.")
	t = o.name + _(" filtrés")
	st= o.next.value
	if st is None : t += _("Zone de recherche vide. ")
	else :
		t += _("Expression entrée: %s")  %st
	# otpion buttons
	o=o.parent.firstChild.next
	iMax = 20
	i, k, st=0, 0,""
	while i<iMax and o.role!=28 : 
		if o.role== 9 : 
			if 16 in o.states : 
				st=st+o.name+", "
				k = k+1
		o = o.next 
		i = i+1
	if k==0 :
		t += _("Aucune option  activée. ")
	else :
		t += _("Les options activées sont: ") + st
	return t

def setDialogID(o,wndClass ) :
	sharedVars.curTab = o.name  # dialog title
	ID = utis.getIA2Attribute(o) # pour spellCheckDlg par exempl
	if ID : 
		sharedVars.curFrame = str(ID)
		return
	if wndClass == "#32770" :
		sharedVars.curFrame = "commonDialog"
		return
	# edit contact dialog
	# if str(utis.getIA2Attribute(o.firstChild)) in("abPopupLabel", "abTabs") :
		# sharedVars.curFrame = "contactDialog"
		# return
	sharedVars.curFrame = wndClass

def copyClsList(clsList) :
	text = "clsList :\n"
	for e in clsList :
		text += str(e) + "\n"
	api.copyToClip(text)

def ttResetFocus(oRow) :
	KeyboardInputGesture.fromName("alt+f")
	beep(440, 30)
	# sleep(0.1)
	# KeyboardInputGesture.fromName("escape")
	api.processPendingEvents()
	# if oRow.previous :
		# beep(440, 30)
		# oRow.previous.setFocus()
		# api.processPendingEvents()
		# oRow.setFocus()
		# api.processPendingEvents()
	# else : 
		# oRow.next.setFocus()
		# api.processPendingEvents()
		# oRow.setFocus()
		# api.processPendingEvents()
