#-*- coding:utf-8 -*
# Thunderbird+ v 4.x
# Reads the cells in a row of the message list
#  overrlay class

import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
from scriptHandler import  getLastScriptRepeatCount
from NVDAObjects.IAccessible import IAccessible
from ui import message
from speech import speakSpelling
from wx import CallLater
import api
from time import time
import addonHandler,  os, sys
addonHandler.initTranslation()
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import utis, sharedVars
import py3compatibility
from  py3compatibility import _unicode, u
del sys.path[-1]
import globalVars


class MessageListItemFields(IAccessible):
	fields = "threadCol, statusCol, attachmentCol, subjectCol, correspondentCol, dateCol, sizeCol, junkStatusCol, tagsCol, senderCol, recipientCol, receivedCol, priorityCol, flaggedCol, unreadButtonColHeader, accountCol, unreadCol, totalCol, locationCol, idCol".split(", ")  #nouvel ordre
	champs = ["Discussion", "statut", "Pièces jointes", "Sujet", "Correspondants", "Date", "Taille", "Statut indésirable", "Étiquettes", "Expéditeur", "Destinataire", "Reçu", "Priorité", "Suivi", "unreadButtonColHeader", "Compte", "Non lus", "Total", "Emplacement", "idCol"]
	notField = "Aucun champ texte"
	lastScriptKeyName=""
	chrono = False

	def initOverlayClass (self): 
		k=("1","2","3","4","5","6","7","8","9","0")  #,")","=" pb si double frappe?
		for e in k:self.bindGesture ("kb:"+_unicode (e),"readField")  		

	def getLabelMailAddress (self,s):
		return s 

	def columnID (self) :
		obj=api.getForegroundObject()
		obj= utis.findChildByID(obj,"tabpanelcontainer").firstChild 
		obj= utis.findChildByID(obj,"threadTree").firstChild 
		cols=[]
		for e in range (obj.childCount-1) :
			if obj.getChild(e) : 
				o=obj.getChild(e)
				if int(o.location[2])>0 :cols.append ((int(o.location[0]),utis.getIA2Attribute (o)))  
			else : return
		cols.sort ()
		cols=[e[1] for e in cols]	
		return cols	

	def readField_default  (self, currentScriptKeyName, keyRepeat):
		index =int (currentScriptKeyName[-1])  #+(9 if  currentScriptKeyName[0].isalpha () else 0)
		if index > len (self.appModule.columnID) : return message (self.notField)
		o =self.getChild (index-1);name, columnText  =o.name, o.columnHeaderText
		if not keyRepeat : 
			#return speak ("{columnText}  {name}".format (columnText = columnText, name =name), symbolLevel =0)
			# version braille
			return message ("{columnText}  {name}".format (columnText = columnText, name =name))
		speak (_("{columnText} copié dans le presse papier").format (columnText =columnText), symbolLevel =0)
		api.copyToClip (""+name)

	def script_readField(self,gesture):
		index, cols, i, currentScriptKeyName, lastScriptRepeatCount = int (gesture.mainKeyName), self.appModule.columnID, -1, gesture.displayName, getLastScriptRepeatCount () 
		# index, cols, i, options, currentScriptKeyName, lastScriptRepeatCount = int (gesture.mainKeyName), self.columnID(), -1, self.appModule.options["messengerWindow"], gesture.displayName, getLastScriptRepeatCount () 
		# if not self.appModule.date_firstMessage :self.appModule.date_firstMessage ="oui"
		if index ==0:index=10
		if index >len (cols):return  message (_("Pas de colonne de rang %s") %(index)) 
		elif not cols :return message (_("aucun en tête "))
		if not cols[0] in self.fields : return self.readField_default (currentScriptKeyName, lastScriptRepeatCount ) 
		if not cols[1] in self.fields : return self.readField_default (currentScriptKeyName, lastScriptRepeatCount )
		e0=0
		for e in range (len (self.fields)):
			if self.fields[e] in cols :
				i+=1
				if i == index-1: e0=e ; break
		field= self.fields[e0]
		champ= self.champs[e0]
		indix =  cols.index (field)
		self.lastCellCalledAndTime =[index,time (),field]
		o = self.getChild (indix)
		if not o :return message (_("Le champ %s n'est pas disponible ") %champ)
		value, columnHeaderText, columnHeaderText_original, add_doublePoint  =o.name, o.columnHeaderText,o.columnHeaderText, " : "
		if value in self.appModule.columnID : value =""
		# if value in self.columnID(): value =""
		api.copyToClip(str(field))
		#if  field =="subjectCol": value = (value [1:-1] if value.startswith ("[") and value.endswith ("]") or value.startswith ("{") and value.endswith ("}") else value )
		if field   == "subjectCol" :
			# listgroup name
			grp = utis.strBetween(value, u"[", u"]")
			# api.copyToClip("groupe " + grp)
			if grp :
				value = self.appModule.regExp_nameListGroup.sub (" ",value)
				value =  grp + " : " +  value 
			# beep(300, 20)
			# grp =self.appModule.regExp_nameListGroup.match(value)
			# api.copyToClip(str(grp))
			# if sharedVars.oSettings.getOption("messengerWindow", "listGroupName") :
				# value =self.appModule.regExp_nameListGroup.sub (" ",value)

		# if field in  "correspondentCol,recipientCol,subjectCol, senderCol" and sharedVars.oSettings.getOption("messengerWindow", "listGroupName") :
			# value =self.appModule.regExp_nameListGroup.sub (" ",value)

		# v3 plus utile TB91if field in ("correspondentCol","senderCol","recipientCol")  and options.as_bool ("mailAddress") :  value =self.getLabelMailAddress (value)
		if field == "subjectCol" : 
			value = self.appModule.regExp_AnnotationResponse.sub (" ",value)
		if field in ("receivedCol","dateCol") : value = utis.formatDateTime(value)  
		if field =="threadCol":
			value = _(u"Les fil de discussion sont {state}").format (state = (u"Affichée",u"Masquée")[self.role == controlTypes.Role.TABLEROW])
			columnHeaderText, add_doublePoint ="",""
		elif field =="junkStatusCol":value ={"0":"acceptable","100":u"indésirable"}.get (value, "acceptable ");columnHeaderText="status "
		elif field == "statusCol" and value =="":
			value ="Non lu"
		elif field == "flaggedCol" and value :
			value ="oui"			
		elif field =="unreadCol" :value =("non","oui")[bool (value)]
		elif field =="unreadButtonColHeader" : 
			value = "message "+{False : columnHeaderText}.get (bool (value),value)
			add_doublePoint, columnHeaderText=""," "
		elif  field  =="attachmentCol"  and value: 
				return self.attachments(value, lastScriptRepeatCount)
		elif value in ("priorityCol","subjectCol") :value =""
		if value :
			s =u"{columnHeaderText} {value}".format (columnHeaderText = columnHeaderText, value= value)
		else:
			s= _("Pas de {columnHeaderText}").format (columnHeaderText= columnHeaderText)
		o= self
		while o and not "id" in o.IA2Attributes.keys () :o=o.container
		o=o.firstChild.getChild (index)
		value =value.strip ()
		#action
		o =self
		while o and not utis.getIA2Attribute (o): o = o.container
		x=(e for e in o.firstChild.children)
		for o in x :
			if utis.getIA2Attribute (o,field) :break
		self.lastCellCalledAndTime.append (o)
		lastScriptRepeatCount = (lastScriptRepeatCount  if  lastScriptRepeatCount and self.lastScriptKeyName == currentScriptKeyName else 0)
		self.lastScriptKeyName = currentScriptKeyName
		if not lastScriptRepeatCount : 
			# return speak  ([s], symbolLevel =0)
			# version braille
			return message (s)
		if  self.chrono :self.chrono.Stop ()
		self.chrono =CallLater (150,self.copyOrSpell, columnHeaderText_original,value, lastScriptRepeatCount )
	script_readField.__doc__ = _("Lire les entêtes des colonnes dans la fenêtre principale")
	script_readField.category=sharedVars.scriptCategory

	def copyOrSpell (self,columnHeaderText_original , value, lastScriptRepeatCount ):
		if lastScriptRepeatCount ==1 :speakSpelling (value)
		else:
			if api.copyToClip  (_unicode (value)): 
				message (_("%s copié dans le presse papier ") % columnHeaderText_original)
			else:
				message (_("le champ %s n'a pas pu être copié dans le presse papier ") % columnHeaderText_original)

	def attachments (self, value, repeats):
		if utis.getMessageHeadersFromFG(False) :
			utis.openListAttachment2(self, repeats)
		else :
			message(value)
