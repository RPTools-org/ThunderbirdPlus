#-*- coding:utf-8 -*
# thunderbird+/appModules/virtualErrors.

from virtualBuffers import gecko_ia2 # Pour les besoins de l'ajout d'un mode de navigation parmi les erreurs d'orthographe lors de la rédaction d'un message.
import speech
import queueHandler
import textInfos
import winUser
import mouseHandler
import api
from NVDAObjects.behaviors import EditableTextWithAutoSelectDetection, EditableTextWithSuggestions						
import browseMode
import treeInterceptorHandler

def hasError(info: textInfos.TextInfo)-> bool:
	"""
	Vérifie si le mot sous le curseur de navigation comporte une erreur.
	paramètres :
	@param info : Position de l'objet TextInfo comportant le mot à analyser.
	@type info : textInfos.TextInfo
	@returns : Un booléen True ou False selon la détection ou pas d'une erreur dans lemot.
	@rtype : bool
	"""
	i = 0
	pos = info.copy()
	fields = pos.getTextWithFields()
	fields.reverse()
	for item in fields:
		if isinstance(item, textInfos.FieldCommand) and isinstance(item.field, textInfos.FormatField):
			i += 1
			if item.field.get("invalid-spelling") and i < 2:
				return True
	return False


class ElementsListDialog(browseMode.ElementsListDialog):
	ELEMENT_TYPES = (
		# On ne prend en charge que les erreurs.
		# Ajoutons donc notre item pour les erreurs.
		("error", _("&errors")),
	)


class ThunderbirdEditTextInfoQuickNavItem (browseMode.TextInfoQuickNavItem):

	def moveTo (self):
		super (ThunderbirdEditTextInfoQuickNavItem, self).moveTo()
		if "error" in self.itemType:
			speech.cancelSpeech()
			try:
				p=api.getReviewPosition().pointAtStart
			except (NotImplementedError, LookupError):
				p=None
			if p:
				x=p.x
				y=p.y
			else:
				try:
					(left,top,width,height)=api.getNavigatorObject().location
				except:
					pass
				x=left+(width//2)
				y=top+(height//2)
			winUser.setCursorPos(x,y)
			mouseHandler.executeMouseMoveEvent(x,y)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTDOWN, 0, 0, None, None)
			winUser.mouse_event(winUser.MOUSEEVENTF_LEFTUP, 0, 0, None, None)
			queueHandler.queueFunction(queueHandler.eventQueue, self.report)

	@property
	def label (self):
		# Méthode qui permet de libeller l'item dans la liste des éléments accessibles avec NVDA+F7.
		if "error" in self.itemType: # Si self.itemType comporte "error", nous avons à faire à des erreurs.
			return self.textInfo.text # Le mot comportant l'erreur sera affiché dans le dialogue ouvert par NVDA + F7.


class ThunderbirdDocumentNodesQuickNavIterator(object):

	def __init__(self, nodeType, document, direction, info):
		self.inElementsList = False
		self.gen1 = None
		self.gen2 = None
		self.nodeType = nodeType
		self.document = document
		self.direction = direction
		if info is not None:
			self.pos = info.copy()
		else:
			self.pos = document.makeTextInfo(textInfos.POSITION_FIRST)
			self.inElementsList = True

	@property
	def checkIteration(self):
		if self.inElementsList:
			try:
				item = next ((i for i in self.document._iterNodesByAttribs(attribs= {}, direction = "next", pos = self.pos, nodeType = self.nodeType)))
			except StopIteration:
				return False
		try:
			self.gen1 = (i for i in self.document._iterNodesByAttribs(attribs= {}, direction = "previous", pos = item.textInfo, nodeType = self.nodeType))
		except:
			return False
		try:
			self.gen2 = (i for i in self.document._iterNodesByAttribs(attribs= {}, direction = "next", pos = self.pos, nodeType = self.nodeType))
		except:
			return False
		return True

	def iterate(self):
		"""
		Cette méthode permet d'itérer parmi les éléments, selon chaque type d'item.
		"""
		if self.inElementsList and self.checkIteration:
			for item in browseMode.mergeQuickNavItemIterators([self.gen1, self.gen2]):
				if hasError (item.textInfo):
					# L'emplacement de l'objet TextInfo comporte bien une erreur.
					info = item.textInfo.copy() # On récupère l'item pour pouvoir l'atteindre.
					item = ThunderbirdEditTextInfoQuickNavItem (self.nodeType, self.document, info)
					# On génère l'item, car nous sommes dans une méthode qui va créer un générateur d'items.
					yield item		
		else:
			for item in self.document._iterNodesByAttribs(attribs= {}, direction = self.direction, pos = self.pos, nodeType = self.nodeType):
				if hasError (item.textInfo):
					# L'emplacement de l'objet TextInfo comporte bien une erreur.
					info = item.textInfo.copy() # On récupère l'item pour pouvoir l'atteindre.
					item = ThunderbirdEditTextInfoQuickNavItem (self.nodeType, self.document, info)
					# On génère l'item, car nous sommes dans une méthode qui va créer un générateur d'items.
					yield item		

class ThunderbirdEditTreeInterceptor (gecko_ia2.Gecko_ia2):

	ElementsListDialog = ElementsListDialog # On ajoute notre classe filtrant les éléments à afficher dans NVDA + F7.

	def _iterNodesByType(self,nodeType,direction="next",pos=None):
		# Cette méthode doit retourner un générateur de tous les items à atteindre en mode navigation, selon chaque type (liens, titres, etc.).
		# Elle permet aussi de générer la liste des éléments que l'on obtient avec NVDA + F7, en fonction du type choisi.
		if nodeType == "error":
			# On retourne notre générateur d'items, selon les types que nous prenons en charge actuellement.
			return ThunderbirdDocumentNodesQuickNavIterator(nodeType, self, direction, pos).iterate()
		return super (ThunderbirdEditTreeInterceptor, self)._iterNodesByType(nodeType, direction, pos)


class ThunderbirdEditDocument (EditableTextWithAutoSelectDetection, EditableTextWithSuggestions):
	# classe insérée dans chooseoverlay
	treeInterceptorClass = ThunderbirdEditTreeInterceptor
	shouldCreateTreeInterceptor = False # On évite de se retrouver automatiquement en mode formulaire.
