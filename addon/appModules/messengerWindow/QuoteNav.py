#-*- coding:utf-8 -*
from . import sharedVars
import speech

oQuoteNav = None

class QuoteNav() :
	text =""
	index =  lastIndex = 0

	def __init__(self) :
		# Translators : do not translate nor remove %date_sender%. Replace french words, word 2 and word 5, by your translations. 
		# The ¨ char is a temporary replacement of \n
		lbls = _("On|Le%date_sender%wrote|écrit")
		lbls = lbls.split("%date_sender%")
s = "(( |¨){1,}(" + lbls[0] + ") .* (" + lbls[1] + ")(:| :))"
# compilation
self.regStdHdr = re.compile(s)

		# lbls = lbls.replace("%date_sender%", "|")
		# sharedVars.tlog("mlbls sgStr:" + lbls)
		# lbls =  lbls.split("|")
		# if len(lbls) < 4 : return
		# sharedVars.tlog("splitted lbls:" + str(lbls))
			# # string to get : lblOn = "¨ On | On |¨ Le | Le "
		# self.lblOn = "¨ {0} | {0} |¨ {1} | {1} ".format(lbls[0], lbls[1])
		
		# # string to get  : 	lblWrote = " wrote :¨| wrote:¨| écrit :¨| écrit:¨" 
		# self.lblWrote = " {0} :¨| {0}:¨| {1} :¨| {1}:¨".format(lbls[2], lbls[3])
	# sharedVars.tlog("iniGVars, lblOn {}, lblWrote {}".format(lblOn, lblWrote))


	def setText(self, msg, endSubj) : 
		self.text = msg
		self.endSubj = endSubj
		# ===
		self.deleteBlocks()
		# return  self.sayText(200)
		# self.text=self.text.replace ("&nbsp;", " ") # .replace("<br>\n", u"àbr") # .replace("&lt;", "<") # .replace ("</span","") # .replace ("&lt;","<").replace ("&gt;",">")
		self.text = self.text.replace("\n", "¨")
		# return  self.sayText(200)

		# removes special &char;
		reg = re.compile("(&nbsp;|&gt;)") 
		self.text=reg.sub(" ",self.text)
		# return  sayText(200)
		self.cleanLinks()
		# Removes of all remaining HTML tags
		reg= re.compile ("<.+?>")
		self.text=reg.sub("",self.text)
			# removes multiple spaces 
		reg = re.compile(" {2,}")
		self.text=reg.sub(" ",self.text)
			# removes multiple pseudo \n ¨
		reg = re.compile("¨{2,}")
		self.text=reg.sub("¨",self.text)

		# return  self.sayText(200)
		self.cleanStdHeaders()
		self.cleanMSHeaders(endSubj)
		# removes multiple  spaces
		reg = re.compile(" { 2,}")
		self.text = reg.sub(" ", self.text)
		# removes multiple " ¨"
		reg = re.compile("( ¨){3,}")
		self.text = reg.sub("", self.text)

		# if reverse :
		self.Quotes = self.text.split("\n")
		self.quotes.reverse()
		self.lastIndex = len(self.quotes)
		self.text = self.text.replace("¨", "\n")
		
	def sayText(self, freq=440) :
		if freq > 0 :
			beep(freq, 40)
		api.copyToClip(self.text)
		speech.speakText(self.text)

	def deleteMetas() :
		lbl = "<meta "
		metas = []
		p, pEnd = findWords(lbl)
		while p > -1 :
			p2 = self.text.find('">', pEnd) 
			if p2 == -1 : break
			b = self.text[p:p2] + '">'
			# sharedVars.tlog("meta:" + b)
			metas.append(b)
			# next block
			p, pEnd = findWords(lbl, p2+2) # +2 is then len of ">
		if len(metas) == 0 : return
		for e in metas :
			# sharedVars.tlog("e:" + e)
			self.text = self.text.replace(e, "")

	def deleteBlocks() :
		# Originale message
		s = _("Original Message|E-mail d'origine|Message d'origine")
		reg = re.compile("(\-{5} ?(" + s + ") ?\-{5})")
		self.text = reg.sub("", self.text)

			# begin code to debug :  and clean
		# Removes meta tag
		# if self.text.find("<meta name") > -1 :
			# beep(100, 50)
			# result = re.findall('(startself.text)(.+)((?:\n.+)+)(endself.text)',input)
			# reg = re.compile("<meta name.+>")
			# reg = re.compile("(<meta name(.+|\s+))")
			# self.text = reg.sub("", self.text)
			# l = reg.findall(self.text)
			# l = re.findall('(<meta)(.+)((?:\n.+)+)(">)', self.text)
			# if len(l) > 0 :
				# for e in l :
					# sharedVars.tlog("meta:" + str(e))
		# end code to debug
		self.deleteMetas()
		#Removes   de google groupe  footer
		s = _("You are receiving this message because you are subscribed to the group") #  Google")
		i =self.text.find (s)
		# api.copyToClip (u"Avant suppr google groups\nposition=" + str(i) + "\n" + self.text)
		if i !=-1 :self.text=self.text[:i]

		#Removes groups.io footer
		pos, pos2 = findWords("Groups.ioLinks|Groups.io Links")
		if pos > -1 :
			pos = self.text.find("-=-=")
			if pos != -1 :
				self.text=self.text[:pos]
		# suppression style CSS
		if self.text.find("<style>") > 0 :
			regExp = re.compile ("\<style\>.+?\</style\>")
			self.text=regExp.sub (" ",self.text)

	def cleanLinks() :
		# mailto and clickable links replacements
		regExp = re.compile ("(\<a .+?\>(.+?)\</a\>)")
		lbl = _(" link %s ").replace(" %s", "")
		l=regExp.findall (self.text)
		for e in l :
			self.text_link = e[1]
			# sharedVars.tlog( "e: " + str(e))
			# sharedVars.tlog( "self.text_link " + str(self.text_link))
			if "mailto" in e[0]:
				self.text = self.text.replace(e[0], self.text_link + ":")
			elif self.text_link.startswith ("http") :
				self.text = self.text.replace (e[0], shortenUrl(self.text_link, lbl))

	def cleanStdHeaders() :
		# Compress standard "On date sender wrot :
		# 1. findAll blocks of headers
		headers = self.regStdHdr.findall(self.text)
		if len(headers) == 0 : return
		for e in headers :
			el = e.split(",")
			if len (el)  < 2 : el = e
			else :
				el = el[1]

			# removes pseudo \n ¨
			el = el.replace("¨", " ")
			# removes  multiple spaces
			reg = re.compile(" {2,}")
			el = reg.sub(" ", el)
			sharedVars.tlog("el:" + el)
			try :.
				self.text = self.text.replace(e, "\n---" + el)
			except :
				beep(100, 30)
				pass
			try :
				print("self.text=" + self.text) 
			except :
				beep(120, 30)
		
	def cleanMSHeaders(endSubj) :
		global self.text
		# Reduction of WinMail and OE headers liene 
		# 1. findAll blocks of headers
		lenSubj = len(endSubj)
		blocks = []
		lbls = _("From|De|Expéditeur") + "|"
		a = lbls.split("|")
		lbls = ""
		for lbl in a :
			if lbl == "" : break
			lbls += lbl + ":|" + lbl + " :|"
		lbls = lbls[:-1]
		# sharedVars.tlog("from labels:" + lbls)

		p, pEnd = findWords(lbls)
		while p > -1 :
			p2 = self.text.find(endSubj, pEnd) 
			if p2 == -1 : break
			b = self.text[p:p2] + endSubj
			# sharedVars.tlog("MS header:" + b)
			blocks.append(b)
			# next block
			p, pEnd = findWords(lbls, p2+lenSubj)
		if len(blocks) == 0 : return

		for e in blocks :
			sharedVars.tlog("to replace:" + e)
			# e may contain ¨, a pseudo \n 
			t = "\n---" + getSenderName(e) + " " +   _("wrote")+ " : "
			sharedVars.tlog("t:" + t)
			self.text = self.text.replace(e, t)
			
		return
			# if utis.wordsMatchWord(search, e[0]) :
				# arr = str(e[0]).split(":")
				# if len(arr) > 2 :
					# repl = "--- " + getSenderName(arr[1]) + " " + _("wrote") + " :¨"
					# sharedVars.tlog( "replacement : " + repl)

	def strBetween2(sep1, sep2) :
		pos1 = self.text.find(sep1) 
		if pos1 < 0 : return ""
		pos1 +=  len(sep1)
		pos2 = txt.find(sep2, pos1)
		if  pos2 < 0 : return ""
		return self.text[pos1:pos2]

	def findWords(words, start=0) :
		lWords = words.split("|")
		for e in lWords :
			pos = self.text.find(e, start)
			if pos > -1 :
				return pos, pos + len(e) + 1
		return pos, pos
		

	def getSenderName(header) :
		#  header may contain ¨
		

		# On Behalf Of Isabelle Delarue via groups.ioSent 
		if "Behalf Of" in header :
			s = strBetween(header, "Behalf Of", "via groups").strip()  
		elif  "via groups.io" in header : 
			# to replace:From: ¨  Jeremy T. via groups.io: 
			s = strBetween(header, ":", "via")
		else :
			# s = "à revoir : " + header
			header  = header.split(":") 
			s = (header[1] if len(header) > 1 else header[0])
			if "&lt;" in s :
				s = s.split("&lt;")[0]

		s = s.replace("¨", " ").strip()
		sharedVars.tlog("retour getSenderName :" + s)
		return s
	# methods related to quotes
		skip(self, n)
	first
	last
	
# normal functions
def getSenderName(header) :
	#  header may contain ¨
	

	# On Behalf Of Isabelle Delarue via groups.ioSent 
	if "Behalf Of" in header :
		s = strBetween(header, "Behalf Of", "via groups").strip()  
	elif  "via groups.io" in header : 
		# to replace:From: ¨  Jeremy T. via groups.io: 
		s = strBetween(header, ":", "via")
	else :
		# s = "à revoir : " + header
		header  = header.split(":") 
		s = (header[1] if len(header) > 1 else header[0])
		if "&lt;" in s :
			s = s.split("&lt;")[0]

	s = s.replace("¨", " ").strip()
	sharedVars.tlog("retour getSenderName :" + s)
	return s
	
def shortenUrl(lnk, label) :
	lnk = lnk.replace("https://", label)
	lnk = lnk.replace("http://", label)
	return lnk.split("/")[0]
	
