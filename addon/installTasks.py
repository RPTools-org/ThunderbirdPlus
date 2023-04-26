#-*- coding:utf-8 -*
# for ThunderbirdPlus 4

import addonHandler
import gui
import wx

addonHandler.initTranslation()

# Code from Emoticons add-on
def onInstall():
	for addon in addonHandler.getAvailableAddons():
		if addon.name == "Thunderbird+4":
			if gui.messageBox(
				# Translators: the label of a message box dialog.
				_("Thunderbird+4 est installé et sera remplacée par Thunderbird+. \nVoulez-vous la supprimer ? \nSinon, elle sera désactivée."),
				# Translators: the title of a message box dialog.
				_("Désinstallation de Thunderbird+4"),
				wx.YES|wx.NO|wx.ICON_WARNING)==wx.YES:
					addon.requestRemove()
			else :
				addon.enable(False)
			return
