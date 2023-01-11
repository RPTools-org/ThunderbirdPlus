# thunderbird4.x

import wx
import scriptHandler
import gui
import itertools
import speech
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
import queueHandler
import re
import textInfos
import UIAHandler
import NVDAObjects
from NVDAObjects.IAccessible import IAccessible
import browseMode
import addonHandler,  os, sys
addonHandler.initTranslation()
_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)
import  sharedVars
del sys.path[-1]

clientObject = UIAHandler.handler.clientObject

def isNotExpandable (element: NVDAObjects.NVDAObject) -> bool:
	"""
	Permet de vérifier si l'objet NVDA passé en paramètre est bien un objet ne faisant pas partie d'une arborescence et donc, non réductible/développable.
	@Paramètres :
	@element : L'objet NVDA dont on souhaite s'assurer qu'il ne fait pas partie d'un objet d'arborescence.
	@type element : NVDAObjects.NVDAObject
	@returns : Un booléen confirmant qu'il s'agit bien d'un objet non compris dans une arborescence développable, True si c'est bien le cas, False dansle cas contraire.
	@rtype : bool
	"""
	return not (controlTypes.State.EXPANDED in element.states) and not (controlTypes.State.COLLAPSED in element.states)


class ElementsListDialog (browseMode.ElementsListDialog):

	ELEMENT_TYPES = (
	("withUnread", _("Avec messages &non-lus seulement (liste plate)")),
	("allItems", _("&Tous les dossiers (liste plate)")),
	("treeWithUnread", _("Avec messages n&on-lus seulement (arborescence complète)")),
	("treeWithAllItems", _("To&us les dossiers (arborescence complète)")),
	)

	def initElementType(self, elType):
		super(ElementsListDialog, self).initElementType(elType)
		sel = False
		element = self.document
		if element.role == controlTypes.Role.TABLEROW:
			# Pour rechercher l'objet principal dont le role est PROPERTYPAGE.
			mainObj = element
			while mainObj and mainObj.role != controlTypes.Role.PROPERTYPAGE:
					mainObj = mainObj.parent
			for treeView in mainObj.children:
				if treeView.role == controlTypes.Role.TREEVIEW:
					break
			for item in treeView.children:
				if item.role == controlTypes.Role.TREEVIEWITEM and controlTypes.State.SELECTED in item.states:
					element = item
		items = itertools.chain(self._iterReachableTreeItemsFromItem(self.tree.GetSelection()), self._iterReachableTreeItemsFromItem(self.tree.GetFirstChild(self.treeRoot)[0]))
		for item in items:
			if self.tree.GetItemData(item).item.element == element:
				self.tree.SelectItem(item)
				sel = True
		if not sel:
			self.tree.SelectItem(self.tree.GetFirstChild(self.treeRoot)[0])


class ThunderbirdFolderItemQuickNavItem (browseMode.QuickNavItem):

	def __init__( self , nodeType , document , element = None, UIAElement = None, itemLabel = None):
		self.nodeType = nodeType
		self.document = document
		self.element = element
		self.UIAElement = UIAElement
		self.itemLabel = itemLabel
		super (ThunderbirdFolderItemQuickNavItem, self).__init__(nodeType, document)

	def isChild(self,parent):
		return False

	def report(self,readUnit=None):
		pass

	def moveTo(self):
		clientObject.ElementFromIAccessible(self.element.IAccessibleObject, self.element.IAccessibleChildID).GetCurrentPattern(UIAHandler.UIA_InvokePatternId).QueryInterface(UIAHandler.IUIAutomationInvokePattern).Invoke()
		speech.cancelSpeech()
		queueHandler.queueFunction(queueHandler.eventQueue, self.report)

	@property
	def label(self):
		return self.itemLabel


class ThunderbirdFolderTreeQuickNavItem (ThunderbirdFolderItemQuickNavItem ):

	def isChild(self, parent):
		return int(self.element.IA2Attributes.get("level")) > int (parent.element.IA2Attributes.get("level"))

	@property
	def label (self):
		return self.element.name

class ThunderbirdAllFolderItemsQuickNavIterator (object):

	QuickNavItemClass = ThunderbirdFolderItemQuickNavItem

	def __init__(self, nodeType, document, direction, info):
		self.nodeType = nodeType
		self.document = document
		self.direction = direction
		if info is None:
			self.info = self.document.makeTextInfo(textInfos.POSITION_FIRST)
		else:
			self.info = info

	def iterate(self):
		sharedVars.objLooping = True
		account = None
		itemLabel = ""
		# Pour rechercher l'objet principal dont le role est PROPERTYPAGE.
		mainObj = self.document
		while mainObj and mainObj.role != controlTypes.Role.PROPERTYPAGE:
				mainObj = mainObj.parent
		for treeView in mainObj.children:
			if treeView.role == controlTypes.Role.TREEVIEW:
				break
		for element in treeView.children:
			if element.name is not None and element.role == (controlTypes.Role.TREEVIEWITEM if hasattr (controlTypes, "Role") else controlTypes.ROLE_TREEVIEWITEM):
				if not controlTypes.State.COLLAPSED in element.states:
					if element.IA2Attributes.get("level") == "1":
						account = element
						continue
					if controlTypes.State.EXPANDED in element.states or isNotExpandable(element):
						itemLabel = f"{element.name} {'dans ' if account else ''}{account.name}"
						item = self.QuickNavItemClass(self.nodeType, self.document, element = element, itemLabel = itemLabel)
						yield item
		sharedVars.objLooping = False


class ThunderbirdWithUnreadFolderItemsQuickNavIterator (ThunderbirdAllFolderItemsQuickNavIterator):

	def iterate(self):
		sharedVars.objLooping = True
		regexp = re.compile(r"(?<!-)\s\(▾?\d+\)$", re.I | re.U)
		account = None
		accountLabel = ""
		itemLabel = ""
		# Pour rechercher l'objet principal dont le role est PROPERTYPAGE.
		mainObj = self.document
		while mainObj and mainObj.role != controlTypes.Role.PROPERTYPAGE:
				mainObj = mainObj.parent
		for treeView in mainObj.children:
			if treeView.role == controlTypes.Role.TREEVIEW:
				break
		for element in treeView.children:
			if element.name is not None and element.role == (controlTypes.Role.TREEVIEWITEM if hasattr (controlTypes, "Role") else controlTypes.ROLE_TREEVIEWITEM):
				if element.IA2Attributes.get("level") == "1":
					if not controlTypes.State.COLLAPSED  in element.states:
						account = element
				if all (not element.name.startswith(x) for x in (_("Brouillons"), _("Envoyés"), _("Archives"), _("Corbeille"))) and not element.name.endswith("-") and regexp.search(element.name):
					itemLabel = f"{element.name} {'dans ' if account else ''}{account.name}"
					item = self.QuickNavItemClass(self.nodeType, self.document, element=element, itemLabel = itemLabel)
					yield item
		sharedVars.objLooping =False


class ThunderbirdAllFolderTreeQuickNavIterator (ThunderbirdAllFolderItemsQuickNavIterator):

	QuickNavItemClass = ThunderbirdFolderTreeQuickNavItem 

	def iterate(self):
		sharedVars.objLooping = True
		# Pour rechercher l'objet principal dont le role est PROPERTYPAGE.
		mainObj = self.document
		while mainObj and mainObj.role != controlTypes.Role.PROPERTYPAGE:
				mainObj = mainObj.parent
		for treeView in mainObj.children:
			if treeView.role == controlTypes.Role.TREEVIEW:
				break
		for element in treeView.children:
			if element.role == (controlTypes.Role.TREEVIEWITEM if hasattr (controlTypes, "Role") else controlTypes.ROLE_TREEVIEWITEM) and element.name is not None:
				if not controlTypes.State.COLLAPSED in element.states:
					item = self.QuickNavItemClass(self.nodeType, self.document, element = element)
					yield item
		sharedVars.objLooping = False


class ThunderbirdWithUnreadFolderTreeQuickNavIterator (ThunderbirdAllFolderTreeQuickNavIterator):

	def iterate(self):
		sharedVars.objLooping = True
		regexp = re.compile(r"(?<!-)\s\(▾?\d+\)$", re.I | re.U)
		# Pour rechercher l'objet principal dont le role est PROPERTYPAGE.
		mainObj = self.document
		while mainObj and mainObj.role != controlTypes.Role.PROPERTYPAGE:
				mainObj = mainObj.parent
		for treeView in mainObj.children:
			if treeView.role == controlTypes.Role.TREEVIEW:
				break
		for element in treeView.children:
			if element.role == (controlTypes.Role.TREEVIEWITEM if hasattr (controlTypes, "Role") else controlTypes.ROLE_TREEVIEWITEM) and element.name is not None:
				if all (not element.name.startswith(x) for x in (_("Brouillons"), _("Envoyés"), _("Archives"), _("Corbeille"))) and not element.name.endswith("-"):
					if controlTypes.State.EXPANDED in element.states or (isNotExpandable(element) and regexp.search(element.name)) or ((controlTypes.State.COLLAPSED if hasattr(controlTypes, "State") else controlTypes.STATE_COLLAPSED) in element.states and int(element.IA2Attributes.get("level")) > 1 and regexp.search(element.name)):
						item = self.QuickNavItemClass(self.nodeType, self.document, element = element)
						yield item
		sharedVars.objLooping = False


class FoldersListItem (IAccessible):

	passThrough = True

	def _iterNodesByType(self,nodeType,direction="next",pos=None):
		if nodeType== "withUnread":
			return ThunderbirdWithUnreadFolderItemsQuickNavIterator (nodeType, self, direction, pos).iterate()
		if nodeType == "allItems":
			return ThunderbirdAllFolderItemsQuickNavIterator (nodeType, self, direction, pos).iterate()
		if nodeType == "treeWithUnread":
			return ThunderbirdWithUnreadFolderTreeQuickNavIterator(nodeType, self, direction, pos).iterate()
		if nodeType == "treeWithAllItems":
			return ThunderbirdAllFolderTreeQuickNavIterator(nodeType, self, direction, pos).iterate()

	@scriptHandler.script(
	description = _("Afficher la liste des dossiers de l'arborescence principale de Thunderbird, selon plusieurs types."),
	gestures = ["kb:nvda+f7", "kb:f7", "kb:shift+f12"],
	category = sharedVars.scriptCategory
	)
	def script_elementsList(self,gesture):
		def run():
			gui.mainFrame.prePopup()
			d = ElementsListDialog(self)
			d.ShowModal()
			d.Destroy()
			gui.mainFrame.postPopup()
		wx.CallAfter(run)
