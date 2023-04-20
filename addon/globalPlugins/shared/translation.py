# -*- coding:utf-8 -*
# translation.py
# A part of Thunderbird+ 4.0  for Thunderbird 102
# Copyright (C) 2023 Cyrille Bougot
# This file is covered by the GNU General Public License version 2 or later.

"""This module provides a tool for add-ons written in another language than English.

If the translatable messages in your add-on are not in English (e.g. French), using
`addonHandler.initTranslation` will cause gettext (`_`) to return French messages for languages with no translation.
This module provides a function that allow gettext (`_`) to return English messages instead.

To use it, on top of your modules, call `translations.initTranslationWithEnglishFallback()` instead
of `addonHandler.initTranslation`.
"""

import os
import inspect
import gettext
import addonHandler
import languageHandler


# Modified function based on initTranslation in addonHandler/__init__.py
def initTranslationWithEnglishFallback():
	addon = addonHandler.getCodeAddon(frameDist=2)
	# Call our getTranslationsInstance instead of normal one.
	translations = getTranslationsInstance(addon)
	# Point _ to the translation object in the globals namespace of the caller frame
	# FIXME: should we retrieve the caller module object explicitly?
	try:
		callerFrame = inspect.currentframe().f_back
		callerFrame.f_globals['_'] = translations.gettext
		# Install our pgettext function.
		callerFrame.f_globals['pgettext'] = languageHandler.makePgettext(translations)
	finally:
		del callerFrame # Avoid reference problems with frames (per python docs)

# Modified function based on Addon.getTranslationsInstance in addonHandler/__init__.py
def getTranslationsInstance(addon, domain='nvda'):
	""" Gets the gettext translation instance for this add-on.
	<addon-path>\\locale will be used to find .mo files, if exists.
	NVDA's language is used to search for translations; if no translation exists for this language, English is
	used.
	If no translation file is found the default fallback null translation is returned.
	@param domain: the translation domain to retrieve. The 'nvda' default should be used in most cases.
	@returns: the gettext translation class.
	"""
	localedir = os.path.join(addon.path, "locale")
	return gettext.translation(
		domain,
		localedir=localedir,
		# If language not available, use English as second try
		languages=[languageHandler.getLanguage(), "en"],
		fallback=True,
	)


