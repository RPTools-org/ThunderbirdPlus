#-*- coding:utf-8 -*

import api, config, sys, glob, shutil
from configobj import ConfigObj
import re
import addonHandler,  os, sys
import translation, sharedVars, utis
from wx import Menu, EVT_MENU, CallAfter, CallLater 
from ui import  message
from speech import cancelSpeech
from tones import beep
translation.initTranslationWithEnglishFallback()


class  Settings() :
	def __init__(self, fromClass) :
		# fromClass doit être une référence sur la classe AppModule ou GlobalPlugin 
		self.refClass  = fromClass
		self.options = self.option_messengerWindow = self.option_msgcomposeWindow = self.option_startup = self.option_chichi = None
		self.regex_removeInSubject = None
		curAddon=addonHandler.getCodeAddon()
		self.addonName =  curAddon.name
		self.iniFile = api.config.getUserDefaultConfigPath()+"\\" + self.addonName + ".ini"
		if sharedVars.debug : sharedVars.log(None, "IniFile : " + self.iniFile) 

		self.responseMode = 0 
		basePath = os.path.join(curAddon.path) 
		# sharedVars.log(None, "basepath : " + basePath)
		self.addonPath =basePath# + "\\AppModules"
		self.copyTB4Ini()
		# sharedVars.log(None, "addonpath : " + self.addonPath)
		self.load()
		self.initDefaults()

	def initDefaults(self) :
		# default option values if ini file does not exist
		if  not os.path.exists(self.iniFile) :
			# self.options = self.option_messengerWindow = self.option_msgcomposeWindow = self.option_startup = None
			self.options["messengerWindow"]["namesCleaned"] = True
			self.options["messengerWindow"]["separateCols"] = True
			self.options["messengerWindow"]["responseMentionGroup"] = True
			self.options["messengerWindow"]["junkStatusCol"] = True
			# made by Chichi or the  "start with inbox" thunderbird addon ->self.options["startup"]["alwaysMainTab"] = True

			self.options["msgcomposeWindow"]["closeMessageWithEscape"] = True
			self.options["msgcomposeWindow"]["spellWords"] = True 
			sharedVars.virtualSpellChk = self.options["msgcomposeWindow"]["virtualSpellChk"]
			self.options["msgcomposeWindow"]["onePress"] = True
		#if self.getOption ("messengerWindow", "separateCols") : self.colSepar = ", "
		# debug logging
		# désactivé sharedVars.debug = self.getOption("startup", "logging")

	def load(self):
		adPath = self.addonPath
		# adPath is the root of the addon path
		self.option_messengerWindow ={
		"responseMentionGroup" : _("Regrouper les mentions 'RE' multiples en une seule"),
		"responseMentionRemove" : _("Supprimer les mentions 'RE' dans la colonne sujet"),
		"responseMentionDelColon" : _("Supprimer les 2 points dans les mentions 'RE', "),
		"namesCleaned" : _("Nettoyer les noms des correspondants dans la liste de messages"),
		"separateCols" : _("Ajouter une ponctuation entre les colonnes"),
		"listGroupName" : _("Masquer les noms de listes de diffusion"),
		"editWords_str" : _("Editer les mots à masquer dans l'objet de messages"),
		"junkStatusCol" : _("Annoncer 'indésirable' si affiché dans la colonne 'Statut indésirable' "),
		"TTFirstUnread" : _("Espace sur un dossier avec non lus  cherche le premier message non lu depuis le début de la liste"),
		"withoutFolderKeyNav" : _("Ne pas utiliser la navigation par initiale dans l'arborescence des dossiers"),
		"noDirectKeyNav" : _("Navigation par initiales indirecte, via une zone d'édition"),
		"withoutReceipt" : _("Ignorer les demandes d'accusé de réception"),
		"WwithUnread" : _("Afficher seulement les dossiers avec non lus dans la boite de dialogue 'Dossiers de l'arborescence'"),
		"WithoutAutoRead" : _("fenêtre séparée de lecture : ne pas lire automatiquement le  mmessage si provoque des blocages de NVDA"),
		"editDelay_str" : _("Editer le délai avant la lecture automatique de la fenêtre séparée du message.\tAlt+d,n ")
		}

		self.option_msgcomposeWindow={
		"spellWords" : _("Vérification orthographique : épeler le mot mal orthographié et le mot suggéré."),
		"virtualSpellChk" : _("Activer l'amélioration de la Vérification orthographique pendant la saisie."),
		"closeMessageWithEscape" : _("La touche Échap ferme le message en cours de rédaction"),
		"onePress" : _("Simple frappe pour  afficher  les menu contextuel, double frappe pour écrire ² ou ³ ou leurs remplaçants.")
	}

		self.option_startup= {}
			# # "alwaysMainTab" : _("Toujours activer l'onglet principal au démarrage de Thunderbird"),
			# # "logging" : _("Journalisation (peut ralentir)")
		# }

		self.option_chichi = {
			"FTnoSpace" : _("Dossiers : Espace ne sélectionne pas le prochain message non lu dans la liste et n'affiche pas la liste de dossiers non lus"),
			"FTnoNavLetter" : _("Dossiers : pas de navigation par initiales"),
			"TTnoSpace" : _("Liste messages : Espace ne lit pas le message du volet d'aperçu"),
			"TTNoExpand" : _("Liste messages : Espace lit le résumé de la conversation du volet d'aperçu"),
			"TTnoSmartReply" : _("Liste messages : pas de  SmartReply"),
			"TTnoFilterBar" : _("Liste messages : ne pas gérer la barre de filtrage rapide"),
			"TTnoEscape" : _("Liste messages : Echappe ne revient pas à l'arborescence"),
			"MainNoTab" : _("fenêtre principale : Tab ne passe pas au volet suivant"),
			"mainNoEscape" : _("Fenêtre principale : rétablir le comportement par défaut de la touche échappe"),
			"closeTBWithCtrlF4" : _("Permettre    la fermeture de Thunderbird avec control+w ou control+F4")
		}

		self.options = ConfigObj(self.iniFile)
		all_options = (("messengerWindow", self.option_messengerWindow),("msgcomposeWindow",self.option_msgcomposeWindow),("startup", self.option_startup), ("chichi", self.option_chichi))
		for x in all_options :
			section, keyValue =x 
			if not section in self.options: self.options.update({section:{}})
			for key in keyValue : 
				if not key in self.options[section] : self.options[section].update({key:False})
		section = self.options["messengerWindow"]
		#sharedVars.useKeyNav =  not section.as_bool ("FKN1_withoutFolderKeyNav")		
		#sharedVars.directKeyNav =   not section.as_bool ("FKN2_noDirectKeyNav")		
		if not"delayReadWnd" in self.options["messengerWindow"] : 
			self.options["messengerWindow"].update({"delayReadWnd":"100"})
		sharedVars.delayReadWnd =    int(section.as_int ("delayReadWnd")		)
		# words to remove from subject in the message list
		if not "removeInSubject" in self.options["messengerWindow"] : 
			self.options["messengerWindow"].update({"removeInSubject":""})
		else : # option  exists   as string  in the ini file
			self.regex_removeInSubject = re.compile(makeRegex(section["removeInSubject"]))
		
		# coptions for chichi : speed needed
		section = self.options["chichi"]
		sharedVars.FTnoNavLetter = section.as_bool ("FTnoNavLetter")
		sharedVars.FTnoSpace = section.as_bool ("FTnoSpace")
		sharedVars.TTnoSpace = section.as_bool ("TTnoSpace")
		sharedVars.TTnoFilterBar = section.as_bool ("TTnoFilterBar")

		# self.withFoldersList = section.as_bool ("WwithFoldersList")		
		#sound
		import shutil
		soundPath = api.config.getUserDefaultConfigPath() + "\\TB+Sounds"
		#print("confPath :" + confPath)
		if  not os.path.exists(soundPath) : 
			libPath =  adPath + "\\SoundLib"
			os.makedirs(soundPath, exist_ok=True)
			shutil.copy2(libPath + "\\filtre.wav" , soundPath + "\\filter.wav")
		from os.path import basename
		soundFilePath = glob.glob(soundPath + "\\*.wav")
		utis.objSoundFiles = {}
		for path in soundFilePath:
			utis.objSoundFiles[basename(path)]= open (path,"rb").read ()
		#utis.playSound("ding")
		# sharedVars.log(None, str(utis.objSoundFiles))
		self.setResponseMode()
		self.setfolderTreeNav()
		return
	def editWords(self) :
		wrds = self.options["messengerWindow"]["removeInSubject"] 
		utis.inputBox(label=_("Mots séparés par des points-virgule : "), title= _("Edition des mots à masquer  dans l'objet des messages"), postFunction=saveWords, startValue=wrds)

	def editDelay(self) :
		utis.inputBox(label=_("Délai entre 20 et 2000 milli secondes  avant  lecture épurée (défaut : 100) : "), title= _("Fenêtre séparée de lecture"), postFunction=saveDelay, startValue=sharedVars.delayReadWnd)

	def backup(self) :
		bakFile = api.config.getUserDefaultConfigPath() + "\\" + self.addonName + ".inibak"
		if   not os.path.exists(self.iniFile) :		
			self.options.write()
		shutil.copyfile(self.iniFile, bakFile) 
		CallLater(30, utis.noSpeechMessage, u"La configuration actuelle  a été sauvegardée dans un fichier .bakini.")
	def restore(self) :
		bakFile = api.config.getUserDefaultConfigPath() + "\\" + self.addonName + ".inibak"
		if   os.path.exists(bakFile) :		
			shutil.copyfile(bakFile, self.iniFile) 
			self.load()
			CallLater(30, utis.noSpeechMessage,u"La configuration sauvegardée a été restaurée.")
		else :
			CallLater(30, utis.noSpeechMessage,_("Fichier de sauvegarde inexistant."))

	def reset(self) :
		bakFile = api.config.getUserDefaultConfigPath() + "\\" + self.addonName + ".inibak"
		if   os.path.exists(self.iniFile) :
			if not os.path.exists(bakFile) :
				os.rename(self.iniFile, bakFile)
			else : 
				os.remove(self.iniFile) 
			self.load()
			self.initDefaults()
			CallLater(30, utis.noSpeechMessage,_("La configuration a été réinitialisée à ses valeurs par défaut"))

	def copyTB4Ini(self) :
		if   os.path.exists(self.iniFile) : return
		tb4File = api.config.getUserDefaultConfigPath() + "\\Thunderbird+4.ini"
		if   os.path.exists(tb4File) :		
			shutil.copyfile(tb4File, self.iniFile) 

	def getOption(self, iniSect, iniKey="") : # si iniKey == "", retourne la section entière 
		if iniSect == "messenger" : iniSect = "messengerWindow"
		elif iniSect == "compose" : iniSect = "msgcomposeWindow"
		if iniKey == "" : return self.options[iniSect]
		else : return self.options[iniSect].as_bool(iniKey)

	def setResponseMode(self):
		if self.getOption("messengerWindow", "responseMentionGroup") : self.responseMode = 1
		elif self.getOption("messengerWindow", "responseMentionRemove") : self.responseMode = 2
		elif self.getOption("messengerWindow", "responseMentionDelColon") : self.responseMode = 3
		else : self.responseMode = 0

	def setfolderTreeNav(self) :
		sharedVars.useKeyNav = (False if  self.getOption("messengerWindow", "withoutFolderKeyNav") else True)
		sharedVars.directKeyNav = (False if  self.getOption("messengerWindow", "noDirectKeyNav") else True)

	def showOptionsMenu(self, frame) :
		mainMenu  = Menu ()
		# menu IDs :0=messenger, 100=compose, 200=startup
		# messengerWindow
		if frame == "messengerWindow" :
			menu, options, keys = Menu(), self.options, list(self.option_messengerWindow.keys())
			#keys.sort ()
			
			for e in range (len(keys)) : 
				lbl = self.option_messengerWindow [keys[e]]
				if keys[e].endswith("_str") : # == "editWords" :
					menu.Append(e, lbl)
				else : 
					menu.AppendCheckItem (0 + e, lbl).Check (options["messengerWindow"].as_bool (keys[e]))
				
			mainMenu.AppendSubMenu (menu, _("Options pour la fenêtre principale"))
		# msgCompose submenu
		if frame in ("messengerWindow", "msgcomposeWindow") :
			menu, options, keys = Menu (), self.options, list(self.option_msgcomposeWindow.keys())
			#keys.sort ()
			for e in range (len (keys)): menu.AppendCheckItem (100+e, self.option_msgcomposeWindow[keys[e]]).Check (options["msgcomposeWindow"].as_bool (keys[e]))	
			mainMenu.AppendSubMenu (menu, _("Options pour la fenêtre de rédaction"))
			mainMenu.Bind (EVT_MENU,self.onOptMenu)
		# startup submenu)
		if frame == "messengerWindow" :
			menu, options, keys = Menu (), self.options, list(self.option_startup.keys())
			#keys.sort ()
			for e in range (len (keys)): menu.AppendCheckItem (200+e, self.option_startup[keys[e]]).Check (options["startup"].as_bool (keys[e]))
			# ajout de activer/ désactiver mise à jour
			menu.Append(200+e+1, getUpdateLabel())
			mainMenu.AppendSubMenu (menu, _("Options de  Mise à jour"))
			mainMenu.Bind (EVT_MENU,self.onOptMenu)
		# Chichi submenu
		if frame == "messengerWindow" :
			menu, options, keys = Menu (), self.options, list(self.option_chichi.keys())
			for e in range (len (keys)): menu.AppendCheckItem (300+e, self.option_chichi[keys[e]]).Check (options["chichi"].as_bool (keys[e]))	
			mainMenu.AppendSubMenu (menu, _("Désactivations   pour Chichi et pour Thunderbird+"))
			mainMenu.Bind (EVT_MENU,self.onOptMenu)

			mainMenu.Append(900, _("Sauvegarder la configuration actuelle"))
			mainMenu.Append(901, _("Restaurer la configuration sauvegardée"))
			mainMenu.Append(902, _("Réinitialiser la configuration"))
	# mainMenu.Bind (EVT_MENU,self.onOptMenu)

		utis.showNVDAMenu  (mainMenu)	

	def onOptMenu(self, evt) :
		eID =evt.Id
		# menu IDs :0=messenger, 100=compose, 200=startup
		# sharedVars.debugLog = ", menu ID : " + str(eID)

		if eID < 100 : # messengerWindow, options fenêtre principale
			IDRange = 0
			section, keys, options = "messengerWindow", list(self.option_messengerWindow.keys()), self.options
			key = keys[eID-IDRange]			
			# sharedVars.log(None, "choosen Key " + str(key))
			if key ==  "editWords_str" :  # is not a check item
				return CallLater(30, self.editWords)
			if key ==  "editDelay_str" :  # is not a check item
				return CallLater(30, self.editDelay)
# =====
			toFind = _("mentions")
			if evt.EventObject.GetLabelText(eID).find (toFind)!=-1 :
				for k in ("responseMentionGroup","responseMentionRemove","responseMentionDelColon"):
					options[section][k] = False
			# ====
			options[section][key]= evt.IsChecked ()
			self.setResponseMode()
			self.setfolderTreeNav()
			return options.write () 	
		elif eID < 200  : # msgcomposeWindow
			IDRange = 100
			section, keys, options = "msgcomposeWindow", list(self.option_msgcomposeWindow.keys()), self.options
			key=keys[eID-IDRange]			
			options[section][key]= evt.IsChecked ()
			if key == "virtualSpellChk" :
				sharedVars.virtualSpellChk = self.options[section][key]
			return options.write () 	
		elif eID < 300  : # update options
			IDRange = 200
			section, keys, options = "startup", list(self.option_startup.keys()), self.options
			if eID == IDRange +4 : # old + len(keys)) : # last option :update
				CallLater(40, toggleUpdateState)
				return
			key = keys[4] #   =# keys[eID-IDRange]
			options[section][key]= evt.IsChecked ()
			if key == "logging" :
				sharedVars.debug = options[section][key]
				sharedVars.debugLog = ""
			return options.write () 	
		# chichi
		elif eID < 400  : # chichi
			IDRange = 300
			section, keys, options = "chichi", list(self.option_chichi.keys()), self.options
			# if eID == (IDRange + len(keys)) : # last option :update
				# CallLater(40, toggleUpdateState)
				# return
			key=keys[eID-IDRange]			
			options[section][key]= evt.IsChecked ()
			if key == "TTnoSpace" : sharedVars.TTnoSpace = self.options[section][key]
			elif key == "TTnoFilterBar" : sharedVars.TTnoFilterBar = self.options[section][key]
			elif key == "FTnoNavLetter" : sharedVars.FTnoNavLetter = self.options[section][key]
			elif key == "FTnoSpace" : sharedVars.FTnoSpace = self.options[section][key]
			return options.write () 	
		elif eID == 900 :
			self.backup()
		elif eID == 901 :
			self.restore()
		elif eID == 902 :
			self.reset()
		return


import os
def getUpdateLabel() :
	addonName = "Thunderbird+4"
	nextUpdateFile = api.config.getUserDefaultConfigPath()+"\\addons\\" +  addonName + "-nextUpdate.pickle"
	exists =  (True if  os.path.exists(nextUpdateFile) else False)
	if exists and  os.path.getsize(nextUpdateFile) < 5 : # mise à jour désactivée # maj désactivée
		return  _("Activer la mise à jour automatique")
	return _("Désactiver la mise à jour automatique")

def toggleUpdateState() :
	addonName = "Thunderbird+4"
	nextUpdateFile = api.config.getUserDefaultConfigPath()+"\\addons\\" +  addonName + "-nextUpdate.pickle"
	if  os.path.exists(nextUpdateFile) and   os.path.getsize(nextUpdateFile) < 5 : 
		os.remove(nextUpdateFile) # réactive la maj
		cancelSpeech()
		CallAfter(message, _("La mise à jour automatique a bien été activée. Vous pouvez redémarrer NVDA pour rechercher une mise à jour."))
		return 1
	# désactivation maj : écrit le fichier de longueur < 5 et contenant 0
	cancelSpeech()
	try :
		ut = "0"
		with open(nextUpdateFile, mode="w") as fileObj :
			#pickle.dump(ut, fileObj)  #, protocol=0
			fileObj.write(ut)
	except :
		return CallAfter(message, _("Erreur d'enregistrement du fichier de paramètres de mise à jour."))
	CallAfter(message, _("La mise à jour automatique a bien été désactivée."))
	return

	def removeLabel(value, label) :
		return  value[len(label):]

def makeRegex(words) :
	words = re.escape(str(words))
	words = words.replace(";", "|")
	return words

def saveWords(words) :
	words = str(words)
	if words == "ibCancel" : return
	# sharedVars.log(None, "Mots saisis " + words)
	# speech.cancelSpeech()
	sharedVars.oSettings.options["messengerWindow"]["removeInSubject"] = words
	# sharedVars.delayReadWnd = iDelay
	sharedVars.oSettings.options["messengerWindow"].update({"removeInSubject" : words})
	sharedVars.oSettings.options.write()
	sharedVars.oSettings.regex_removeInSubject = re.compile(makeRegex(words))

def saveDelay(strDelay) :
	if strDelay == "ibCancel" : return
	cancelSpeech()
	try : iDelay = int(strDelay)
	except : return beep(100, 50) # return CallLater(50, message, u"La valeur doit être un nombre")
	if iDelay < 20 or iDelay > 2000 :
		return beep(250, 50) # CallLater(50, message, u"Le délai doit être compris entre 20 et 2000 milli-secondes !")
	sharedVars.delayReadWnd = iDelay
	sharedVars.oSettings.options["messengerWindow"].update({"delayReadWnd":strDelay})
	sharedVars.oSettings.options.write()
