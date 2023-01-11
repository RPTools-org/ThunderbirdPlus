#-*- coding:utf-8 *-

from  py3compatibility import _unicode
from comtypes.gen.ISimpleDOM import ISimpleDOMNode
from NVDAObjects.IAccessible import IAccessible
import controlTypes
if not hasattr(controlTypes, "Role"):
	from controlTypes import ROLE_INTERNALFRAME, ROLE_EDITABLETEXT, ROLE_ALERT
else:
	ROLE_INTERNALFRAME = controlTypes.Role.INTERNALFRAME
	ROLE_EDITABLETEXT = controlTypes.Role.EDITABLETEXT
	ROLE_ALERT = controlTypes.Role.ALERT
from scriptHandler import getLastScriptRepeatCount
from ui import message
from speech import speak
from time import time
from UIAHandler import handler, UIA_ControlTypePropertyId ,UIA_EditControlTypeId ,UIA_CustomControlTypeId,TreeScope_Descendants,UIA_DocumentControlTypeId 
clientObject =handler.clientObject
CPC=clientObject.CreatePropertyCondition
from threading import Thread
from wx import CallLater
from tones import beep
import addonHandler,  os, sys , api
from keyboardHandler import KeyboardInputGesture
addonHandler.initTranslation()
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import utis, sharedVars
del sys.path[-1]
from . import contentMailRead
_timer = None


class Document (IAccessible):
	def initOverlayClass (self):
		#for e in  range(1,9): self.bindGestures ({"kb:alt+"+_unicode(e):"readOtherField"}) 		
		self.bindGesture ("kb:space", "readDocument")
		self.bindGesture ("kb:shift+space", "readDocument")
		self.bindGesture ("kb:f4", "readDocument") 
		self.bindGesture ("kb:shift+f4", "readDocument") 

	def script_readDocument (self, gesture) :
		filt = True
		if 		getLastScriptRepeatCount()>0 :
			filt = False
		rev = False  # reverse 
		if  "up" in gesture.mainKeyName or("shift" in gesture.modifierNames) :
			rev = True
		if rev and not filt :
			message(_("La lecture non filtrée en sens inverse n'est pas disponible."))
			return
		contentMailRead.readContentMail(self, rev, filt)
	script_readDocument.__doc__ = _("Lecture filtrée du document")
	script_readDocument.category = sharedVars.scriptCategory

	def script_readOtherField (self,gesture, oFocus=None):
		global _timer
		beep(440, 20)
		repeats = getLastScriptRepeatCount ()
		if _timer is not None:
			_timer.Stop()
			_timer = None
		if repeats in (0, 2) : delay = 5 # annonce entête ou ouverture menu contextuel de la zone des entêtes
		elif repeats == 1 : delay = 300 # affichage dialogue Copier dans le presse-papiers
		message(_("Read other fields depuis document"))
		#_timer = CallLater(delay, readHeaders, oFocus, expHeaders, int(gesture.mainKeyName), repeats, delay) # key, repeatCount, delay
	script_readOtherField.__doc__ = _("Lire différents entêtes d'un message.")
	script_readOtherField.category = sharedVars.scriptCategory

def readDoc(oDoc, title="") :
	# return message(str(oDoc))
	contentMailRead.readContentMail(oDoc, False, True, title)



