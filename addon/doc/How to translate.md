 # Documentation for translators ##

### Written by Rémy Ruiz (BlindHelp) ###

If you want to become a new member of the tim translation of Thunderbird+ you're welcome!

Note: For the addon documentations, it is not recommended to use the Spanish and Portuguese versions as bases for a new translation, they have an old structure. Documentation in English and French are the most recent.

# How to translate the Thunderbird+ addon in other language? #

It is very easy!

## How to translate manually Thunderbird+ into other languages step by step instructions ##

Here are the explanations step by step ...

First of all, you will need to create a folder corresponding to your language manually; (not translation system)

This folders are located on folder of the local language. Example: for French on folder fr, what you found following the path:

`1.` `Start \ All Programs \ NVDA \ Explore NVDA user configuration directory \ addons \ Thunderbird+4 \ locale \ fr \ LC_MESSAGES \`

You will find two files called:

nvda.mo `=` result of the compilation of the file:

nvda.po

This is the file that contains the messages that you translate into your language.

the file must be encoded in UTF-8 format.

`2.` The file nvda.po is opened with the poEdit program.

You can get it from:

[http://www.poedit.net](http://www.poedit.net)

File name:

poedit-1.4.6-setup.exe

Link:

[http://freefr.dl.sourceforge.net/project/poedit/poedit/1.4.6/poedit-1.4.6-setup.exe](http://freefr.dl.sourceforge.net/project/poedit/poedit/1.4.6/poedit-1.4.6-setup.exe)

This version is more accessible but old

Source Poedit download SourceForge.net:

[http://sourceforge.net/projects/poedit/](http://sourceforge.net/projects/poedit/)

You can download the latest version but it is not very accessible.

Link:

[http://sourceforge.net/projects/poedit/files/latest/download](http://sourceforge.net/projects/poedit/files/latest/download)

Download poeditMadeEasy-3.1.nvda-addon for NVDA compatible 2021.1 here; (Link via BlindHelp.github.io):

[https://blindhelp.github.io/nvda-poeditMadeEasy-3.1-p03.nvda-addon)

File name:

nvda-poeditMadeEasy-3.1-p03.nvda-addon

### Instructions for translators ###

`1.` Install PoEdit. It is used for editting .po catalog files on a quick and easy way.

`2.` Open nvda.po file in PoEdit and translate all messages.

`3.` In PoEdit, you use your arrow keys for navigating message list, the Tab key for moving between your translation edit box and message list, and Control+C for copying original text to
translation field (may be useful for easier translation of long messages).

`4.` Also please fill in your name and E-Mail address when asked by the program, or enter them in PoEdit's preferences.

`5.` Go to the catalog menu, then choose Settings. A dialog box will open with various edit fields that you should fill in, such as package version, language team, language name and
country etc.

Note: some fields already are filled, so leave it!

`6.` After entering the required information, you can save the file by pressing Ctrl+S. Your nvda.po file will then be saved and compiled into a binary nvda.mo format, which will be located
in the same directory as nvda.po file.

`7.` In "Locale" directory, create a subdirectory with a name of your language prefix manually; (not translation system).

For example, in my case when was translating  Thunderbird+ addon to spanish, the subdirectory name must be "es". Next, under your language subdirectory, create a directory named

"LC_MESSAGES".

`8.` That's it! Now the addon Thunderbird+ should detect your language!

Note: Don't forget to change manually in the properties tab  of the file nvda.po (poedit) your name and email and your language (not translation system.

#### Some notes for translators ####

In nvda.po file.

`1.` The `&` (ampersand) sign infront of any letter indicates that the letter next to the & sign will be underlined and thus will be used as a shortcut key.

example, "`&`Aide" (the & sign infront of a letter ) indicates that the shortcut for Aide" dialog will be A.

##### Language codes and variants (as pt-br) #####

[Language localisation - Wikipedia, the free encyclopedia:](https://en.wikipedia.org/wiki/Language_localisation)

### Codes for folder names in addons ###

po file status for NVDA:

[http://addons.nvda-project.org/poStatus.html](http://addons.nvda-project.org/poStatus.html)

Note: In this case for the folders, variant is separated from the language with underline (_), not with hyphen (-) and the main language code is in lowercase, but the variant is in uppercase. For example, pt_BR if you create it manually; (not translation system).

### How to translate the documentation manually into your language (not translation system) ###

`1.` You have to find the documentation called "readme.md" in english that is located in the following path

`Start \ All Programs \ NVDA \ Explore NVDA user configuration directory \ addons \ Thunderbird+4 \ doc \ en\`

readme.md documentation file is located in your own folder of your language!

the converted HTML files must be in the path of your own folder of your language.

You will find one file in english called:

readme.md

`2.` Open readme.md with a text editor such as:

Notepad++

[Notepad++ official site:](http://notepad-plus.sourceforge.net/)

[Notepad++ wiki:](http://sourceforge.net/apps/mediawiki/notepad-plus/index.php?title=Main_Page)

Note:

You can also use this program

MarkDown# Editor

File name:

mked1230.exe

Link:

[http://hibara.org/software/markdownsharpeditor/download/?f=mked1230.exe](http://hibara.org/software/markdownsharpeditor/download/?f=mked1230.exe)

Source:

[HIBARA.ORG - MarkDown#Editor](http://hibara.org/software/markdownsharpeditor/)

Important Note!

to change the language, by default it starts in Japanese

`1.` Go to menu alt+v

`2.` Two arrows up

`3.` You hear the Word submenu

`4.` Right Arrow

`5.` An up arrow

`6.` Choose first item: English an press Enter.

`7.` And restart this application, by clicking on the Yes button

Note: The name of the button depends on the language used in your system.

`8.` Now the program MarkDown# Editor is in English.


Finally, don't forget to send your translation language and your email to Pierre-Louis, so the add it in the next version of this fabulous addon!

 Only if you have translated it manually, and have not gone through the translation system!

Thank you for having translated the Thunderbird+ addon in your language!

Have fun with Thunderbird+!

@+

Rémy Ruiz (BlindHelp)

End of document.
