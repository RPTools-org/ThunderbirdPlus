# -*- coding: utf-8 -*-
# Thunderbird+4

try: 	from urllib import urlopen
except Exception: from urllib.request import urlopen
try: 	from urllib import Request
except Exception: from urllib.request import Request

import api, globalVars
import os, wx
import  gui
from ui import  message, browseableMessage
import addonHandler
addonHandler.initTranslation()
import time, winUser
import config
from tones import beep
import pickle


class availableUpdateDialog(wx.Dialog):

	def __init__(self, parent, title, msg, releaseNoteURL=None):  #, message, auto, releaseNoteURL=None , releaseNoteURL
		super(availableUpdateDialog, self).__init__(parent, -1, title=title)
		self.parent = parent    # mainFrame
		mainSizer = wx.BoxSizer(wx.VERTICAL)
		sHelper = gui.guiHelper.BoxSizerHelper(self, orientation=wx.VERTICAL)
		textStatic = sHelper.addItem(wx.StaticText(self))
		textStatic.SetLabel(msg)
		bHelper = gui.guiHelper.ButtonHelper(wx.HORIZONTAL)	
		# try :
			# with urlopen(releaseNoteURL) as data :
				# data=data.read()
				# if not data : releaseNoteURL =None
		# except: releaseNoteURL =None  
		if releaseNoteURL:
			self.releaseNoteURL = releaseNoteURL
			infoButton = bHelper.addButton(self, label=_("&Quoi de neuf"))
			infoButton .Bind(wx.EVT_BUTTON, self.onInfoButton)   #onInfoButton onReleaseNotesButton2
		yesButton = bHelper.addButton(self, wx.ID_YES, label=_("&Oui"))
		laterButton = bHelper.addButton(self,  label=_("&Plus tard"))  #wx.NewId(),
		noButton = bHelper.addButton(self, wx.ID_NO, label=_("&Désactiver"))
		cancelButton = bHelper.addButton(self, wx.ID_CANCEL) 
		#events
		yesButton.Bind(wx.EVT_BUTTON, self.onYesButton)  # onYesButton
		laterButton.Bind(wx.EVT_BUTTON, self.onLaterButton)
		noButton.Bind(wx.EVT_BUTTON, self.onNoButton)  # onYesButton	
		sHelper.addDialogDismissButtons(bHelper)
		mainSizer.Add(sHelper.sizer, border=gui.guiHelper.BORDER_FOR_DIALOGS, flag=wx.ALL)
		mainSizer.Fit(self)
		self.SetSizer(mainSizer)
		#self.SetTitle(title)
		#yesButton.SetFocus()
		infoButton.SetFocus()
		self.CentreOnScreen()
		# the text in the window must be spoken.

		option = config.conf["presentation"]["reportObjectDescriptions"]
		config.conf["presentation"]["reportObjectDescriptions"] = True
		self.Show()
		winUser.setForegroundWindow(self.GetHandle())
		api.processPendingEvents()
		config.conf["presentation"]["reportObjectDescriptions"] = option 

	def onYesButton(self, event):
		self.EndModal(wx.ID_YES)

	def onLaterButton(self, event):
		self.EndModal(6666)

	def onNoButton(self, event):
		self.EndModal(wx.ID_NO)

	def onInfoButton(self, event):
		os.startfile (self.releaseNoteURL)
# end of  classe
# functions
def getURLHelp(url) :
	# 2022-12-20 localized
	from languageHandler import getLanguage
	lang = getLanguage()
	if "PT" not in   lang :
		lang = lang.split("_")[0]
	return url.format(lang)
	
# Variables to configure
baseUrl="https://www.rptools.org/"
urlHelp = getURLHelp(baseUrl + "Outils-DV/changes_{0}.html#histo")
urlFileInfos = baseUrl + "fileInfos.php?key=thunderbirdup4102"
# test urlFileInfos = baseUrl + "fileInfos.php?key=thunderbirduptest"
# on peut aussi donner un lien direct : urlFileInfos = baseUrl + "dossierFichieonInfoButton/motCléExtension.txt"
# Structure du fichier d'informations,  l'ordre des lignes doit être respecté
# version=3.2.4
# dbID=identifiant pour les statistiques 
# name=Thunderbird+
# type=2022-01-15.nvda-addon
# path = "https://www.monsite.orfg/dossierContenantLesFichiersInfo/"
# Le nom du fichier à télécharger est donc : path + "/" + nane + "-" + version + "-" + type

isDlg = False

def checkUpdate(autoUp) :
	global isDlg, urlHelp
	# beep(440, 30)
	if isDlg : return
	nm, curVer = getCurVersion() 
	# print("TbPlus curVer: " + nm + " curVer " + curVer)
	# décommenter la ligne ci-dessous pour provoquer test màj
	# curVer = "4.3.1" # pour provoquer test mise à jour 
	if autoUp : 
		if not hasToUpdate(nm) : return
	name, ver =  getLastVersion()
	if curVer >= ver : 
		if not autoUp : message(name + " " + curVer + _(" est à jour."))
		return
	isDlg = True
	msg = _("Voulez-vous mettre à jour la version {0} vers la version {1} ?").format(curVer, ver)
	with availableUpdateDialog(gui.mainFrame,_("Mise à jour de l'extension Thunderbird+"), msg, releaseNoteURL=urlHelp) as dlg:  
		result=dlg.ShowModal()
	if result ==  6666 : # later
		wx.CallLater(40, setNextUpdate, nm)
	elif result ==  wx.ID_NO :
		wx.CallLater(40, setNextUpdate, nm, True) # disable
	elif result ==  wx.ID_YES :
		result, msg = doUpdate(curVer)
		if result < 1 :
			browseableMessage (message = msg, title = _("Mise à jour de l'extension") + name, isHtml = False)
	isDlg = False

def getLastVersion() :
	global urlFileInfos
	# bytes = getFileSizeFromURL(urlFileInfos) 
	# return "taille : " + str(bytes), "1.0"
	try :
		with urlopen  (urlFileInfos) as data :
			data = data.read().decode()
	except :
		return _("Erreur de vérification de la version"), "1.0"
	if len(data)  < 10 : # v 3.4.2 si longueur du contenu fileInfos < 10 dans le cas de TB+
		#beep(100, 20)
		return _("Erreur de lecture du file Infos"), "1.0"
	lines = data.split("\n")
	v = lines[0].split("=")[1] # version
	v = v.split(" ")[0]
	n = 	 lines[2].split("=")[1] # name
	return n, v

def doUpdate(oldVer) :
	global baseUrl, urlFileInfos
	beep(337, 1)
	try :
		with urlopen  (urlFileInfos) as data :
			data = data.read().decode()
	except :
		return -1, _("Erreur de récupération des informations du fichier")
	if len(data) < 10 :
		return -1, _("Erreur de récupération des informations du fichier")
	lines = data.split("\n")
	ver = lines[0].split("=")[1]
	dbID = lines[1].split("=")[1]
	name = 	 lines[2].split("=")[1]
	dlFile= lines[3].split("=")[1]
	path = lines[4].split("=")[1]
	beep(337, 1)
	# download addon or new major version notification
	#urlFile =  path + name + "-" + ver + "-" + type
	urlFile =  path + dlFile 
	try :
		with urlopen  (urlFile) as data :
			data = data.read()
	except :
		return -2, _("Erreur de téléchargement de:\n") + urlFile
	lenData = len(data) # v 3.4.2
	if lenData < 10000 : return -3, _("Erreur de fichier vide")
	# sauvegarde dans fichier
	beep(337, 1)
	if ".html" in dlFile: 
		filePath = os.getenv('temp') + "\\" + dlFile
	else : 
		filePath = os.getenv('temp') + "\\Thunderbird+-update.nvda-addon"
	# v 3.4.2 suppression fichier précédent par sécurité
	if  os.path.exists(filePath) :
		try : 
			os.remove(filePath)
		except OSError as error:
			return -4, error + _(", ne peut supprimer : ") + filePath
	# écriture
	try :
		with open(filePath, mode="wb") as fileObj :
			fileObj.write(data)
	except :
		return -4, _("Erreur d'enregistrement de:\n") + filePath
	# v 3.4.2 vérif taille fichier écrit 
	if os.path.getsize(filePath)  < lenData :
		return  - -4, _("Erreur d'enregistrement de l'extension dans un fichier temporaire.")
	# updateinfos
	try:
		from urllib import parse
	except Exception:
		from urllib.request import parse
	urlFile = baseUrl + "updateInfos.php?p=" + dbID + "&a=" + name + "-" + ver + "-old%20" + str(oldVer) + "&u=" + parse.quote(os.getenv('username') .encode('latin-1'))
	try :
		with urlopen  (urlFile) as data :
			data = data.read()
	except :
		pass
	# lance l'installation de l'extension ou le fichier HTML
	os.startfile (filePath)
	return 1, "OK"

import addonHandler
import time

def getCurVersion() :
	_curAddon = addonHandler.getCodeAddon()
	name = _curAddon.manifest["name"]
	ver = _curAddon.manifest["version"]
	return  name, ver.split(" ")[0]
import api
def setNextUpdate(addonName, disable=False) :
	from speech import cancelSpeech
	cancelSpeech()
	nextUpdateFile = api.config.getUserDefaultConfigPath()+"\\addons\\" +  addonName + "-nextUpdate.pickle"
	if not disable :
		# anciien ut = str(time.time() + 3600 * 72) 
		ut = time.time() + 3600 * 72 
		msg = _("La   mise à jour  sera à nouveau proposée dans 3 jours. Entretemps, vous pourrez presser AltGr+Maj+puissance2 pour effectuer une recherche de mise à jour.")
		fMode = "wb"
	else :  # disable auto update
		ut = "0"
		fMode = "w"
		msg = _("La mise à jour automatique a été désactivée. presser    AltGr+Maj+puissance2 pour une mise à jour manuelle.")

	try :
		with open(nextUpdateFile, mode=fMode) as fileObj :
			if disable :
				fileObj.write(ut)
			else :
					pickle.dump(ut, fileObj)  #, protocol=0
	except :
		msg = _("Erreur d'enregistrement de:\n") + nextUpdateFile
		pass
	#os.startfile(nextUpdateFile)
	wx.CallAfter(message, msg)

def hasToUpdate(addonName) :
	nextUpdateFile = api.config.getUserDefaultConfigPath()+"\\addons\\" +  addonName + "-nextUpdate.pickle"
	if  not os.path.exists(nextUpdateFile) : return True
	if os.path.getsize(nextUpdateFile) < 5 : return False # mise à jour désactivée

	now = time.time() 
	try :
		with open(nextUpdateFile, mode="rb") as fileObj :
			ut = (pickle.load(fileObj))
		ut = float(ut)
	except :
		ut = now - 3600
		pass
	#print("TB+ update Time : " + str(ut))
	if ut < now :
		return True
	return False

def getFileSizeFromURL(url) :
	req = Request(url, method='HEAD')
	f = urlopen(req)
	#f.status # 200
	return str(f.headers['Content-Length'])

