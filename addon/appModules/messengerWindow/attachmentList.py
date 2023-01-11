# coding :utf-8
# Thunderbird+ 4.x

from keyboardHandler import KeyboardInputGesture
from NVDAObjects.IAccessible import IAccessible
from ui import message
from wx import CallAfter
from tones import beep
import addonHandler
addonHandler.initTranslation()


class AttachmentList (IAccessible):
	def initOverlayClass (self): 
		self.bindGestures({"kb:escape":"escape", "kb:alt+1":"readAttachField", "kb:alt+2":"readAttachField"})

	def  _get_description (self):
		return ""

	def scr_shiftTab (self,gesture): 
		#gesture.fromName ("shift+f6").send ()
		#beep (300, 100)
		if not self.appModule.restoreFocus () :
			gesture.send ()

	def script_escape (self,gesture): 
		self.sendShiftF6(gesture)

	def sendShiftF6 (self,gesture):
		gesture.fromName ("shift+f6").send ()

	def scr_tab (self, gesture):
		# provisoirement comme shift Tab
		if not self.appModule.restoreFocus () :
			gesture.send()

	def scri_testObj (self, gesture) :
		# script désactivé par son nom modifié en scri_
		""" o = self
		i = 1
		while o :
			oID = getIA2Attr  (o)
			message (str(i) + ": script tab oID : " + str(oID) + ", role : " + str(o.role))
			i += 1
			o = o.parent """
		ogp = self.parent.parent
		oID = getIA2Attr  (ogp)
		#message ("cetest ogp : " + str(oID) + ", role : " + str(ogp.role))
		message (_("Objets précédents"))
		o = self.parent
		i = 0
		while o :
			oID = getIA2Attr  (o)
			#message (str(i) + ":oID : " + str(oID) + ", role : " + str(o.role) + ", childCount : "+ str(o.childCount))
			i -= 1
			o = o.previous

	def script_readAttachField (self, gesture):
		if gesture.mainKeyName in  ("1", "2") :
			message (self.getChild (int (gesture.mainKeyName)).name)

	# __gestures={ "kb:escape":"escape",
# "kb:alt+1":"readAttachField",
# "kb:alt+2":"readAttachField",
# }
