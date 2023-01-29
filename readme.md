# Thunderbird+ #

* Authors : Pierre-Louis Renaud, Daniel Poiraud
* URL : [User manual](http://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-en.html) , [Contact in French or English](http://www.rptools.org/Outils-DV/contact.html) ;
* Download :
	* [Stable version][1]
* NVDA Compatibility :
	* Minimum version : 2019.3
	* Last tested version : 2022.1
* Tunderbird compatibility : 102.x versions ; 
* [See source code on GitHub][3]

Note: This add-on is not compatible with the Mozilla Apps Enhancements add-on. If you have the Mozilla Apps Enhancements add-on installed, you must disable or uninstall it before using this one ;

This add-on greatly improves the accessibility, efficiency and comfort of using the Mozilla Thunderbird mail client with NVDA.

* Hearing comfort:
	* "so-and-so requested acknowledgment" alerts can be disabled via an option;
	* "This is a draft" and "Thunderbird thinks this message is fraudulent" alerts are simply ignored;
	* Options make it possible to deactivate the announcement of the names of mailing lists, to remove or group the mentions "RE" and to purify the names of the correspondents by removing the numbers and other awkward special characters;
* Improved navigation:
	* Moving to the next panel is done using the TAB key while the escape key allows you to return to the previous panel. This is more comfortable than F6 and Shift+F6.
	* Two dialogs of accounts and their associated folders allow filtering them by keyword or displaying only folders with unread messages;
	* In the folder tree, alt+down arrow and Alt+up arrow allow you to navigate between folders with unread messages;
	* Still in the folder tree, typing a letter or a number selects the next folder whose name begins with the character typed. With the Shift key, the move is from bottom to top. Additionally, the name of the account the folder belongs to is announced;
	* The Space key on a folder with unread messages selects the first unread message in the list;
* In the message list:
	* The choice of columns as well as their arrangement in the list of messages is made accessible through a simple dialog;
	* Consultation of the columns of the list of messages: allows you to listen again, spell or easily copy the name of the sender, the subject or the date of a message by pressing a number on the alphanumeric keyboard: for example, 1 or & announces the sender, 2 presses spells the name and 3 presses copies it to the clipboard;
	* Consultation of the headers of the headers pane displayed with F8: with Alt+a number, 1 press speaks a header containing the addresses of the sender or the recipients, 2 presses opens a dialog allowing them to be copied, 3 presses opens the contextual menu native Thunderbird associated with the header;
	* Clean quick preview of message text with space, Alt+down arrow or F4: large block headers in message quotes are replaced with the phrase "Sender's name wrote". NVDA will also announce "clickable link" instead of the long link address.
	* Quick view of quotes in their chronological order, from bottom to top, via Shift+Space, Alt+up arrow or Shift+F4;
	* Easy access to attachments using the shortcut Alt+pageDown or the number 1 on the alpha-numeric keyboard;
	* Quick filter bar made accessible and priority tag management simplified:
		* It is possible to navigate among Filter options using the vertical arrow keys. The Enter key allows you to check or uncheck an option ;
		* Adding or removing priority tags is done by simply pressing Shift+a number on the alphanumeric keyboard. For example, press 4 to add the tag "To do" to a message. You can then filter the list of messages by tags via the quick filter bar which is now accessible;
* Compose message window:
	* Alt+1 announces Sender, Alt+2 receiver, Alt+3 attachments, etc. Two presses set  the focus on one of these fields;
	* In the spell check dialog:
		* the misspelled word is announced before the suggested word. NVDA+Tab or Alt+up arrow shortcuts announce misspelled and replacement words: 1 tap spells the words at normal speed, 2 taps spells them fast, 3 taps copies the misspelled word to the clipboard for analysis in another edit field;
		* various combinations of the enter key activate the buttons Replace, Replace all, Ignore, Ignore all or Add the word to the dictionary have been added for an increased comfort of this dialog;
* Automatic extension update;
* And many other things that you will discover by reading the [user manual][2] ;


[1]: https://github.com/RPTools-org/ThunderbirdPlus/releases/download/v4.4/ThunderbirdPlus-v4.4-TB102.nvda-addon

[2]: http://www.rptools.org/Outils-DV/NVDA-ThunderbirdPlus-en.html

[3]: https://github.com/RPTools-org/ThunderbirdPlus/