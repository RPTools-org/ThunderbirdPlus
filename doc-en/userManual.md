# Thunderbird+

* Authors: Pierre-Louis Renaud (From Thunderbird 78 to 102) & Cyrille Bougot (TB 102), Daniel Poiraud (From TB 78 to 91), Yannick (TB 45 to 60);
* URL: [User manual][4] ;
  [History of changes at RPTools.org][5] ;
  [Contact in French or English][6] ;
* Download [stable version][1]
* Download [Latest version from RPTools.org][3] ;
* NVDA compatibility: 2019.3 and later;
* Thunderbird compatibility: versions 102.x;
* [Source code on gitHub][2]

Note: This add-on is not compatible with the Mozilla Apps Enhancements add-on. If the latter is installed, you will have to disable or uninstall it before installing Thunderbird+;

<!-- [Jump to table of contents](#toc) -->

## Description

This add-on greatly improves the Mozilla Thunderbird messaging client's comfort and efficient use with NVDA.

Improvements relate to the following aspects:

### Auditory Comfort

* Alerts such as "so-and-so requested a return receipt" can be deactivated via an option;
* The alerts "This is a draft" and "Thunderbird thinks this message is fraudulent" are simply dismissed in silence; 
* Options allow you to disable mailing list names announcement, remove or group "RE" mentions and clean up the names of correspondents by removing numbers and other annoying special characters;  

### Navigating The Main Window

* Moving to the next panel is done using the TAB key, while the Escape key returns to the previous panel. This is more comfortable than through F6 and Shift+F6. 
* The selection of tabs with Control+Tab and Control+number is spoken as in this example: Tab 1 of 4, inbox; 
* A keyboard shortcut allows you to list tabs in a menu in order to easily activate one of them;
* A keyboard shortcut is used to display the context menu of the tabs bar;

### The Folder Tree view

* Alt+Down Arrow and Alt+Up Arrow let you navigate among folders containing unread messages;
* Typing a letter or number selects the next folder whose name begins with that character. With the Shift key, the move occurs from bottom to top. Besides, the name of the account to which the folder belongs is announced;
* Pressing Space bar on a folder containing unread messages selects the first unread message of the message list;
* Two dialogs for accounts and their associated folders allow you to filter them by keyword or display only folders with unread messages;

### The Message List

* Choosing columns and their layout within the message list is made accessible through a simple dialog;
* Viewing the columns of the message list: shortcuts allow you to easily listen to, spell or copy the sender's name, the message subject or its date by typing a digit on the alphanumeric keypad. For instance, a single press on 1 or & announces the sender, two presses spell the name and three presses copy it to the clipboard;
* Viewing the headers in the header pane displayed using F8: with Alt+ a digit, 1 press announces any header containing the sender's addresses or recipients, 2 presses open a dialog to copy them, 3 presses open the native Thunderbird context menu associated with the header;
* Cleaned quick message text preview via space key, Alt+down arrow or F4: Large header blocks in message quotes are replaced by the phrase "Sender name wrote". NVDA will also announce "clickable link" instead of the long address of the link.
* Quick overview of quotes in chronological order, from bottom to top, via Shift+Space, Alt+up arrow or Shift+F4;
* Easy access to attachments using the shortcut Alt+page down or via number 1 of alphanumeric keypad;

<!-- Translators : étiquettes = tags -->
### Quick Filter Bar And Priority Tag Management 

* It is possible to navigate filtering options with the vertical arrows. The Enter key is used to check or uncheck a filter;
* Adding or removing tags is done by simply pressing Shift+ a digit on the alphanumeric keyboard. For example, press Shift+4 to add the "To Do" tag to a message. You can then filter the message list by tag via the quick filter bar which is hence accessible; 

### The Message Write Window

Alt+1 announces the Sender, Alt+2 announces the Recipient, Alt+3 announces the Attachments, etc. Two presses place the focus on one of these fields;

### Spell-check Dialog

* The misspelled word is announced with or without spelling before the suggested word. The shortcuts NVDA+Tab or Alt+up arrow announce misspelled and replacement words: 1 press spells the words at normal speed, 2 presses spell them quickly, 3 presses copy the misspelled word to the clipboard for analysis in another edit field; 
* Various combinations involving the Enter key trigger the Replace, Replace All, Ignore, Ignore All, or Add Word to Dictionary buttons have been added for even more convenience within this dialog; 

### Automatic Update

ThunderbirdPlus contains an independent auto-update system with deactivation/reactivation and postponement features;

### Side-to-side Operation with Chichi

ThunderbirdPlus is designed to work seamlessly with Chichi, an add-on that installs directly onto Thunderbird.

Read about this on the [page of Chichi](https://www.rptools.org/Outils-DV/thunderbird-chichi-en.html) ;

### A Note About Languages

Some features will not work properly if ThunderbirdPlus is not translated into the language you use with NVDA and Thunderbird.

* Alerts will not be intercepted. These are draft-related alerts, receipt requests, fraudulent messages, updates and so on.;
* Thunderbird add-on search enhancement feature will not work.

To date, the add-on is available in the following languages:

[Original version in French](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_fr.html) : written by the developer;

Translations from oldest to newest order:

* [Portuguese](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_pt_PT.html): by Rui Fontes from TifloTecnia.com and member of the NVDA Portuguese team;
* [Spanish](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_es.html): by Rémy Ruiz;
* [English](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_en.html): by Bachir Benanou, former member of the NVDA French translation team;
* [Turkish](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_tr.html): by  umut korkmaz;
* [Czech](https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_cs.html) : by Jarek Krcmar ;

Thank you, translators.

<a name="navpanels">

## Navigating The Panels of the Message Tab (Tab, Escape)

This hereby concerns the tab containing the following panels: folder tree view, message list, header pane and message preview (shown or hidden via the F8 key).

* TAB: Moves to the next panel. This shortcut will be more ergonomic for some people than F6;
* Escape: Returns to the previous panel. Equivalent to Shift+F6;

Note:

When tabbing from the message list to reach the text, the header area is skipped. To reach this header area, press Alt+one digit on the alphanumeric keyboard three times quickly, then press Escape to exit the header context menu. These Alt+digit shortcuts reduce the need to go to the header area. For more details, see the "Header viewing" section below.  


<a name="threadTree">

## Message List, Preview Pane And Separate Reading Window 

Some of the following shortcuts are common to these three contexts, others relate to a particular context.

<a name="attach">

### Accessing Attachments (Alt+Page down) 

* Alt+page down or Alt+p: if the preview pane is displayed (via F8), Opens the list of attachments for the selected message;
* Alt+9 or number 1 or 2: only from the message list, one press states the number of attachments, two presses open the list of attachments;

<a name="readPreview">

### Quick And Uncluttered Message Reading 

* Quick message reading commands are available in three contexts: from the message list, from a message opened in a tab or from a message opened in a separate window;
* They are now all compatible with messages from Framalistes;
* Most quick-reading keyboard shortcuts have been concentrated to minimize hand movement during a session of reading many messages;
* A single press of the main key of a shortcut starts the uncluttered reading of the message, i.e. with strongly shortened quote headers.
* A double press starts reading the message in its original form. The terms "unfiltered reading" are synonymous;

<a name="readFromList">

#### Quick Message Reading From The List Without Leaving It (Spacebar, F4 or Alt+down arrow) 

To benefit from this feature, you will have to display the message reading pane with the F8 key first. By pressing this key, you will hear if this pane is present or absent;

Next, go to the message list and use the following keys:

* Space, Alt+Down Arrow or F4: Reads the message body without leaving the list. After reading a message, press down arrow then Space or Alt+down arrow or F4 to hear the next message;
* Double-keystroke, displays the list of links in a message if Chichi is active. If an RSS feed article is selected, it will be opened in the Internet browser;
* Shift+space, Alt+Up arrow or Shift+f4: same function in addition to reading quotes in their chronological order (from bottom to top);

And to complete the commands available from the message list, let's mention here:

* Letter n or Alt+Right arrow: selects the next unread message, even across folders;
* Alt+Page down or Alt+p from the message list: allows you to go directly to the attachments area without Tabbing through the text;  

<a name="readFromWinTab">

### Quick Message Reading In A Separate Window Or Message Tab (F4 or Alt+Down Arrow) 

When a message is opened in a new window, the message body is read automatically by default. However, the following shortcuts allow you to hear the message again at any time.

* F4 or Alt+down arrow: quick message body reading;
* Shift+F4 or Alt+up arrow: same function but in reverse;

Notes:

* As a reminder, a double-press of these shortcuts starts the reading of the original message;
* Automatic reading may cause NVDA to crash on some PCs, especially if the account is set to IMAP. To try resolving this issue, the Alt+d shortcut opens an edit box that lets you lengthen the delay between opening the window and starting automatic reading <br>
If setting this delay does not solve the problem, you may disable the automatic reading via the menu Shift+[Grave](keyEquiv_en.html#aboveTab) / Options for the main window / separate reading window: do not automatically read message if this causes NVDA blockages;
* To make the most of uncluttered reading and protect yourself from remote content that does not respect your privacy, display the body of messages in simple HTML. To do this, open the View menu, scroll down to Message Body and in the submenu, choose the Simple HTML option.


Viewing columns and headers:

It is important here to distinguish between columns and headers: the word "column" is used below to indicate the value of a row cell in the message table. The word "header" refers to the message itself. Headers can be viewed both in the message preview pane and in the separate tab or window of an open message;

<a name="readCols">

### Viewing Columns: one Digit On The Alphanumeric Keyboard 

These keys are for columns in the message list only. Type a number on the alphanumeric keyboard without pressing the Shift key:

* A single press of a number: states the name and value of the corresponding column;
* Two presses of a number: spells the value of the corresponding column;
* Three quick presses of a number: copies the column value to the clipboard. To copy the addresses of the various senders and recipients, use the header reading procedure discussed below; 

<a name="readHeaders">

### Header Reading: Alt+one Digit On Alphanumeric Keyboard 

The following shortcuts can be used from the main window if the preview panel is displayed (via F8) and from the separate tab or window of an open message. One tap speaks the header and two taps displays a context menu as appropriate;

* Alt+1: one press announces the sender's name and his email address, two presses open an edit box of these values. You can edit them and then press Enter to copy them to the clipboard. Three presses: opens the context menu of the header;
* Alt+2: Subject with name of mailing list if any;
* Alt+3: Message date;
* Alt+4 to: main message recipients. If several recipients, three presses set focus on the first recipient, then tab moves to the next one. Applications key on each recipient displays the context menu;
* Alt+5: Copy recipients; 
* Alt+6: Blind copy recipients;
* Alt+7: "reply to" address;
* Alt+8: User agent, if full headers are enabled via the View / headers / full menu;
* Alt+9: 1 press announces the number of attachments, 2 presses opens the attachment list;
* Alt+0: List of priority tags placed on a message;
* Alt+[Minus](keyEquiv_en.html#bs2) or Alt+End: Gives a shortened version of the status bar: number of unread messages, total number of messages and quick filter expression; 
* Alt+[Equals](keyEquiv_en.html#bs1): Opens the tabs context menu;
* Control+[Equals](keyEquiv_en.html#bs1): Displays the list of open tabs in a menu that lets you select the chosen tab;  

<a name="tags">

### Adding And Removing Priority Tags: Shift+ digit On The Alphanumeric Keyboard 

This feature allows you to mark a message as important or to do, for instance. Next, the quick filter bar will display only messages with one or more tags. For example, only important messages in the message list are shown;

To verify which tags are already placed on a message, press Alt+0 on the alphanumeric keyboard. 

To add or remove a tag, press Shift+ number 1 to 9; 

<a name="qfb">

### Quick Filter Bar (Letter F Or Control+Shift+K) 

* letter F or Control+Shift+K: Displays the message quick filter bar in the current folder.
* Keyword filtering: Enter a keyword and press Tab to scroll through the filtered list using the arrow keys;
* The down arrow key from the keyword edit box gives you access to the following options list: 

    * 1: Keep filters when changing folders? c
    * 2: Show only unread messages u
    * 3: Show only tracked messages s
    * 4: Show only messages from persons listed in my address book d
    * 5: Show only messages with tags t
    * 6 : Show only messages with attachments a
    * etc.

* Press Enter to enable or disable one or several of the mentioned criteria;
* Alt+End or Alt+[Equals](keyEquiv_en.html#bs1): Allows you to hear a summary of active filters and the number of filtered messages. These two shortcuts also work within the message list, not just within the quick filter bar;
* When a quick filter is active, a WAV audio file is played when the list or tab to which it belongs is focused. The sound resembles a breath;
* The file filter.wav is located in the folder:
"%appdata%\\NVDA\\TB+sounds"
You can place a sound to your liking as long as your file is called: filter.wav. After this file change, NVDA must be restarted; 

<a name="tagFilter">

#### Filtering By Tag 

When the focus is placed on the edit field of the Quick Filter bar:

*  Press Down Arrow until you hear "tags" and press Enter to check this option;
*  Press the Tab key at that point to move to the drop-down list of tag filtering modes. For example, if you choose "to do", only messages tagged "to do" will be listed in the message table; 

<a name="colLayout">

### Column Layout (Alt+c) 

The shortcut Alt+c displays a dialog that lets you change the order of the columns in the message list, but also add or remove columns.

To use it, first go to the message list or folder tree view and press Alt+c;

The column layout dialog appears. It consists of the list of columns as well as the "Help", "Columns" and "Close" buttons.

The "columns..." button     displays Thunderbird's native "Choose Columns to Display" menu  

When you are in the column list, the following keyboard shortcuts are available:

* Left arrow: Displays the checkbox menu called "Choose columns to display". This shortcut corresponds to the "Columns..." button;
* Space: To move the selected column, press Space, go to another column and press Space again to place the column there. This is similar to a cut and paste operation;

You can also use the following direct movement shortcuts:

* Control+Up or Control+Down Arrow: Moves the selected column up or down one step;
* Control+Home or Control+End: Moves the selected column to the top or bottom of the list;
* Control+Page up or Control+Page down: Moves the selected column up or down three steps;

To perform such moves, the columns are actually displaced by drag and drop with the mouse. A one-millisecond beep is heard every 10 pointer movements;

When the "Choose the columns to display" menu is present, you can use the following keyboard shortcuts:

* Right arrow: Displays the column layout dialog;
* Space: Checks or unchecks the selected column in the menu. The Enter key performs the same action;

With the left and right arrows, it is therefore very easy to switch between the menu for choosing columns and the column layout dialog;

<a name="smartReply">

### SmartReply: Reply To All Mailing Lists By Pressing Control+r 

If you're one of those who forget to press Control+Shift+l to reply to a mailing list like GoogleGroups, this feature will save you from privately replying to the sender of a message without realizing it. 

You can always press Control+r as follows:

* Through a single keystroke: in order to reply to the list;
* Through a double keystroke: in order to reply privately to the sender of the message;
* Through a single keystroke to reply to the sender of a message which does not come from a list.

Notes: 

The use of single or double keystrokes is possible with GoogleGroups, Framalistes and FreeLists.

When using a single keystroke, with one of these three mailing lists, you will hear "to the list" before the write message window opens. 

You should also not use the "Reply All" command to reply to a list so that the sender does not receive your reply privately; 

And finally, if you want to return to the usual Control+r function:

* Press Shift+[Grave](keyEquiv_en.html#aboveTab) to display the Options menu;
* Select "Deactivations for Chichi and for Thunderbird+ sub-Menu";
* Press Enter to uncheck "Message list: no SmartReply";

### Hotkeys A, J, M Spoken

* a: Archives the selected message, announcing this. Press Control+z to cancel the operation;
* j : marks the message as spam, announcing this;
* Shift+j : marks the message as acceptable, announcing this;
* m : Marks selected messages as unread. Shift+m marks them as read; 

<a name="folderTree">

## Folder Tree view

<a name="unreadFolders">

### Quick Navigation Of Folders Containing Unread Messages (Alt+Down Arrow, Alt+Up Arrow) 

When in the folder tree view, you can press:

* Alt+down arrow: to go to the next folder with unread messages;
* Alt+up arrow: to go to the previous folder with unread messages;
* Space, Chichi not installed: If the selected folder contains unread messages, selects the first unread message in the list;
* Space, Chichi installed: same function except that If the folder contains no unread messages, Chichi will display the list of unread folders.
By pressing Enter on an unread folder in this list, the first unread message in that folder will be activated in the message list; <br>
This lets you quickly know which folders have received messages before deciding which one you wish to start reading first. ;<br>

While on this matter, see also the two dialogs below:

* Filtered Lists dialog of account and folders (F12) 
* List of folders in the main tree view, based on 4 types (F7, NVDA+F7 or Shift+F12)

Note: When there is a large number of folders, Chichi operates instantaneously, unlike these two dialogs; 

<a name="folderDlg">

### Filtered Lists Dialog Of Account And Folders (F12) 

This dialog displays the accounts and their associated folders in two separate lists. You can filter them on the base of a keyword or restrict the folder list to those containing unread messages.

Setting the default view mode:

If you plan to display most of the time folders containing only unread messages, first go to the folder tree view or the message list, then use the shortcut Shift+[Grave](keyEquiv_en.html#aboveTab). In the main window options submenu, choose the item entitled: Show only folders containing unread messages.

Basic use of the dialog:

* From within the main window, press F12 to display the dialog. 
* If you have set the default view to folders containing unread messages, they will show in the list named: Account Folders;
* Otherwise, all folders of all accounts will be included in this list;
* You can move through this list by pressing the first letter of a folder name;
* Note that folders that are not displayed in the tree view will not be included here either. This occurs, for example, when folders belong to a collapsed account in the Accounts and Folders tree view;
* If you have found the folder you are interested in at this point, press Enter on it to select it within the tree view. You can also press Alt+g to simulate a simple left-click on the folder or Alt+d to simulate a simple right-click;


Toggling view modes:

* To recall at anytime which view mode you are in, press the Backspace key (backspace). After hearing the information, press this key again to return to the folder list;
* To toggle the view from "unread folders only" mode to "all folders" mode and vice versa, press F12;
* In the "all folders" mode, the accounts are displayed in the list on the left and the folders of the selected account in the list on the right. To move from one list to the other, use the left or right arrow;
* a virtual account called "All accounts" is selected and the focus is placed in the folder list which includes all the folders of all accounts. For each folder in this list, the account name to which the folder belongs is mentioned; 


Keyword filtering usage:

* Beforehand, you will most likely benefit from switching to "All folders" mode as explained above;
* Below, you can use either the "Page Up" or "Page Down" keys; 
* From within a list, press the "Page Up" key to go up to the filter expression edit field;
* Enter an expression, then validate it using the "Page Down" key to start filtering;
* The results are displayed in the folder list. If no folder is found, you will hear: No results. If you weren't expecting this, you may have forgotten to switch to all folders view mode; 
* Finally, press Enter on the desired folder to select it from the folder tree view. As mentioned before, you can simulate a left-click or right-click on the folder by pressing Alt+g or Alt+d; 

#### Excluding Certain Folders From The List Of Folders Containing Unread Messages 

As stated above, you can exclude seldom or never accessed folders from the list of folders containing unread messages.

All you have to do is rename a folder to exclude by adding a hyphen to the end of its name.

It is necessary to point out here that if the renamed folder is part of a message filter, Thunderbird will automatically modify this filter to reflect this change.


<a name="foldersList">

### List Of Folders In The Main Tree view, Based On 4 Types (F7, NVDA+F7 Or Shift+F12) 

When you are in the folder tree view or message list, this command displays a dialog with a folder list that can have the following four layouts: 

* Containing only unread messages (flat list), Alt+n;
* All folders (flat list), Alt+t;
* Containing only unread messages (entire tree view), Alt+o;
* All folders (entire tree view), Alt+u;


For folders containing unread messages, Drafts and Trash folders and folders with names ending with a hyphen are excluded from the list;

To activate one of these types, you can press the associated keyboard shortcut or Shift+Tab and then use the arrow keys to toggle modes.

The type chosen will be memorized and activated the next time this dialog is displayed;

You can also filter the list by keyword. Press Tab or Alt+e to reach the edit box.

Navigation in a flat list or tree view is done with the up or down arrows as well as by the initial of a folder name;

To activate the selected folder in the main tree view, simply press Enter on it.

Tip: If you were to press Enter on a folder containing unread messages, press Space to select the first unread message in the message table; 

<br>
Note:

Keyboard shortcuts that display this dialog can be removed and another can be added via NVDA's Input Gestures setting dialog. Follow these steps:

* First, bring the Thunderbird window to the foreground;
* Open the NVDA menu and select "Preferences";
* In the submenu, press Enter on: "Input gestures";
* In the dialog that opens press the letter t until you reach: Thunderbird+;
* Press the right arrow to expand this branch;
* Scroll down to the item: "Display the folder list in the main Thunderbird tree view based on several types. Collapsed 2 of 4 level 1" and press right arrow to expand this level;
* Tab to the "Add" button, press space then press an input gesture in the new dialog;
* Press Enter to confirm your choice;
* Back in the gesture list, verify the presence of your new input gesture;
* Close the dialog with the OK button.

<a name="alerts">

## Alerts Made Accessible

For alerts requiring your intervention, the buttons are accessible and navigating them can be done using the arrow keys:

* installation of add-ons for Thunderbird: the "Install" button is selected. Just press Enter on it to continue installing;
* New Thunderbird update: this alert is also accessible;
* Request a read receipt: this can be dismissed via an option in the Shift+[Grave](keyEquiv_en.html#aboveTab) / options menu for the main window;;
* Blocking remote content display in messages: the "Options" button is selected and the following sentence is added to the message: Tip: Open the View menu, scroll down to Message Body and press Enter on Simple HTML in the submenu. Once the proposed settings applied, this alert will show no longer;

For alerts that interfere with message list browsing:

* Alert This is a draft: This useless alert is removed;
* Thunderbird thinks that this message is fraudulent: this announcement is replaced by two short tones of a frequency close to the human voice (200 Hertz). To mark the message acceptable or unwanted, press the [Grave](keyEquiv_en.html#aboveTab) key and select the desired action from the "Alert" submenu;

<a name="tabs">

## Keyboard Shortcuts for Tabs 

Besides new commands, tabs are announced as in this example: Tab 1 of 4, Inbox

* Control+Tab and Control+Shift+Tab: goes to the next or previous tab;
* Control+a number: selects the tab corresponding to its order number in the tab bar. If you press a number greater than the number of open tabs, you will be placed on the last one;
* Control+[Equals](keyEquiv_en.html#bs1): displays the list of open tabs in a menu. Press Enter on a tab name to move to it; 
* Alt+[Equals](keyEquiv_en.html#bs1): Opens the tab bar context menu. It mainly includes the commands: Close the active tab and Close my other tabs;  
* Control+w, Control+Bakspace or Control+F4: closes the active tab; 
* Control+j: opens the "Saved files" tab which groups the attachments and downloads saved on your hard drive;

<a name="tabAddons">

## The Add-ons Tab

This add-on makes it easy to find and install add-ons for Thunderbird.

* In the "Add-ons" tab, enter a module name and press Enter;
* The Thunderbird+ add-on will wait for the search results tab to open and then tries to select the first add-on found;
* More concretely, you can read the [Start With Inbox module installation](#stwInstall) example;

<!-- Translators : fenêtre de rédaction = Write window -->
<a name="writeWnd">
## The Write Window 

When the write window opens, nothing special is noticeable although the following keyboard shortcuts are available:

* Escape: closes the write window;
* Review of address fields: one press on Alt+a digit announces the header, two presses focus the corresponding input field:<br>
Alt+1: Sender: one of your email addresses in your e-mail address list;<br>
Alt+2 : to:<br>
Alt+3: The attachment names. Two presses focus the list of attachments;<br>
The other digits give access to optional headers such as: copy to, blind copy to and reply to;
* [Grave](keyEquiv_en.html#aboveTab): in a message text: displays the following context menu: - Mail toolbar then, in the submenu: Send, Spelling, Attach, Security, Save.<br>
Text formatting and then, in the submenu: (Styles of) Paragraph, Apply or remove bulleted list, Apply or remove numbered list, Fonts, Indents, insert link, image, anchor, horizontal line or table. 

<br>
Note: this menu is reached through one or two [Grave](keyEquiv_en.html#aboveTab) key presses depending on the setting in the write window options menu obtained by pressing Shift+[Grave](keyEquiv_en.html#aboveTab) once or twice;

<a name="spellDlg">
### Spell Check Dialog: F7 

Keyboard shortcuts that limit hand movement have been added. When the focus is on the replacement word edit field, you can use the following keyboard shortcuts:

* Enter: Activates the "Replace" button;
* Shift+Enter: Activates the "Replace All" button;
* Control+Enter: Activates the "Ignore" button;
* Shift+Control+Enter: Activates the "Ignore All" button;
* Alt+Enter: Activates the "Add word to dictionary" button;


To remember these combinations involving the Enter key, Control refers to the "Ignore" action and the presence of Shift indicates "all occurrences".

Moreover, the Alt+up arrow shortcut spells words:

* 1 press spells words at normal speed;
* 2 presses spell words quickly;
* 3 presses copy the misspelled word to the clipboard for analysis in another edit field;

<a name="virtspell">

## Improved spell check mode while typing

<!-- Translators: this section was translated by Google on version 4.7.1, may 08, 2023 -->

Note : this section was translated from French into English by Google ;

Despite the spellings added to the spell check dialog, it is sometimes necessary to close the dialog to hear the context of the mistake in the text. This done, this dialog restarts the spell check from the beginning and stops again on the words that we had voluntarily ignored previously.

Spellchecking while typing avoids these inconveniences but can distract the writer with "Misspelling" announcements.

In order not to be distracted by spelling errors while typing, this checking mode has been improved by adding three keyboard shortcuts:

Before activating them, it is necessary to switch to navigation mode by pressing: NVDA+space;

* w and -shift+w to go to the next and previous error respectively;
* NVDA+F7 to display the list of mispelled words. You just need to press enter on an mispelled word to jump to it in the text;

This mode of operation allows you to disable NVDA announcing mispelled words ;

Before using this improved mode of spell chech while typing, it is necessary to carry out a small configuration.

### Preliminary configuration
1: In Thunderbird, Enable spell check while typing in Settings :

* In the main window, open the Options menu, go down to Settings and press Enter ;
* In the Settings  tab, tab to reach the options search field, enter the word "spell" then press Tab;
* In the results, tabulate then check the box entitled: "Enable spell check while typing";
* Finally close the Settings tab with Control+w or -ctrl+Backspace;


2: Disable reporting of misspellings in NVDA
This setting is optional. If you prefer to hear an announcement about a mispelled word, you can also shorten this announcement by replacing in your pronunciation dictionary "mispelled word" by "misp", for example;

To disable this ad:

* Open the NVDA menu, Preferences then press Enter  on: Settings ;
* In the settings dialog, go to the "Document formatting" category;
* Tab until you hear: "Spelling errors" then press space to uncheck this option;
* Close the dialog by validating on the OK button;


### Using w, -shift+w and NVDA+F7 hotkeys

* Before using these hotkeys, you must first activate browse mode by pressing NVDA+space;
* Then press the letter w to go to the next error or -shift+w to go to the previous error or press NVDA+F7 to select the word to correct from a list;* When the faulty word is selected in the text, You can press the Applications key to display the contextual menu of replacement suggestions;
* You can also easily listen to the sentence that contains the faulty word before proceeding to correct it;
* To manually correct a word, first press NVDA+space to return to form mode;

<a name="menus">

## Thunderbird+ Options And Commands Menus 

<a name="optMenu">

### Options Menu (Shift+[Grave](keyEquiv_en.html#aboveTab)) 

Main window options: 

* Group multiple 'RE' mentions into one: for example, Re: Re: Re: will be changed to 3Re:;
* Remove 'RE' in the subject column s : 
* Delete the colon in the 'RE' mentions: 
* Clean up correspondents' names in the message list: remove numbers and some special characters to make listening to names of correspondents less tiresome;
* Add punctuation to columns: a comma is added to some columns to create a short pause between them when announcing a row in the message list;
* Hide mailing list names: Removes the announcement of mailing list names in brackets or braces for more enjoyable listening when using a different folder for each mailing list. Otherwise, the mailing list name is announced only once if it appears several times in the subject line of a message; 
* Edit the words to hide in message subjects: opens an edit box that lets you add or remove words not to be announced in the subject lines of messages. For example, add * so that *** Spam *** will be announced as Spam;
* Announce 'unwanted' if shown in the 'Unwanted status column: if the "unwanted status" column is present in the message table, this option may or may not be used to announce "Unwanted"; 
* Pressing Space on a folder containing unread messages looks for the first unread message from the beginning of the message list: By default, the script for this option sends the "n" command to select the next unread message in the message list. Thunderbird does not always select the first unread message in the list. If this option is checked, the add-on will select the first unread message in the folder by making a detour that can be heard on some PCs;
* Do not use first-letter navigation in the folder tree view: this option is handy if you use the "Quick folder key navigation" add-on;
* Indirect initials navigation: Displays a folder name edit box as soon as you press a letter or number in the folder tree view. If this option is disabled, you can display this search box by pressing letter z; 
* Ignore receipt requests: If enabled, the receipt request pane will be dismissed when a message is selected in the message list;   
* Do not emulate Shift+F6 with escape: disables the use of the escape key when navigating panels in the main window; 
* Show only folders containing unread in the 'Tree view folders' dialog box a: displays only folders with unread messages each time you open this dialog via the F12 key;
* Separate reading window: do not read the message automatically if this blocks NVDA: By default, when you open a message by pressing Enter from the message list, an uncluttered reading of the message starts when the new window opens. On some computers, if the email account is set to IMAP, NVDA may crash. When this option is checked, the automatic reading is disabled to avoid blockage.  

If you do experience a blockage when you open this window, you can extend the delay before Automatic reading starts. To do this, press Alt+d and type a different value. If you are unable to remove this blockage, then check this option; 

<br>
Options for the write window: 

* Spell check: spell the misspelled word and suggested word: This option changes the announcements in the spell check dialog;
* Enable Spell Check enhancement while typing: The command for this setting does not yet work with NVDA 2022.1;
* The Escape key closes the message being composed;
* Single press to display the context menu, double press to write [Grave](keyEquiv_en.html#aboveTab) or Shift+[Grave](keyEquiv_en.html#aboveTab) or their replacements: this option allows you to display the context menu by pressing the [Grave](keyEquiv_en.html#aboveTab) key which will be more practical if you very rarely type the characters [Grave](keyEquiv_en.html#aboveTab) and Shift+[Grave](keyEquiv_en.html#aboveTab);

<br>
Update options:

This option lets you disable Thunderbird+ automatic updates or re-enable them;

<br>
Deactivations for Chichi and Thunderbird+:

The main purpose of these options is to allow a good cohabitation between Thunderbird+ and Chichi by avoiding duplicate features. But you can use them without Chichi to suit your preferences;

The term "folders" below refers to the folder tree view;

* Folders: Space does not select the next unread message in the list and does not display the list of unread folders d: Chichi does not yet have an autonomous equivalent feature;
* Folders: no navigation by initials d: by activating this option, Chichi will be used. This only works from top to bottom and does not announce the account name to which the activated folder belongs; 
* List messages: Space does not read the message in the preview pane l: if you check this option, it is Chichi that will speak the message in the preview pane. Unlike Thunderbird+, this reading will not be uncluttered. On the other hand, F4 and Alt+down arrow will continue to use Thunderbird+ uncluttered reading; 
* List messages: no SmartReply: disables the reply feature to a mailing list via Control+r on single press or to the sender via Control+r on double press;
* List messages: Do not handle the quick filter bar: Removes access to filtering options via down arrow;
* Main window: Tab does not move to the next pane: this option concerns navigation between the folder tree view, the message list and the message pane of headers;
* Main window: Reset the escape key to its default state. This particularly concerns the navigation between the panes mentioned above;
* Allow Thunderbird to be closed with Control+w or Control+F4: by checking this option, the forementioned two shortcuts close Thunderbird when only one tab is open. This behavior is embarrassing for some people;  

Backing up and restoring settings:

* Back up the current configuration s: Copies the add-on's .ini file to a .inibak file.
* Restore Saved Configuration r: Copies the .inibak file to the .ini and reloads the settings;
* Reset Configuration r: Resets the add-on's default settings. Creates a backup beforehand if none already exists;

<a name="cmdMenu">

### Commands Menu ([Grave](keyEquiv_en.html#aboveTab)) 

* Choose and arrange columns from the message list: Displays the Thunderbird menu with check boxes called "Choose columns to display". When on a column name, press the right arrow to open the column layout dialog;
* Write to the support: in French or in English. This command opens a write window pre-addressed to the add-on's support. This only works if Thunderbird is properly set as your default email client;

<a name="startup">

## Enhanced Thunderbird startup

Natively, after Thunderbird's last closes, it launches on the last active tab and without activating anything, which is rather unpleasant.

To get a comfortable start, there are two add-ons that install directly on Thunderbird:

* Chichi, developed by Yannick: this add-on is recommended because it offers many other accessibility features and ThunderbirdPlus is designed to interact with it;
* Start with inbox: if you don't use Chichi, this module does a good job; 

<a name="chichi">

### With Chichi

To use Chichi, read the Download and Installation section together with the Set the Startup Folder section of the [Chichi WebPage](https://www.rptools.org/Outils-DV/thunderbird-chichi-en.html);

<a name="stwi">

### With Start with inbox

As of October 2022, the latest version of this Thunderbird 102 add-on was 2.5.2.

Characteristics:

* Installation: via a search by its name in the "Add-ons" tab of Thunderbird; 
* Startup folder: always the same, either the inbox folder of the account chosen in the add-on settings or the unified folder;
* Auto-focus: on the last message in the message list or on the "Inbox" folder in the tree view, depending on the setting in the add-on options. The second option is selected by default; 
* Settings: Less easy access. Go to the Add-ons tab, select "Start with inbox" in the list of installed add-ons then press enter on the "Add-on Options" button. This will open a new tab "Settings Start with inbox";  

A drop-down list allows you to choose the email account for which the inbox folder will be selected when Thunderbird starts;  

Three radio buttons will allow you to choose between focusing the last message, the first unread message in the message list or the folder in the tree view;

<a name="stwInstall">

Installation:

* In Thunderbird, open the "Tools" menu and press Enter on: Add-ons and themes;
* In the Add-on Manager page, go to the search field. In browse mode, you can press letter e to reach it quickly;
* Write: Start with Inbox and press Enter;
* If you have Thunderbird+, wait a moment for it to select the add-on you are looking for in the results tab;
* Otherwise, manually select the tab "Start with inbox:: Search:: Add-ons for Thunderbird", for instance. Next, press 3 until you reach the level 3 heading which bears the name of the add-on you have searched for; 
* Using the down arrow, scroll down to the link "Add to Thunderbird" and press Enter on it;
* Follow the procedure then restart Thunderbird;
* If all went well, Thunderbird will open on the main tab and focus the message list;

Set Start with Inbox options:

* Return to the "Add-ons Manager" tab;
* If necessary, leave the search field to be in browse mode;
* Press 3 as many times as required to reach the level 3 heading titled "Start with Inbox in the list of installed add-ons;
* Next, activate the button: Add-on Options. This opens a new tab titled: Start with Inbox, Settings;
* Here's what is displayed by default:

<!-- En anglais : -->

Start with Inbox - Settings 

Please select the account for which its inbox shall be displayed after start of Thunderbird. 

Drop-down list: \<your first email account\>

Select and put the focus on:

clickable radio button not checked: the latest* message.

Clickable radio button not checked the inbox folder in the folder tree view.
radio button checked: the first unread message.

* Definition of "latest": The last message that was put into the inbox (independent from the date of the message).

If the inbox contains no messages, the inbox folder in the folder tree will be selected and focused.

<!-- Translators: for other languages, translate the sentences above into your language like the French tanslation below.

Interprétation en français : 

Start with Inbox - Réglages  ;

Sélectionnez le compte dont  le dossier Courrier entrant  sera affiché au démarrage de Thunderbird ; 

liste déroulante : \<votre premier compte de messagerie\>

Sélectionner puis placer le focus sur :

bouton radio   cliquable non coché :Le dernier message de la liste ;

bouton radio non coché cliquable Le dossier Courrier entrant dans l'arborescence des dossiers ;

bouton radio coché : Le premier message non lu de la liste ;
-->

If the Inbox folder contains no messages, this folder will gain focus in the folder tree view; 

<br>
When you have defined your settings, restart Thunderbird.

<br>
Built-in Thunderbird launcher via AltGr+[Grave](keyEquiv_en.html#aboveTab):

For convenience and speed, you can launch Thunderbird by pressing AltGr+[Grave](keyEquiv_en.html#aboveTab). 

This shortcut is configurable via NVDA's input gesture manager which offers greater freedom to choose modifier keys than Windows shortcuts, limited to AltGr;

Follow these steps to add another input gesture:

* First, bring the Thunderbird window to the foreground;
* Open the NVDA menu and select "Preferences";
* In the submenu, press Enter on: "Input gestures";
* In the dialog that opens press the letter t until you reach: "Thunderbird, Launcher";
* Press the right arrow to expand this branch;
* Scroll down to the item: "Starts Thunderbird" then press right arrow to expand this level;
* Tab to the "Add" button, press space then press an input gesture in the new dialog;
* Press Enter to confirm your choice;
* Back in the gesture list, verify the presence of your new input gesture;
* Close the dialog with the OK button.

Notes:

* The Thunderbird launcher is only intended for the Thunderbird installed version of which Thunderbird.exe paths are predictable. 
* In a 64-bit Windows architecture, this add-on will not launch the 32-bit version of Thunderbird if both 64-bit and 32-bit versions are installed on your system; 

<!-- links section -->

[1]: https://www.nvaccess.org/addonStore/legacy?file=thunderbirdPlus

[2]: https://github.com/RPTools-org/ThunderbirdPlus/

[3]: https://www.rptools.org/?p=8610

[4]: https://www.rptools.org/NVDA-Thunderbird/ThunderbirdPlus_en.html#navpanels

[5]: https://www.rptools.org/NVDA-Thunderbird/changes.php?lg=en

[6]: https://www.rptools.org/NVDA-Thunderbird/toContact.html
