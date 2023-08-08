#-*- coding:utf-8 -*
# version 4.x Thunderbird 102.x

from tones  import beep
# "expandedtagsBox":u"Étiquettes" 

#from threading import Thread
import speech 
from speech import speak, cancelSpeech
from scriptHandler import getLastScriptRepeatCount
import api, globalVars
import winUser
from api import copyToClip
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
from keyboardHandler import KeyboardInputGesture
from oleacc import ROLE_SYSTEM_LINK, ROLE_SYSTEM_TOOLBAR, ROLE_SYSTEM_TEXT,STATE_SYSTEM_MARQUEED, STATE_SYSTEM_PRESSED, ROLE_SYSTEM_SEPARATOR, STATE_SYSTEM_SELECTED, STATE_SYSTEM_SELECTABLE, STATE_SYSTEM_FOCUSABLE
from NVDAObjects.IAccessible import IAccessible, getNVDAObjectFromPoint
# controlTypes importé au début 
if not hasattr(controlTypes, "Role"):
	from controlTypes import ROLE_UNKNOWN, ROLE_LINK, STATE_PRESSED, STATE_COLLAPSED, STATE_SELECTED
else:
	ROLE_UNKNOWN = controlTypes.Role.UNKNOWN
	ROLE_LINK = controlTypes.Role.LINK
	STATE_PRESSED = controlTypes.State.PRESSED
	STATE_COLLAPSED = controlTypes.State.COLLAPSED
	STATE_SELECTED = controlTypes.State.SELECTED
from wx import CallAfter, CallLater
from UIAHandler import handler, UIA_ControlTypePropertyId, UIA_ToolBarControlTypeId, TreeScope_Children, TreeScope_Descendants, UIA_ButtonControlTypeId, UIA_LegacyIAccessibleRolePropertyId, UIA_LegacyIAccessibleValuePropertyId, UIA_TextControlTypeId, UIA_LegacyIAccessibleStatePropertyId, UIA_ListControlTypeId, UIA_ListItemControlTypeId, IUIAutomationInvokePattern, UIA_LegacyIAccessibleKeyboardShortcutPropertyId, UIA_LegacyIAccessibleNamePropertyId, UIA_DocumentControlTypeId, UIA_EditControlTypeId, UIA_CustomControlTypeId,UIA_NamePropertyId, UIA_LegacyIAccessibleDescriptionPropertyId , UIA_TreeItemControlTypeId , UIA_NamePropertyId 
from UIAHandler import UIA_SelectionItemIsSelectedPropertyId ,UIA_ItemStatusPropertyId,UIA_TreeControlTypeId  
clientObject =handler.clientObject
GetFirstChildElement, GetNextSiblingElement, GetParentElement, GetLastChildElement    = clientObject.RawViewWalker.GetFirstChildElement, clientObject.RawViewWalker.GetNextSiblingElement, clientObject.RawViewWalker.GetParentElement, clientObject.RawViewWalker.GetLastChildElement
from ui import message, browseableMessage
import addonHandler,  os, sys
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import  utis, sharedVars
from utis import versionTB
from . import foldersMessages
# import zDevTools as z
del sys.path[-1]
addonHandler.initTranslation()

from time import time, sleep

CPC=clientObject.CreatePropertyCondition 
WM_KEYDOWN, WM_KEYUP, VK_NUMPAD0 = 256, 257, 96
from ctypes import windll 
postMessage =windll.user32.PostMessageA
_timer = None


class MessageListItem(IAccessible):
	#lastScriptName=False
	def initOverlayClass (self):
		if str(utis.getIA2Attribute(self.parent)) != "threadTree" : return
		self.bindGesture ("kb:escape", "escape") 
		for e in  range(1,10) : self.bindGestures ({"kb:shift+"+utis._unicode(e):"sayMessageTags"})
		self.bindGesture ("kb:shift+0", "removeMessageTags")
		self.bindGesture ("kb:Alt+0", "sayMessageTags")
		if self.role in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW, controlTypes.Role.DOCUMENT) and self.hasFocus :  #  treeviewitem or tablerow 
			# sharedVars.log(None, "Avant bindgesture, sharedVars.TTnoSpace=" + str(sharedVars.TTnoSpace))
			if not sharedVars.TTnoSpace :
				# beep(600, 20)
				self.bindGesture ("kb:space", "readPreview")
				self	.bindGesture ("kb:shift+space", "readPreview")
			self.bindGestures(
			{"kb:a" : "sayShortcut",
			"kb:shift+c" : "sayShortcut",
			"kb:j" : "sayShortcut",
			"kb:shift+j" : "sayShortcut",
			"kb:f" : "showFilterBar",
			"kb:m" : "sayUnreadMessage"
			})
			# pour F4  , voir sharedF4 dans thunderbird.py
			# pour alt+ xx Arrow , voir sharedAltArrow dans thunderbird.py

	# na	vigation scripts
	def script_escape(self, gesture):
		#beep(700, 30)
		# v 3.4 :si menu Choisir les colonnes à afficher est ouvert
		# script_exitColumns se trouve dans columnManager.py 
		# if hasattr(self, "exitColumns") :
			# return self.exitColumns(gesture)
		# v 3.2.2 2022-01-05 
		role = self.role
		if role in (controlTypes.Role.TREEVIEWITEM, controlTypes.Role.TABLEROW) :
			obj = self.parent
		else :
			return gesture.send()

		ID = str(utis.getIA2Attribute (obj) )
		if ID == "threadTree"  :
			# filtre rapide
			if  obj.previous.role == controlTypes.Role.EDITABLETEXT : #feditable vide, pas de boutons
				CallAfter(message, _("Quick Filter Bar closed. Table."))
				return gesture.send()
			elif  obj.previous.role ==  controlTypes.Role.BUTTON :
				#gesture.send() # vide la zone éditable
				return  CallAfter(KeyboardInputGesture.fromName ("shift+tab").send) 
			else : # threadtree
				if sharedVars.oSettings.getOption("chichi", "TTnoEscape") : return gesture.send()
				return  KeyboardInputGesture.fromName ("shift+f6").send () # revenir à l'arborescence des dossiers
		elif  ID == "folderTree" :
			return  KeyboardInputGesture.fromName ("f6").send () # aller à la liste des messages
		# Autres cas
		return			 gesture.send()

	def script_tab (self,gesture):
		if sharedVars.oSettings.getOption("chichi", "MainNoTab") : return gesture.send()
		#beep(200, 20)
		# si pas dans liste messages ou arb disc groupées, renvoie directement le geste de commande 
		#try : # 2021.07.03 try ajouté car plantages de TB dans certains cas
		r= self.role
		if  r not in (controlTypes.Role.TREEVIEWITEM, controlTypes.Role.TABLEROW) :
			gesture.send()
			return
		#except:
			#return
		# si ligne pas sélectionnée 
		if controlTypes.State.SELECTED in self.states : 
			self.doAction ()
			#Délai nécessaire sinon NVDA parle trop
			CallLater (40, KeyboardInputGesture.fromName ("f6").send)
			return
		KeyboardInputGesture.fromName ("f6").send ()

	# read headers scritps with alt+n
	def script_readOtherField (self,gesture, oFocus=None):
		global _timer
		#beep(440, 20)
		repeats = getLastScriptRepeatCount ()
		if _timer is not None:
			_timer.Stop()
			_timer = None
		if repeats in (0, 2) : delay = 5 # annonce entête ou ouverture menu contextuel de la zone des entêtes
		elif repeats == 1 : delay = 300 # affichage dialogue Copier dans le presse-papiers
		# message("Read other fields depuis messageListItem")
		#_timer = CallLater(delay, readHeaders, oFocus, msgHeader, int(gesture.mainKeyName), repeats, delay) # key, repeatCount, delay
	script_readOtherField.__doc__ = _("Read different headers of a message.")
	script_readOtherField.category=sharedVars.scriptCategory

	def script_attachments(self, gesture): # alt+9
		# alt+9 : 0 orepeat  : says number of attachements,  1 repeat open list attachment
		# alt+pageDown : 0 repeat, open list attachments
		if gesture.mainKeyName == "9" and getLastScriptRepeatCount()==0 : 
			return utis.openListAttachment2(self, None) # sans gesture, dit seulement le nombre de PJ.
		else :
			return utis.openListAttachment2(self, gesture) 
	script_attachments.__doc__ = _("Single Press: Announces the number of attachments if any. Double Press: shows the list.")
	script_attachments.category=sharedVars.scriptCategory

	# begin tags 
	def getTagName(self, tagNo="1") :
		if tagNo > "6" :
			return tagNo
		#tagNo = str(tagNo)
		if tagNo < "1" or tagNo > "9" : return None
		# 0 of  1, name : Étiquette, role.POPUPMENU=12, IA2ID : mailContext-tagpopup Tag: menupopup, états : , COLLAPSED, INVISIBLE, OFFSCREEN, childCount  : 11 Chemin : role FRAME=34| i2, role-POPUPMENU=12, , IA2ID : mailContext | i11, role-MENUITEM=11, , IA2ID : mailContext-tags | i0, role-POPUPMENU=12, , IA2ID : mailContext-tagpopup , IA2Attr : explicit-name : true, id : mailContext-tagpopup, display : -moz-popup, tag : menupopup, , Actions : click ancestor,  ;
		o = sharedVars.oCurFrame # globalVars.foregroundObject
		# sharedVars.debugLog = ""
		# if sharedVars.debug : sharedVars.log(o, "frame   ", False)
		# | i2, role-POPUPMENU=12, , IA2ID : mailContext | i11, role-MENUITEM=11, , IA2ID : mailContext-tags | i0, role-POPUPMENU=12, , IA2ID : mailContext-tagpopup 
		o = utis.findChildByID(o,  "mailContext")
		# if sharedVars.debug : sharedVars.log(o, " child ", False)
		o = utis.findChildByID(o,  "mailContext-tags")
		# if sharedVars.debug : sharedVars.log(o, " child ", False)
		o = utis.findChildByID(o,  "mailContext-tagpopup")
		# if sharedVars.debug : sharedVars.log(o, " child ", False)
		#      5 of 10, name : 1 Important	1, role.CHECKMENUITEM=60 Tag: menuitem, états : , CHECKED, INVISIBLE, SELECTABLE, FOCUSABLE, CHECKABLE Chemin : role FRAME=34| i2, role-POPUPMENU=12, , IA2ID : mailContext | i11, role-MENUITEM=11, , IA2ID : mailContext-tags | i0, role-POPUPMENU=12, , IA2ID : mailContext-tagpopup | i5, role-CHECKMENUITEM=60,  , IA2Attr : explicit-name : true, checkable : true, display : -moz-box, tag : menuitem, , Actions : click,  ;
		try :
			sharedVars.objLooping = True
			o = o.getChild(5)
			while o :
				# if sharedVars.debug : sharedVars.log(o, " menu item  ", False)
				if o.name.startswith(tagNo) : 
					nm = o.name.split("\t")
					nm = nm[0]
					return nm[2:]
				o = o.next
			return None
		finally :
			sharedVars.objLooping = False

	def getMessageTagSet(self) :
		tagSet =set ()
		o =  utis.getMessageHeadersFromFG(reportNotOpen=True)
		if not o : return tagSet
		#| i3, role-SECTION=86, , IA2ID : expandedtagsRow  
		o = utis.findChildByID(o, "expandedtagsRow")
		if not o : return tagSet
		# modifié 102.b4
		#| i1, role-SECTION=86, , IA2ID : expandedtagsBox 
		o = utis.findChildByID(o, "expandedtagsBox")
		# | i0, role-LIST=14,  
		o = o.firstChild
		# | i0, role-LISTITEM=15,  , IA2Attr : setsize : 2, display : list-item, class : tag, tag : li, posinset : 1, formatting : block, , Actions : click ancestor,  ;
		o = o.firstChild
		while o :
			tagSet.add(o.name)
			o = o.next
		return tagSet

	def getMessageTagStr(self) :
		TagSet =  self.getMessageTagSet() 
		return setToStr(TagSet, _("Tags"), _("No tag."))

	def script_sayMessageTags(self,gesture):
		lblTags = _("Tags")
		#Translators: Tags feature
		lblNoTags = _("No tag.")
		if gesture.mainKeyName == "0" :
			msgTags = setToStr(self.getMessageTagSet(), lblTags, lblNoTags)
			return message(msgTags)
		#translators
		lblNoMore = _("No More tag.")
		lblAdded = _("added")
		lblRemoved = _(" removed")
		prevTagSet = self.getMessageTagSet() 
		# 2022-1215 : explicit key name send necessary
		KeyboardInputGesture.fromName(gesture.mainKeyName).send()
		sleep(0.2)
		api.processPendingEvents()
		newTagSet =  self.getMessageTagSet() 
		tagChanged =newTagSet.difference(prevTagSet)
		if not tagChanged  :tagChanged = prevTagSet.difference(newTagSet)
		# return message("tagChanged" + str(tagChanged))
		msg  = list(tagChanged)[0]+" "+(lblAdded,lblRemoved)[len(prevTagSet)>len(newTagSet)]
		msg ="{0}, {1}".format(msg,setToStr(newTagSet, lblTags, lblNoMore))
		message (msg)
		#message(u"Changé" + str(tagChanged))
		#message(u"étiquettes : " + str(newTagSet))
		return
		# translator 
		lblTag = _("tag")
		lblNoMore = _("No more tag.")
		lblAdded = _("added")
		lblRemoved  = _("removed")
		msgTags = self.getMessageTags()
		if not msgTags : 
			msgTags =  lblNoMore
		newState = (lblAdded if tagName in msgTags else lblRemoved)
		message("{0} : {1} {2}, {3}".format(lblTag, tagName, newState, msgTags))
	script_sayMessageTags.__doc__ = _("Shift + 1 to 8: announces the additions or removals of tags, Shift+0 announces the tags of the message")
	script_sayMessageTags.category=sharedVars.scriptCategory

	def script_removeMessageTags(self,gesture):
		# translator
		lblNoTag = _("No tag to remove.")
		msgTags = self.getMessageTagSet()
		if not msgTags :  
			return message(lblNoTag)
		rc =  getLastScriptRepeatCount ()
		if rc == 0 :
			# translator 
			lblPressTwice = _("Press this command twice quickly to delete the") 
			msgTags = setToStr(msgTags, lblPressTwice) 
			return message(msgTags)
		elif rc   == 1:
			KeyboardInputGesture.fromName("0").send()
			# translator
			lblNoTag = _("All tags have been removed from this message.")
		return CallLater(40, message, lblNoTag)
	script_removeMessageTags.__doc__ = _("Removes all tags from the selected message.")
	script_removeMessageTags.category=sharedVars.scriptCategory
	# end of Message tags

	# read preview panel
	def script_readPreview(self, gesture) :
		global _timer
		# sharedVars.log(None, "Dans readPreview, sharedVars.TTnoSpace=" + str(sharedVars.TTnoSpace))
		if sharedVars.TTnoSpace and gesture.mainKeyName == "space" :
			# message("Lecture avec Chichi")
			CallAfter(gesture.send)
			return
		# sharedVars.log(self, "_readPreview with " + gesture.mainKeyName)
		checkFocus(self, None)
		oPP = utis.getPropertyPageFromFG() 
		oPane = utis.getPreviewPane(oPP)
		if not oPane : 
			return message(_("The preview pane is not displayed. Press F8 and try again please"))
			# determine how to read the doc
		rc = getLastScriptRepeatCount ()
		if _timer is None:
			_timer = CallLater(20, self.script_readPreview, gesture)
			return
		else :
			_timer.Stop()
			_timer = None
		if not _timer and rc > 0 and utis.isChichi() :
			#beep(0, 40)
			# sleep(0.3)
			message(_("Links"))
			return CallLater(20, chichiLinks, 2)

		if _timer : return
		filt = True
		if rc >0 :
			filt = False

		rev = False  # reverse 
		if  "up" in gesture.mainKeyName or("shift" in gesture.modifierNames) :
			rev = True
		if rev and not filt :
			message (_("Uncleaned reading in reverse is not available."))
			return
		# get   document  object
		# path : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i14, role-INTERNALFRAME=115, , IA2ID : messagepane | i0, role-DOCUMENT=52,  , 
		i = 0
		while i < 20 :
			o = oPane.firstChild
			if o and hasattr(o, "role") : 
				if o.role == controlTypes.Role.DOCUMENT :
					break
			beep(350, 2)
			sleep(0.3)
			api.processPendingEvents()
			i += 1

		if not o :
			return message(_("Message unavailable. Try again."))
		if o.childCount == 0  :
			return message(self.name + ", " + o.name)
		if not sharedVars.oQuoteNav : sharedVars.initQuoteNav() 
		sharedVars.oQuoteNav.readMail(o, rev, filt)
	script_readPreview.__doc__ = _("Filtered reading of the message preview pane without leaving the list.")
	script_readPreview.category=sharedVars.scriptCategory

	def script_sayShortcut (self,gesture):
		# beep(440, 10)
		if gesture.mainKeyName == "a" :
			# no need to check if the button is present in the toolbar
			message(_("Archived"))
			return gesture.send()
		elif gesture.mainKeyName == "c"  and"shift" in gesture.modifierNames :
			folder = self.windowText.split (" - ")[0]
			rc =  getLastScriptRepeatCount ()
			if rc == 0 : return message(_("Press this command twice to mark all messages as read in the folder:" + folder))
			else :
				gesture.send()
				return message(_("the {name} folder no longer contains unread messages.").format (name = folder))
		elif gesture.mainKeyName == "j" : #   junk mail
			newState = (_("not junk") if "shift" in gesture.modifierNames else _("junk"))
			if _("selected") in utis.getStatusBarText() :
				message(_("The status {0} has been applied to the selection").format(newState)) 
			else :
				message(_("The {0} status has been applied to this message").format(newState))
			return			 gesture.send()

	def script_showFilterBar(self, gesture) :
		#if self.role not in  (controlTypes.Role.TREEVIEWItem, controlTypes.Role.TABLEROW) : return gesture.send()
		if str(utis.getIA2Attribute(self.parent)) != "threadTree" : return gesture.send()
		return  KeyboardInputGesture.fromName ("control+shift+k").send()
	script_showFilterBar.__doc__ = _("Shows the quick filter bar from the message list.")
	script_showFilterBar.category=sharedVars.scriptCategory

	def script_sayUnreadMessage (self,gesture):
		# bound to m key
		o = self.parent
		if not o or utis.getIA2Attribute (o)!="threadTree" :
			return gesture.send ()
		#if sharedVars.debug : sharedVars.log(o, "container")
		o=(e for e in o.firstChild.children )
		for e in o:
			ID =  utis.getIA2Attribute (e) 
			if ID in ("unreadButtonColHeader", "statusCol") :
				#if sharedVars.debug : sharedVars.log(e, u" Colonne trouvée " + ID)
				break
		else:
			return gesture.send ()
		name =e.name
		#if sharedVars.debug : sharedVars.log(None, "Nom colonne : " + name)  
		o=(e for e in self.children)
		for e in o :
			#if sharedVars.debug : sharedVars.log(None, "contenu  col avant changement :" + str(e.name))
			if e.columnHeaderText ==name:break
		gesture.send ()
		api.processPendingEvents() # ajouté le 12-01-2022
		#if sharedVars.debug : sharedVars.log(None, u"contenu  col après  changement :" + str(e.name))
		CallLater(50, self.sayNewReadState, e) # 2022-01-12
	script_sayUnreadMessage.__doc__ = _("Reverses the read and unread status of the selected message")
	script_sayUnreadMessage.category=sharedVars.scriptCategory

	def sayNewReadState(self, e) : # 2022-01-12
		name = e.name
		if name == "" : name = _("read")
		elif name == "statusCol" : name = _("unread")
		#Translators: bug fixed on 2022-12-15
		message(_("Message marked as ") + name)

	def script_showFoldersMessages(self,gesture):	
		withUnread = sharedVars.oSettings.getOption("messengerWindow", "WwithUnread")
		foldersMessages.FoldersMessagesList.run(withUnread)		
	script_showFoldersMessages.__doc__ = _("Shows a dialog with the list of folders")
	script_showFoldersMessages.category=sharedVars.scriptCategory

	__gestures={
		"kb:tab":"tab",
		"kb:F12":"showFoldersMessages"
	}

# function helpers
#  get recipients contained in a field
def getRecip(oParent) : # of role section
	# sharedVars.debugLog = "fonction getRecip\n"
	o  =  oParent.getChild(1).firstChild 
	if sharedVars.debug : sharedVars.log(o, " doit etre list ")
	lbl = o.name + " : "
	# 0 sur 1, name : nvda-fr@groups.io Pas dans le , role.LISTITEM=15, IA2ID : toRecipient0 
	o = oFirst= o.firstChild
	text = ""
	while o : 
		if sharedVars.debug : sharedVars.log(o, " o ", False)
		if o.role == controlTypes.Role.LISTITEM : 
			nm = o.firstChild.name
			if nm is None : nm = o.firstChild.firstChild.name
			text = text + str(nm) + ";"
		o = o.next
	return oFirst, lbl, text[0:-1] 

def readHeaders(fobj, msgHeader, k, rc, delay) : # key, repeatCount, delay
	#translators: header labels : "none,From,Subject: ,Date,To,CC,BCC,Reply to" 
	fieldLabels = _("void,From,Subject: ,Date,To,CC,BCC,Reply to") 
	fldMessageFound = _("{0} {1}") 
	fldMessageNotFound = _("The {0} header is missing from this message.")
	try :
		sharedVars.objLooping = True
		#beep(200, 60)
		# sharedVars.debugLog = ""
		# from : 0 sur 4, role.SECTION=86, IA2ID : headerSenderToolbarContainer Tag: div, états : , childCount  : 2 Chemin : role FRAME=34| i19, role-LANDMARK = 149, , IA2ID : messageHeader | i0, role-SECTION=86, , IA2ID : headerSenderToolbarContainer , IA2Attr : display : flex, id : headerSenderToolbarContainer, tag : div, class : message-header-row header-row-reverse message-header-wrap items-center, , Actions : click ancestor,  ;
		# o = msgHeader.firstChild
		# while o :
			# if sharedVars.debug : sharedVars.log(o, " messageHeader Child ", False)
			# o = o.next
		#beep(500, 20)
		# messageHeader Child  : role : 86, ID : headerSenderToolbarContainer, childCount : 2name : None
		# messageHeader Child  : role : 86, ID : expandedtoRow, childCount : 3name : None
		# messageHeader Child  : role : 86, ID : headerSubjectSecurityContainer, childCount : 1name : None
		# messageHeader Child  : role : 86, ID : expandedtagsRow, childCount : 2name : None
		if k == 1 : # de : / from
			# look for : messageHeader Child  : role : 86, ID : headerSenderToolbarContainer, childCount : 2name : None
			o = utis.findChildByID(msgHeader, "headerSenderToolbarContainer")
			# look for : | i1, role-SECTION=86, , IA2ID : expandedfromRow 
			o = o.getChild(1)
			# new 
			#| i1, role-SECTION=86, , IA2ID : expandedfromBox 
			o = o.getChild(1)
			#| i0, role-LIST=14,  
			o = o.firstChild
			fldLabel = o.name 
			#| i0, role-LISTITEM=15, , IA2ID : fromRecipient0
			o = o.firstChild # first list item
			fldVal = o.firstChild.name # if in addressbook
			if fldVal is None :
				fldVal = o.firstChild.firstChild.name # if not in addressbook
			oField = o
			fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 2 : # subject
			# messageHeader Child  : role : 86, ID : headerSubjectSecurityContainer, childCount : 3name : None
			oField = utis.findChildByID(msgHeader, "headerSubjectSecurityContainer")
			# sharedVars.debugLog = "Sujet :\n"
			# if sharedVars.debug : sharedVars.log(oField, "", False)
			if not oField :
				fldMessage = fldMessageNotFound.format(fieldLabels.split(",")[k])
			else : 
				oField = oField.firstChild.getChild(1).firstChild
				# if sharedVars.debug : sharedVars.log(oField, " valeur : " + oField.name, False)
				fldLabel = fieldLabels.split(",")[k] 
				fldVal = oField.name
				fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 3 : #date
			# 0 sur 0, name : 06:17, role.STATICTEXT=7, états :  Chemin : role FRAME=34| i19, role-LANDMARK = 149, , IA2ID : messageHeader | i1, role-SECTION=86, , IA2ID : expandedtoRow | i2, role-TEXTFRAME=91, , IA2ID : dateLabel | i0, role-STATICTEXT=7,  , 
			oField = utis.findChildByID(msgHeader, "expandedtoRow")
			# | i2, role-TEXTFRAME=91, , IA2ID : dateLabel | i0, role-STATICTEXT=7
			oField =  oField.getChild(2).firstChild
			message(fieldLabels.split(",")[k] + ": " + oField.name)
			return

		elif k == 4 : # expandedtoRow 
			# messageHeader Child  : role : 86, ID : expandedtoRow, childCount : 3name : None
			oField = utis.findChildByID(msgHeader, "expandedtoRow")
			if not oField :
				fldMessage = fldMessageNotFound.format(fieldLabels.split(",")[k])
			else : 
				oField, fldLabel, fldVal =  getRecip(oField)
				# fldLabel = fieldLabels.split(",")[k]
				fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 5 : # expandedccRow 
			# messageHeader Child  : role : 86, ID : expandedccRow , childCount : 3name : None
			oField = utis.findChildByID(msgHeader, "expandedccRow")
			if not oField :
				fldMessage = fldMessageNotFound.format(fieldLabels.split(",")[k])
			else : 
				oField, fldLabel, fldVal = getRecip(oField)
				# fldLabel = fieldLabels.split(",")[k]
				fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 6 : # expandedbccRow 
			# messageHeader Child  : role : 86, ID : expandedbccRow  , childCount : 3name : None
			oField = utis.findChildByID(msgHeader, "expandedbccRow")
			if not oField :
				fldMessage = fldMessageNotFound.format(fieldLabels.split(",")[k])
			else : 
				oField, fldLabel, fldVal =  getRecip(oField)
				# a revoir à la version RC1 fldLabel = fieldLabels.split(",")[k]
				fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 7 : # expandedreply-toRow 
			# messageHeader Child  : role : 86, ID : expandedreply-toRow   , childCount : 3name : None
			oField = utis.findChildByID(msgHeader, "expandedreply-toRow")
			if not oField :
				fldMessage = fldMessageNotFound.format(fieldLabels.split(",")[k])
			else : 
				oField, fldLabel, fldVal =  getRecip(oField)
				# fldLabel = fieldLabels.split(",")[k]
				fldMessage = fldMessageFound.format(fldLabel, fldVal)
		elif k == 8 : # all headers
			#  |1 of 1, name : Agent utilisateur: Microsoft O, role.UNKNOWN=0, IA2ID : expandeduser-agentBox Tag: mail-headerfield,  Chemin : role FRAME=34| i19, role-LANDMARK = 149, , IA2ID : messageHeader | i7, role-SECTION=86, , IA2ID : expandeduser-agentRow | i1, role-UNKNOWN=0, , IA2ID : expandeduser-agentBox , IA2Attr : class : headerValue, explicit-name : true, id : expandeduser-agentBox, display : flex, tag : mail-headerfield, , Actions : click ancestor,  ;
			oField = utis.findChildByID(msgHeader,"expandeduser-agentRow")
			if not oField :
				message(_("The complete list of headers is not displayed."))
				return
			#| i7, role-SECTION=86, , IA2ID : expandeduser-agentRow | | i1, role-UNKNOWN=0, , IA2ID : expandeduser-
			oField = oField.getChild(1)
			#oField.scrollIntoView()
			parts = oField.name.split(": ")
			fldLabel = parts[0]
			fldVal = parts[1]
			fldMessage = fldMessageFound.format(fldLabel, fldVal)
		# common
		if rc  >= 2 : 
			oField.doAction()
		elif rc == 1 : 
			CallLater(100, utis.inputBox , label=fldLabel, title= _("Copy to clipboard"), postFunction=None, startValue=fldVal)
		elif rc == 0 :
			message(fldMessage)
		return
	finally :
		sharedVars.objLooping = False
def setState(o, state, strAction, action=None) :
	if state in o.states : 
		return
	i = 0
	while i < 20 and state not in o.states :
		# exception if o is a not expandable treeviewItem
		try : o.doAction(action) 
		except : return
		sleep(0.05)
		api.processPendingEvents()
		i += 1
	# sharedVars.log(o, "setState, {0}, count : {1}, ".format(strAction, str(i)))

def checkFocus(obj, gesture=None) :
	role = obj.role
	if role == controlTypes.Role.DOCUMENT :
		return obj
	elif role == controlTypes.Role.EDITABLETEXT : # r smartReply key for quick filter bar :
		return None
	elif  role == controlTypes.Role.TABLEROW : 
		setState(obj, controlTypes.State.SELECTED, "Select")
		return obj
	elif role == controlTypes.Role.TREEVIEWITEM  :
		if gesture and  str(utis.getIA2Attribute	(obj.parent)) == "folderTree" :
			if hasattr(obj, "script_keyNav") :  obj.script_keyNav(gesture)
			return None
		setState(obj, controlTypes.State.SELECTED, "Select")
		if sharedVars.oSettings.getOption("chichi", "TTNoExpand") == False :
			setState(obj, controlTypes.State.EXPANDED, "Expand", action=1)
		return obj
	elif obj.role in (controlTypes.Role.UNKNOWN, controlTypes.Role.BUTTON) : #unknown ou button dans zone entêtes  
		o = obj
		while o :
			if o.role in (controlTypes.Role.FRAME, controlTypes.Role.PROPERTYPAGE) :  # role frame ou propertypage id=mailContent  ou 
				break
			o = o.parent
		if not o :
			message(_("Window not found"))
			return None
		if o.role == controlTypes.Role.PROPERTYPAGE : # cherche liste messages
			obj = utis.findChildByID(				o, "threadTree")
		elif o.role ==controlTypes.Role.FRAME  : # cherche role 115 id messagePane  puis 52 document
			# beep(440, 20)
			# alert(o)
			# return None
			# Chemin : role FRAME=34| i30, role-INTERNALFRAME=115, , IA2ID : messagepane | i0, role-DOCUMENT=52,  , 
			obj =  o.lastChild # status bar
			while obj :
				#alert(obj)
				if obj.role == controlTypes.Role.INTERNALFRAME :
					obj = obj.firstChild
					break
				obj = obj.previous
		obj.setFocus()
		# si branche réduite en mode conversation groupée
		if obj.role == controlTypes.Role.TREEVIEWITEM  and controlTypes.State.COLLAPSED in obj.states :
			#beep(150, 20)
			obj.doAction(1) # "expand")
		return obj

def openListAttachment (fo,gesture=None ):
	o  = fo
	# v3 : recherche  de l'objet mailContent (role 57) pour fenêtre princcipale et de role frame = 34      pour fenêtre séparée de lecture
	oID = False
	while o :
		r = o.role
		oID = utis.getIA2Attribute (o)
		#message ("OpenListAttachement ID : " + str(oID) + ", role : " + str(r))
		if oID == "mailContent" :  # fenêtre principale
			break
		elif r == 34 : # frame dans fenêtre séparée de lecture
			oID = "messengerWindow"
			break
		o=o.parent
	#if o :
		#message(u"Objet trouvé : " + str(oID) + ", role" + str(r))

	if not o: 
		message (_("No attachments available in this context."))
		return False
	isMsgWnd = (True if oID == "messengerWindow" else False)
	if not isMsgWnd : # fen principale
		if not utis.getExpandedHeadersFromFO(o) : return
	oPP = o # pour la suite
	#cherche les objets d'ID attachmentCount 
	x =(e for e in range (o.childCount, o.childCount-16,-1)) # -5,-1
	pj=False
	for e in x:
		#oTemp = o.getChild (e)
		#if sharedVars.debug : sharedVars.log(oTemp, "openListAttach : ")
		if utis.getIA2Attribute (o.getChild (e), "attachmentCount") :
			o = o.getChild(e)
			pj= True
			break
	if not pj:
		message (_("No Attachement."))
		return False
	# il y a 1 ou plusieurs  PJ
	st=o.name
	st = (_("One attachment.") if "1 " in st else st)
	message(st)
	if not gesture : # simple  frappe de alt+9
		return True
	# on doit activer le bouton toggle attachments si pas enfoncé
	o=o.previous.previous # bouton 
	if (controlTypes.State.PRESSED if hasattr(controlTypes, "State") else controlTypes.controlTypes.State.PRESSED) not in o.states:
		#message(u"bouton non enfoncé, on l'active")
		o.doAction() # place aussi le focus dans la liste
		return True
	else :
		while o and not o.role==14:  #list
			o=o.next
		o=o.firstChild 
		if (controlTypes.State.SELECTED if hasattr(controlTypes, "State") else controlTypes.controlTypes.State.SELECTED) not in o.states:
			o.doAction()
		o.setFocus()	
		message (o.name)
		return True

	# bouton déjà enfoncé, on doit trouver la liste des PJ
	o = oPP # property page ou frame
	x = (e for e in range (o.childCount, o.childCount-10,-1)) # -5,-1
	pj=False
	for e in x:
		if utis.getIA2Attribute (o.getChild (e), "attachmentList") : # "attachmentSize"): 
			#message (u"attachment_ trouvé")
			o =  o.getChild(e)
			pj=True
			break

	o.setFocus()
	return True

def gotoUnread(obj, gesture) :
	# goto  next unread message
	ttID = str(utis.getIA2Attribute (obj.parent) )
	# message ("ttID : " + ttID)
	if  ttID == "threadTree" : 
		if "alt" not in gesture.modifierNames : return KeyboardInputGesture.fromName ("n").send()
	else : return gesture.send() # not threadTree
	# threadTree et avec alt
	# trop tôt -> utis.setSpeech(False) # speech rétabli dans thunderbbird.appModule.event_gainFocus
	sharedVars.lockEditMenu = True
	CallLater(20, KeyboardInputGesture.fromName ("n").send) # envoie alt+n en réalité
	return

def getTreeID(fo) :
	if fo.role in (controlTypes.Role.TREEVIEWITEM , controlTypes.Role.TABLEROW) :
		ID = utis.getIA2Attribute(fo.parent)
		if ID : return str(ID)
	return ""

def smartReply(msgHeader, rc) :
	# beep(440, 20)
	fldLabel = _("To: ")
	#oField = utis.findChildByID(msgHeader, "expandedreply-toRow")
	# if not oField :
	oField = utis.findChildByID(msgHeader, "expandedtoRow")
	if not oField :
		message(_("No header") + fldLabel)
		return KeyboardInputGesture.fromName("control+r").send()
	# sharedVars.debugMess(oField, "SmartReply pour")
	# return
	oField, fldLabel, fldVal =  getRecip(oField)
	# message(str(fldLabel) +" " + str(fldVal))
	# return
	isList = (rc == 0 and utis.wordsMatchWord("@googlegroups|@framalist|@freelist", fldVal))
	if isList : 
		message(_("To the group, "))
		# display a menu -> return CallLater(150, replyTo, msgHeader, 1)
		#beep(100, 40)
		return CallLater(25, KeyboardInputGesture.fromName("control+shift+l").send)
	else :
		delay = 25
		if "groups.io" in fldVal :
			fldLabel = fldLabel.split(":")[0]
			if ";" not in str(fldVal) : message(_("To the list, "))
			else : 
				delay = 250
				message(fldLabel + "2 addresses") #  + fldVal)
			return CallLater(delay, KeyboardInputGesture.fromName("control+r").send)
		# not a list
		CallLater(delay, replyTo, msgHeader, 0)

def replyTo(msgHeader, recip) : # 0=correspondent 1=luist  
	# buttons to find
	# level5, 0 sur 1, role.TOOLBAR=35, IA2ID : header-view-toolbox Chemin : role FRAME=34| i46, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i7, role-LANDMARK = 149, , IA2ID : messageHeader | i0, role-SECTION=86, , IA2ID : headerSenderToolbarContainer | i0, role-TOOLBAR=35, , IA2ID : header-view-toolbox , IA2Attr : id : header-view-toolbox, display : flex, tag : div, class : header-buttons-container, xml-roles : toolbar, , Actions : click ancestor,  ;
	#Niveau 6,       0 sur 7, name : Répondre, role.BUTTON=9, IA2ID : hdrReplyToSenderButton Tag: toolbarbutton, états :  Chemin : role FRAME=34| i46, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i7, role-LANDMARK = 149, , IA2ID : messageHeader | i0, role-SECTION=86, , IA2ID : headerSenderToolbarContainer | i0, role-TOOLBAR=35, , IA2ID : header-view-toolbox | i0, role-BUTTON=9, , IA2ID : hdrReplyToSenderButton , IA2Attr : display : -moz-box, id : hdrReplyToSenderButton, setsize : 8, tag : toolbarbutton, posinset : 1, class : toolbarbutton-1 message-header-view-button hdrReplyToSenderButton, explicit-name : true, , Actions : press,  ;
	#Niveau 6,       1 sur 7, name : Répondre à la liste, role.BUTTON=9, IA2ID : hdrReplyListButton Tag: toolbarbutton, états : , childCount  : 1 Chemin : role FRAME=34| i46, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i7, role-LANDMARK = 149, , IA2ID : messageHeader | i0, role-SECTION=86, , IA2ID : headerSenderToolbarContainer | i0, role-TOOLBAR=35, , IA2ID : header-view-toolbox | i1, role-BUTTON=9, , IA2ID : hdrReplyListButton , IA2Attr : display : -moz-box, id : hdrReplyListButton, setsize : 8, tag : toolbarbutton, posinset : 2, class : toolbarbutton-1 message-header-view-button hdrReplyButton hdrReplyListButton, explicit-name : true, , Actions : press,  ;

	# path : i0, role-SECTION=86, , IA2ID : headerSenderToolbarContainer | i0, role-TOOLBAR=35, , IA2ID : header-view-toolbox , 
	o = msgHeader.firstChild.firstChild
	# OK sharedVars.debugMess(o, "barre outils ")

	if recip == 0 :  btnID = "hdrReplyToSenderButton"
	elif recip == 1 : btnID = "hdrReplyListButton"
	o = utis.findChildByID(o, btnID)
	#sharedVars.debugMess(o, " Button ")
	#return
	if o:
		# beep(440, 30)
		o.doAction()
		#CallAfter(KeyboardInputGesture.fromName("downArrow").send)
		#CallLater(00, o.doAction)
	else :
		gest = ("shift+control+l" if recip == 1 else "control+r") 
		CallAfter(KeyboardInputGesture.fromName(gest).send)


def getToolbarButtons() :
	# ble, role.BUTTON=9, IA2ID : hdrJunkButton Tag: toolbarbutton, états :  Chemin : role FRAME=34| i34, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i7, role-BUTTON=9, , IA2ID : hdrJunkButton , IA2Attr : tag : toolbarbutton, explicit-name : true, class : toolbarbutton-1 msgHeaderView-button hdrJunkButton, display : -moz-box, id : hdrJunkButton, setsize : 19, posinset : 8, , Actions : press,  ;
	o = utis.getPropertyPageFromFG()
	if not o : return beep(150, 20)
	o = o.firstChild
	while o and o.role != controlTypes.Role.BUTTON : o = o.next
	if not o : return beep(150, 20)
	# sharedVars.debugLog = ""
	while o and  o.role == controlTypes.Role.BUTTON :
		if sharedVars.debug : sharedVars.log(o, " Bouton barre outils : ", False)
		o = o.next
		
def getToolbarButtonByID(btnID) :
	# ble, role.BUTTON=9, IA2ID : hdrJunkButton Tag: toolbarbutton, états :  Chemin : role FRAME=34| i34, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i7, role-BUTTON=9, , IA2ID : hdrJunkButton , IA2Attr : tag : toolbarbutton, explicit-name : true, class : toolbarbutton-1 msgHeaderView-button hdrJunkButton, display : -moz-box, id : hdrJunkButton, setsize : 19, posinset : 8, , Actions : press,  ;
	o = utis.getPropertyPageFromFG()
	if not o : return beep(150, 20)
	o = o.firstChild
	while o and o.role != controlTypes.Role.BUTTON : o = o.next
	if not o : return beep(150, 20)
	# sharedVars.debugLog = ""
	while o and  o.role == controlTypes.Role.BUTTON :
		if sharedVars.debug : sharedVars.log(o, " Bouton barre outils : ", False)
		if str(utis.getIA2Attribute(o)) == btnID :
			return o
		o = o.next
	return None

def findChildByRoleID(obj,role,  ID) : # attention : valeurs role de controlTypes.py
	try : 
		prevLooping = sharedVars.objLooping
		sharedVars.objLooping = True
		o = obj.firstChild
		while o:
			if o.role == role :
				ia2ID = str(utis.getIA2Attribute(o))  # get_ia2Id(o)	
			if  ia2ID ==  ID:
				return o
			o= o.next
		return None	
	finally :
		sharedVars.objLooping = prevLooping

def setToStr(aSet, aLabel="", msgEmpty="") :
	if len(aSet) == 0 : return msgEmpty
	result = ""
	for e  in aSet :
		result += str(e) + ", " 
	return aLabel + " : " + result[:-2]

def chichiLinks(rc) :
	CallLater(20, utis.sendKey, "space", rc, 0.02)
	CallLater(100, speech.cancelSpeech) # message, "Liste de liens : ")
	return

def readPreview2(oRow, gesture) :
	# sharedVars.log(oRow, "readPreview2,oRow properties")
	if sharedVars.TTnoSpace and gesture.mainKeyName == "space" :
		# message("Lecture avec Chichi")
		CallAfter(gesture.send)
		return

	rev = False  # reverse 
	spkMode = 1 # speak only
	if    gesture.mainKeyName == "downArrow" and("shift" in gesture.modifierNames) :
		spkMode = 2 # copyToClip + speak
	elif   gesture.mainKeyName == "upArrow" or("shift" in gesture.modifierNames) :
		rev = True
	if  controlTypes.State.SELECTED not in oRow.states :
		# message(u"Ligne non sélectionnée. Veuillez réitérer votre commande.")
		beep(80, 30)
		# # on sélectionne le message avec control+espace
		KeyboardInputGesture.fromName ("control+space").send ()
		api.processPendingEvents()
		return readPreview2(oRow, gesture)
	# recherche de l'objet document 
	# Chemin : role FRAME=34| i37, role-GROUPING=56, , IA2ID : tabpanelcontainer | i0, role-PROPERTYPAGE=57, , IA2ID : mailContent | i14, role-INTERNALFRAME=115, , IA2ID : messagepane | i0, role-DOCUMENT=52,  , 
	o = oRow
	while o and not o.role==controlTypes.Role.PROPERTYPAGE :  #ROLE_PROPERTYPAGE
		o=o.parent
	o=o.lastChild
	while o :
		role =o.role 
		if role  ==controlTypes.Role.INTERNALFRAME  : break 
		elif role == controlTypes.Role.EDITABLETEXT: o=False
		else : o=o.previous
	if not o : 
		if getTreeID(ORow)  == "threadTree": return message(_("The headers and message pane is not displayed. Please press F8 then try again."))
		else : return message (_("The body of the message is missing."))
	#memLog.addprops(o, u"Recherche section")
	o = o.firstChild
	if not sharedVars.oQuoteNav : sharedVars.initQuoteNav() # then use  sharedVars.oQuoteNav.*		self.regExp_date =compile ("^(\d\d/\d\d/\d{4} \d\d:\d\d|\d\d:\d\d)$")
	sharedVars.oQuoteNav.readMail(o, rev, spkMode)
