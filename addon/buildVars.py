# -*- coding: UTF-8 -*-
# Thunderbird+ 4  
# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.


# Since some strings in "addon_info" are translatable,
# we need to include them in the .po files.
# Gettext recognizes only strings given as parameters to the "_" function.
# To avoid initializing translations in this module we simply roll our own "fake" "_" function
# which returns whatever is given to it as an argument.
def _(arg):
	return arg

# Add-on information variables
addon_info = {
	# add-on Name/identifier, internal for NVDA
	"addon_name": "Thunderbird+4",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown
	# on installation and add-on information.
	"addon_summary": _("Thunderbird+ 4"),
	# Add-on description
	# Translators: Long description to be shown for this add-on
	# on add-on information from add-ons manager
	"addon_description": _("""This extension adds commands to Thunderbird 102 and above to make it more accessible, efficient and comfortable to use."""),
	# version
	"addon_version": "4.5",
	# Author(s)
	"addon_author": u"Pierre-Louis Renaud (Thunderbird v. 78 to 102), Daniel Poiraud (TB v. 68 to 91), Abdelkrim Bensaïd for a part of TB 78, Yannick (TB v. 38 to 60)",
	# URL for the add-on documentation support
	"addon_url": "http://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-en.html",
	# Documentation file name
	"addon_docFileName": "addonUserManual.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion": "2019.3.0",
	# Last NVDA version supported/tested
	# (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion": "2023.1.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel": None,
}

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
import os.path
pythonSources = [
	os.path.join("addon", "*.py"),
	os.path.join("addon", "appModules", "*.py"),
	os.path.join("addon", "appModules", "messengerWindow", "*.py"),
	os.path.join("addon", "appModules", "msgComposeWindow", "*.py"),
	os.path.join("addon", "appModules", "shared", "*.py"),
	os.path.join("addon", "globalPlugins", "*.py"),
	os.path.join("addon", "globalPlugins", "shared", "*.py"),
]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory,
# not to the root directory of your addon sources.
excludedFiles = []

# If your add-on is written in a language other than english,
# modify this variable.
# For example:
# set baseLanguage to "es" if your add-on is primarily written in spanish.
baseLanguage = "en"