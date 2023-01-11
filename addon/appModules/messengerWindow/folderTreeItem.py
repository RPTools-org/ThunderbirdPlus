#coding:utf-8
# Thunderbird+ 4.x

import api
from time import sleep
from NVDAObjects.IAccessible import IAccessible
from ui import message, browseableMessage
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
from wx import CallAfter, CallLater
import winUser
import addonHandler,  os, sys
addonHandler.initTranslation()
from keyboardHandler import KeyboardInputGesture
from tones import  beep
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import utis, sharedVars
from  py3compatibility import *
from  py3compatibility import _unicode
del sys.path[-1]

from re import compile,IGNORECASE
regExp_excludeFolders =compile (_("brouillons|corbeille|\- \("), IGNORECASE)

lastSearch = ""


class FolderTreeItem (IAccessible):
	oLastNav = None
	spacePressed = False

	def initOverlayClass (self):
		# role =self.role # treeviewitem
		if str(utis.getIA2Attribute(self.parent)) != "folderTree" : return
		if  not sharedVars.objLooping :
			if sharedVars.useKeyNav and  sharedVars.directKeyNav :
				#beep(600, 20)
				self.bindKeyNav()
				# self.bindGestures({"kb:space":"tviNextUnread", "kb:alt+downArrow":"altDown", "kb:alt+upArrow":"altUp", "kb:z":"findFolder", "kb:shift+z":"findFolder"})
				if not sharedVars.FTnoSpace : 
					self.bindGestures({"kb:space":"tviNextUnread", "kb:z":"findFolder", "kb:shift+z":"findFolder", "kb:a":"activateKeyNav"})
				self.bindGestures({"kb:alt+downArrow":"altDown", "kb:alt+upArrow":"altUp", "kb:z":"findFolder", "kb:shift+z":"findFolder"})
			else :
				if not sharedVars.TTnoSpace : self.bindGestures({"kb:space":"tviNextUnread", "kb:z":"findFolder", "kb:shift+z":"findFolder", "kb:a":"activateKeyNav"})

	def script_tviNextUnread(self, gesture) :
		# beep(440, 40)
		unread = (True if "(" in self.name else False)
		isChichi = utis.isChichi() 
		self.spacePressed = True
		if unread and  sharedVars.oSettings.getOption("messengerWindow", "TTFirstUnread") :
			o = self.parent.next # threadTree
			if not o : 				return message(_("Liste de messages non trouvée."))
			o = o.getChild(1)
			if not o : 				return message(_("Liste de messages non trouvée."))
			fstUnread = False
			if _("Non lu") in o.name or "statusCol  " in o.name : fstUnread = True
			o.setFocus()
			# sharedVars.log(o, "ThreadTree : ")
			if not fstUnread : CallLater(20, KeyboardInputGesture.fromName ("n").send )
			return
		elif unread and not isChichi:
			return KeyboardInputGesture.fromName ("n").send ()
		elif unread and isChichi:
			o = self.parent.next # threadTree
			if not o : 				return message(_("Liste de messages non trouvée."))
			o.setFocus()
			# # sharedVars.log(o, "ThreadTree : ")
			CallLater(20, KeyboardInputGesture.fromName ("n").send )
		elif  not unread and isChichi : 
			CallLater(20, KeyboardInputGesture.fromName ("alt+f1").send ) # commande chichi
	script_tviNextUnread.__doc__ = _("sélectionne le premier message non lu dans la liste depuis l'arborescence des dossiers.")
	script_tviNextUnread.category = sharedVars.scriptCategory

	def script_altDown(self, gesture) :
		try :
			sharedVars.objLooping = True # évite l'insertion de cette classe pendant la recherche
			ti = self.next
			if not ti : return
			while ti :
				if ti.name.endswith(")") :
					if includeFolder(ti.name):
						break
				ti= ti.next
			if not ti : return beep(250, 10)
			if  controlTypes.State.INVISIBLE in ti.states :
				ti.scrollIntoView()
			ti.setFocus()
			ti.doAction()
			api.processPendingEvents()
			account = self.getAccountName(ti)
			CallLater(100, message, account)
		finally :	
			sharedVars.objLooping = False

	def script_altUp(self, gesture) :
		try :
			sharedVars.objLooping = True # évite l'insertion de cette classe pendant la recherche
			ti = self.previous
			if not ti.name : return beep(250, 10) 
			while ti :
				if ti.name.endswith(")") :
					if includeFolder(ti.name):
						break
				ti= ti.previous
				if  not ti.name : return beep(250, 10)

			if  controlTypes.State.INVISIBLE in ti.states :
				ti.scrollIntoView()
			ti.setFocus()
			ti.doAction()
			account = self.getAccountName(ti)
			CallLater(100, message, account)
		finally :	
			sharedVars.objLooping = False

	def getAccountName(self, ti) :
		if not ti : return ""
		if utis.getIA2Attribute(ti,"1", "level") : return " compte" # (" compte." if sharedVars.directKeyNav else ", compte.")
		while ti :
			if utis.getIA2Attribute(ti,"1", "level") :
				return _(" dans ") + ti.name
			ti = ti.previous
		return ""

	# navigation par initiales dans les  dossiers
	def bindKeyNav(self) :
		# liaison   des 26 lettres et 10 chiffres au script de navigation par initiale  dans les  dossiers
		if sharedVars.FTnoNavLetter : return
		kn = "abcdefghijklmnopqrstuvwxyz1234567890"
		for k in kn : 
			self.bindGestures ({"kb:"+k:"keyNav"})
			self.bindGestures ({"kb:shift+"+k:"keyNav"})
	def unbindKeyNav(self, ti) :
		kn = "abcdefghijklmnopqrstuvwxyz1234567890"
		for k in kn :
			ti.removeGestureBinding(k)
			ti.removeGestureBinding(k)
			ti.removeGestureBinding("shift+" + k)

	def script_activateKeyNav(self, gesture) :
		if not  sharedVars.useKeyNav : return gesture.send()
		self.bindKeyNav()
		self.bindGesture("kb:enter", "activateFolder")
		#beep(440, 20)
	#script_activateKeyNav.__doc__ = u"Active le mode navigation par initiale dans l'arborescence des dossiers de TB."
	#script_activateKeyNav.category="Thunderbird" #_scriptCategory

		#browseableMessage(text)

	def script_keyNav(self, gesture) :
		if self.spacePressed : 
			self.spacePressed = False
			return 
		try :
			sharedVars.setLooping(True)
			# beep(440, 10)
			if "shift" in gesture.modifierNames :
				o = self.navPrevFolders(gesture.mainKeyName.upper()) 
			else :
				o	 = self.navNextFolders(gesture.mainKeyName.upper()) 
			if o :
				self.oLastNav = o
				account = self.getAccountName(o)
			else : 
				o = (self if sharedVars.directKeyNav else self.oLastNav)
				if not o : o = self
				account =  (o.name if sharedVars.directKeyNav else "") + self.getAccountName(o) 
				#beep(250, 10)
			if o and sharedVars.directKeyNav :
				o.setFocus() 
				o.doAction()
				CallLater(100, message, account)
			else :
				message(o.name+ account)
		finally :
			sharedVars.setLooping(False)

	def navNextFolders(self, s) :
		if self.oLastNav :
			ti = self.oLastNav
		else :
			ti = self
		if iStartswith(ti.name, s) > -1 :
			ti = ti.next
		while ti :
			if iStartswith(ti.name, s) > -1 :
				return ti
			ti = ti.next
		return None

	def navPrevFolders(self, s) :
		if self.oLastNav :
			ti = self.oLastNav
		else :
			ti = self
		if not ti : return None
		if iStartswith(ti.name, s) > -1 :
			ti = ti.previous
		while ti :
			if ti.name and iStartswith(ti.name, s) > -1 :
				return ti
			ti = ti.previous
		return None

	def script_activateFolder(self, gesture) :
		if self.oLastNav :
			self.oLastNav.setFocus()
			self.oLastNav.doAction()

	# Dialogue de recherche 
	def script_findFolder(self, gesture) :
		global lastSearch
		if "shift" in gesture.modifierNames :
			utis.inputBox(label= _("mot-clé : "), title= _("Recherche en arrière d'un dossier"), postFunction=self.searchPreviousFolder, startValue=lastSearch)
		else :
			utis.inputBox(label= _("mot-clé : "), title= _("Recherche en avant d'un dossier"), postFunction=self.searchNextFolder, startValue=lastSearch)
	script_findFolder.__doc__ = _("Active le dialogue de recherche par mot-clé dans l'arborescence des dossiers.")
	script_findFolder.category= sharedVars.scriptCategory

	def searchNextFolder(self, searchStr) :
		global lastSearch
		if  not searchStr or searchStr == "ibCancel" :
			return
		if len(searchStr) == 1 :
			searchFunction = iStartswith
		else :
			searchFunction = iFind

		lastSearch = searchStr
		searchStr = searchStr.upper()
		ti = self
		setSearching(True)
		if searchFunction(str(ti.name), searchStr)  > -1 :
			ti = ti.next
		if not ti : return setSearching(False)
		while ti :
			if ti.role == controlTypes.Role.TREEVIEWITEM and searchFunction(str(ti.name), searchStr)> -1 :
				break
			ti = ti.next
		account = self.getAccountName(ti)
		setSearching(False)
		if not ti : 
			beep(250, 10)
			return
		if  (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE) in ti.states :
			ti.scrollIntoView()
		ti.setFocus()
		ti.doAction()
		CallLater(100, message, account)

	def searchPreviousFolder(self, searchStr) :
		global lastSearch
		if  not searchStr or searchStr == "ibCancel" :
			return
		if len(searchStr) == 1 :
			searchFunction = iStartswith
		else :
			searchFunction = iFind

		lastSearch = searchStr
		searchStr = searchStr.upper()
		ti = self
		setSearching(True)
		if searchFunction(str(ti.name), searchStr)  > -1 :
			ti = ti.previous
		if not ti : return setSearching(False)
		while ti :
			if ti.role == controlTypes.Role.TREEVIEWITEM and searchFunction(str(ti.name), searchStr)> -1 :
				break
			ti = ti.previous
		account = self.getAccountName(ti)
		setSearching(False)
		if not ti : 
			beep(250, 10)
			return			
		if  (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE) in ti.states :
			ti.scrollIntoView()
		ti.setFocus()
		ti.doAction()
		CallLater(100, message, account)

def includeFolder(name) :
	global regExp_excludeFolders
	result = regExp_excludeFolders.search(name)
	#z.mtlog.add(name + " : " + str(result))
	if result is None : return True
	else:  return False

def iStartswith(text, search) :
	t = text[0]
	return (1 if t.upper() == search else -1) 

def iFind(text, search) :
	#t = text.upper()
	return text.upper().find(search)

def setSearching(flag) :
	sharedVars.objLooping = flag
