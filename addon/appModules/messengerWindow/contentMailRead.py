 #-*- coding:utf-8 -*

from time import sleep
from wx import CallLater
import speech, winUser
import characterProcessing
if not hasattr(characterProcessing, "SYMLVL_SOME"):
	SYMLVL_SOME = characterProcessing.SymbolLevel.SOME
else:
	from characterProcessing import SYMLVL_SOME

from comtypes.gen.ISimpleDOM import ISimpleDOMNode
from NVDAObjects.IAccessible import IAccessible
import controlTypes
if not hasattr(controlTypes, "Role"):
	from controlTypes import ROLE_INTERNALFRAME, ROLE_EDITABLETEXT, ROLE_ALERT, STATE_SELECTED
else:
	ROLE_INTERNALFRAME = controlTypes.Role.INTERNALFRAME
	ROLE_EDITABLETEXT = controlTypes.Role.EDITABLETEXT
	ROLE_ALERT = controlTypes.Role.ALERT
	import controlTypes
if not hasattr(controlTypes, "Role"):
	from controlTypes import ROLE_INTERNALFRAME, ROLE_EDITABLETEXT, ROLE_ALERT, STATE_SELECTED
else:
	ROLE_INTERNALFRAME = controlTypes.Role.INTERNALFRAME
	ROLE_EDITABLETEXT = controlTypes.Role.EDITABLETEXT
	ROLE_ALERT = controlTypes.Role.ALERT
	STATE_SELECTED = controlTypes.State.SELECTED
from scriptHandler import getLastScriptRepeatCount
from ui import message
from tones import beep
import controlTypes
import addonHandler,  os, sys , api
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import translation, utis, sharedVars
# import zDevTools as z
del sys.path[-1]
translation.initTranslationWithEnglishFallback()

import re # regex

def readContentMail(oDoc, reverse=False, filter = True, title=""): 
	# return message(title)
	if not oDoc : return # message(u"Veuillez réitérer votre commande de lecture.")
	o= oDoc # .firstChild # du document 
	if title :
		subjLastWord =  title.split(" - Mozilla ")[0]
		subjLastWord =subjLastWord.strip ().split (" ")[-1]
	elif hasattr(oDoc, "name") : 
		subjLastWord =oDoc.name.strip ().split (" ")[-1]
	else :
		subjLastWord =oDoc.IAccessibleObject.accName(0).strip ().split (" ")[-1]
	#message ("avant o.firstChild " + str(o.role) + ", " + str(o.name)) # doit être document
	o=o.firstChild # section ou paragraph
	# message ("après  o.firstChild " + str(o.role)  + ", " + str(o.name))
	if not o : return message(_("erreur"))
	cCount = oDoc.childCount
	text = title
	# text += "\pchildCount : " + str(cCount) + "\n"

	if o.next :
		#o=o.next
		i = 1
		if cCount > 100 : message(str(cCount) + " objects. Press Control to stop.")
		#html simple
		while o :
			try : 
				obj = o.IAccessibleObject.QueryInterface(ISimpleDOMNode)
				s=obj.innerHTML
				if not s :s=o.name
			except :
				s = "error"
				pass
				
			if s :text+=s
			if winUser.getKeyState(winUser.VK_CONTROL)&32768:
				beep(100, 30)
				# CallLater(200, message, text)
				CallLater(200, filterSpeakDoc, 		subjLastWord, text, reverse, filter)
				return

			i += 1
			if cCount > 100 :
				perc = (i / cCount) * 100
				if perc % 10 == 0 :
					if perc == 50.0 : beep(350, 20)
					else : beep(350, 2) # message(str(int(perc)) + "%")
			try : o=o.next
			except : break # fix v 3.4.1
	else: # texte brut
		# beep(500, 30)
		o = o.IAccessibleObject.QueryInterface(ISimpleDOMNode)
		#text= unicode (o.innerHTML) if sys.version_info.major == 2 else str (o.innerHTML)
		text += str(o.innerHTML)
	# api.copyToClip (text)
	# message("texte dans le presse-papiers")
	filterSpeakDoc (		subjLastWord, text, reverse, filter)
def shortenUrl(lnk, label) :
	lnk = lnk.replace("https://", label)
	lnk = lnk.replace("http://", label)
	return lnk.split("/")[0]
	

def filterSpeakDoc(endSubj, text, reverse, filter) :
	# beep(700, 30)
	# api.copyToClip (u"endSubj [" + endSubj + "] text=" + text)

	if not filter :
		message(_("Lecture non filtrée."))
	#suppression du pied  de google groupe 
	s = _(u"Vous recevez ce message, car vous êtes abonné au groupe") #  Google")
	i =text.find (s)
	# api.copyToClip (u"Avant suppr google groups\nposition=" + str(i) + "\n" + text)
	if i !=-1 :text=text[:i]

	#suppression du pied de groups.io
	if text.find(_("Groups.io Links")) > 0 :
		i = text.find("-=-=-")
		if i !=-1 :text=text[:i]
		# remplacement temporaire  des \n
	text=text.replace ("\n",u"àn")
	# suppression style CSS
	if text.find("<style>") > 0 :
		regExp = re.compile ("\<style\>.+?\</style\>")
		text=regExp.sub (" ",text)

	# remplacement de la balise lien (<a...</>
	regExp = re.compile ("(\<a .+?\>(.+?)\</a\>)")
	lbl = _(" lien %s ").replace(" %s", "")

	# 2023-05-29 : added call to shortenUrl()
	l=regExp.findall (text)
	for e in l :
		text_link = e[1]
		if "mailto" in e[0]: continue
		elif text_link.startswith ("http") :
			text = text.replace (e[0], shortenUrl(text_link, lbl))
		# else :
			# text =text.replace (e[0],_(u" lien %s ") % text_link)
		
	#remplacement des objets youtube par du texte  (dans le flus rss)
	reg = re.compile ("\<iframe.+?\</iframe\>")
	text =reg.sub (_(u"objet youtube présent. "),text)
	#suppression du titre dans les flus rss
	reg = re.compile ("\<title\>.+?\</title\>")
	text=reg.sub (" ",text)
	# #suppression de fin de message yahoo
	# reg = re.compile ("\-{36}")
	# if reg.search (text):text =text[:text.find ("-"*36)]
	# s="    <!--~-|**|PrettyHtmlStart|**|-~-->"
	# i=text.find (s)
	# if i!=-1:text=text[:i]
	# suppression caractères entre & et point-virgule
	text=text.replace ("\n"," ").replace ("&nbsp;","").replace ("&lt;","<").replace ("&gt;",">")
	# suppression  des <balise> restantes, par exemple <br> ou <br />
	reg= re.compile ("\<.+?>")
	text=reg.sub ("<",text)
	# suppression
	# reg= re.compile ("([\<\> ][\>\< ])+")
	# text =reg.sub (" ",text)
	# suppression  de ?
	# reg = re.compile (" *: *")
	# text =reg.sub (":",text)
	if not filter :
		text=text.replace (u"àn","\n")
		speech.speak ([text], symbolLevel=SYMLVL_SOME)
		return
	from re import escape

	text =text.replace ("mailto:","")
	reg = re.compile (_("(\s+|\-{5} ?(E-mail d'origine|Message d'origine|Original Message) ?\-{5})"))
	text =reg.sub (" ",text)
	reg = re.compile(_("((((From|De|Expéditeur):.+?(Sujet|Subject|Objet):.+?%s)))") % escape (endSubj))
	l=reg.findall (text)
	for e in  l:
		e= e[0]
		x=e.split (":")[1]
		arobase =x.find ("@")
		if arobase !=-1:x=x[:arobase]
		x=x.replace ("'","").replace ("\"","")
		if x.count (" "):x=x[:x.rfind (" ")]
		text=text.replace (e, _("\n. %s a écrit . ") % x)
	#suppression date 
	#pour le confort 
	text =text.replace ("<","")
	#autre champ du style le ... a écrit ...
	s= _(">> > C'aurait été con. >> > >> > J.-F. >> > >> >")
	#if text.count (s):text=text[text.find (s)+len (s):]
	reg = re.compile (_("((\s*(Dans un e\-mail daté du|Le) (\d\d[\-/]\d\d[\-/ ]|\d\d .+? )\d{2,4}( (. )?\d\d:\d\d(:\d\d .+?, .+?)?)?,\s*(.+?)a écrit:))"))
	l=reg.findall (text)
	for e in l :
		x=e[7]
		if x.count ("@"):
			x=x.split("@")[0]
			i=x.rfind (" ")
			if i !=-1:x=x[:i]
			text=text.replace (e[0],_("\n. %s a écrit. ") % x)
		else:
			text =text.replace (e[0],_("\n. %s a écrit.") % x)
	text=text.strip ()
	#modification de lien  non cliquables
	reg = re.compile ("https?://.+?\s?.+?\s")
	l=reg.findall (text)
	for e in l : 
		text =text.replace (e, shortenUrl(e, " URL "))
	if reverse :
		text=text.split ("\n")
		text.reverse ()
		text =("\n").join (text)
	#vérifie si le texte est vide 
	reg = re.compile ("\S")
	if not reg.search (text):text = _("pas de texte ")
	text=text.replace (u"àn","\n")
	# api.copyToClip (u"endSubj [" + endSubj + "] text=" + text)
	message(text)
	# speech.speak  ([text], symbolLevel=SYMLVL_SOME)
