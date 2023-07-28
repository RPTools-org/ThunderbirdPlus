# -*- coding:utf-8 -*
#A part of NonVisual Desktop Access (NVDA)
# Thunderbird+ 4.x

from NVDAObjects.IAccessible import getNVDAObjectFromPoint
import winUser
from winUser import *
import api
import speech
from ui import message
from keyboardHandler import KeyboardInputGesture
from time import sleep
import wx, config
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
import addonHandler,  os, sys
import translation, utis, sharedVars
import core
from tones import beep
from speech import speakSpelling 
import scriptHandler
import globalCommands
translation.initTranslationWithEnglishFallback()

_curAddon=addonHandler.getCodeAddon()
sharedPath=os.path.join(_curAddon.path,"AppModules", "shared")
sys.path.append(sharedPath)

def PutWindowOnForeground(hwnd, sleepNb, sleepTime):
	try:
		setForegroundWindow(hwnd)
	except:
		pass
	for i in [sleepTime]*(sleepNb-1):
		sleep(i)
		if winUser.getForegroundWindow() == hwnd:
			return True 
	KeyboardInputGesture.fromName("alt+Tab").send()
	sleep(sleepTime)
	if winUser.getForegroundWindow() == hwnd:
		return true
	return False

def SendKey(	keys) :
	KeyboardInputGesture.fromName(keys).send()	


class FoldersMessagesList(wx.Dialog):
	global avecNonLus, avecFiltre, index0 , oDeb, withUnread, cocheEnterInit
	_timer=None
	cocheEnterInit= config.conf["keyboard"]["speechInterruptForEnter"]
	avecFiltre=False  
	filtre0=""
	filtre1=""

	def __init__(self, parent,ID, title, closeIfInactive): 
		super(FoldersMessagesList, self).__init__(parent, ID,title) 
		self.closeIfInactive = closeIfInactive
		self.destroyed = False
		# config.conf["keyboard"]["speechInterruptForEnter"]=False
		self.doGui()

	def doGui(self):		
		panel = self
		panelSizer = wx.GridBagSizer (6,4)
		self.taggedObjectsCB = wx.CheckBox(panel, wx.ID_ANY, label =_("Show only folders with &unread"))
		self.taggedObjectsCB.SetValue(avecNonLus)   #<<<< False  True
		panelSizer.Add(self.taggedObjectsCB, pos=(0,0), span= (1,1), flag=wx.EXPAND|wx.LEFT|wx.TOP,border=10)
		self.rechercheLabel=wx.StaticText(panel, wx.ID_ANY, label= _("&Filter expression:"))
		panelSizer.Add(self.rechercheLabel,pos=(0,1), span= (1,1), flag=wx.EXPAND|wx.LEFT|wx.TOP,border=15)
		self.zoneRecherche = wx.TextCtrl(panel, wx.ID_ANY)
		self.zoneRecherche.Value ="" 
		panelSizer.Add(self.zoneRecherche, pos=(0,2), span= (1,1), flag=wx.EXPAND|wx.TOP,border=10)
		self.typeLabel = wx.StaticText(panel, wx.ID_ANY, label= _("Email &accounts: "))
		panelSizer.Add(self.typeLabel, pos=(1,0), span= (1,1), flag=wx.EXPAND|wx.LEFT,border=15)
		#the list boxes
		self.lbComptes = wx.ListBox(panel, wx.ID_ANY, style = wx.LB_SINGLE, size = (260, 400))
		if len(self.getlisteComptes())>0:   
			self.lbComptes.SetItems([obj[0] for obj in self.getlisteComptes()])  
			self.lbComptes.Select(0) 
		panelSizer.Add(self.lbComptes, pos=(2,0), span= (5,1), flag=wx.EXPAND|wx.LEFT|wx.BOTTOM, border=10)	
		self.elemLabel = wx.StaticText(panel, wx.ID_ANY, label= _("Account &Folders : "))
		panelSizer.Add(self.elemLabel, pos=(1,1), span= (1,1), flag=wx.EXPAND|wx.LEFT,border=15)
		self.lbDossiers = wx.ListBox(panel, wx.ID_ANY,  style = wx.LB_SINGLE, size = (400, 400))
		if len(self.getlisteDossiers())>0:   
			self.lbDossiers.SetItems([obj[0] for obj in self.getlisteDossiers()])
			self.lbDossiers.Select(0) 
		panelSizer.Add(self.lbDossiers, pos=(2,1), span=(5,2), flag=wx.EXPAND|wx.LEFT|wx.BOTTOM,
			border=10)
		# the buttons
		self.rightClickButton=wx.Button(panel, wx.NewId(), label = _("Single &right-click"), size = (120, 30)) 
		self.leftClickButton=wx.Button(panel, wx.NewId(), label = _("Single &left-click"), size = (120, 30))
		self.infosButton=wx.Button(panel, wx.NewId(), label = _("&Informations"), size = (120, 30))
		self.leftClickButton.SetDefault()
		self.cancelButton =wx.Button(panel,wx.ID_CANCEL, size = (120, 30))
		panelSizer.Add(self.rightClickButton,(2,3),flag=wx.ALL, border = 10)
		panelSizer.Add(self.leftClickButton,(3,3),flag=wx.ALL, border = 10)  
		panelSizer.Add(self.infosButton,(4,3),flag=wx.ALL, border = 10)  
		panelSizer.Add(self.cancelButton,(6,3),flag = wx.ALL, border= 10)
		panel.SetSizerAndFit(panelSizer)

		# the events 
		self.taggedObjectsCB.Bind(wx.EVT_CHECKBOX,self.onCaseChange)  
		self.zoneRecherche.Bind(wx.EVT_KEY_DOWN, self.onKeydown0)
		self.lbComptes.Bind(wx.EVT_SET_FOCUS,self.onObjectTypeListBoxFocus)  
		self.lbComptes.Bind(wx.EVT_LISTBOX,self.onElementComptesChange)  
		self.lbComptes.Bind(wx.EVT_KEY_DOWN, self.onKeydown1)	
		self.lbDossiers.Bind(wx.EVT_KEY_DOWN, self.onKeydown2)	
		self.leftClickButton.Bind(wx.EVT_BUTTON, self.onLeftMouseButton) 
		self.leftClickButton.Bind(wx.EVT_KEY_DOWN, self.onKeydownButton)  
		self.rightClickButton.Bind(wx.EVT_BUTTON, self.onRightMouseButton)	
		self.rightClickButton.Bind(wx.EVT_KEY_DOWN, self.onKeydownButton) 	
		self.infosButton.Bind(wx.EVT_BUTTON, self.onKeydownButton0) 		
		self.infosButton.Bind(wx.EVT_KEY_DOWN ,self.onKeydownButton)
		self.cancelButton.Bind(wx.EVT_BUTTON,self.onCancelButton)
		self.cancelButton.Bind(wx.EVT_KEY_DOWN, self.onKeydownButton)
		self.Bind(wx.EVT_ACTIVATE, self.onActivate)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.lbDossiers.SetFocus()
		self.sayNumberOfElements()

	def sayNumberOfElements(self):
		def callback (count):
			self._timer=None
			try : 
				if not self.lbComptes.HasFocus and not self.lbDossiers.HasFocus : return
			except RuntimeError: return
			if count == 0 :
				msg = _("no element")
			elif count == 1 :
				msg = _("1 element")
			else :
				msg = _("%s elements") % str(count) 
			message(msg)

		if self._timer is not None: self._timer.Stop()
		self._timer = wx.CallLater(200,callback, self.lbDossiers.Count) 

	def getPositionXY (self):
		if self.lbComptes.HasFocus(): 
			beep (440,75)
			return		
		global oDeb
		# nb,iSelect,iSelect0,y0,iSelect1,y1,iSelect2,y2=oDeb.childCount-1,0,0,0,0,0,0,0  
		nb,iSelect,iSelect0,iSelect1,y1,iSelect2,y2=oDeb.childCount-1,0,0,0,0,0,0 
		#iSelect1: premier dossier visible  ;  iSelect2: dernier dossier visible
		o=self
		iSelect0 =(0 if self.getlisteDossiers0()[0][2]==False else nb) # 0 si premier dossier non visible
		iSelect2 =(0 if self.getlisteDossiers0()[nb-1][2]==False else nb) # 0 si dernier dossier non visible
		if iSelect2==0 : # fin non visible
			iSelect=nb-1
			while iSelect and self.getlisteDossiers0()[iSelect][2]==False :
				iSelect-=1
			iSelect2=iSelect-1 # -1 pour barre d'état?
			y2=int(self.getlisteDossiers0()[iSelect2][1][1])+8
		if iSelect0 ==0 : # début non visible
			iSelect= 0 
			while iSelect< 60 and self.getlisteDossiers0()[iSelect][2]==False :
				iSelect+=1
			iSelect1=iSelect 
			y1=int(self.getlisteDossiers0()[iSelect1][1][1])+8
		else :
			y1=int(self.getlisteDossiers0()[0][1][1])+8

		itemSelected=self.lbDossiers.GetSelection() 
		y =int(self.getlisteDossiers()[itemSelected][1][1])+8
		EstVisible=( True if y>=y1 and y<=y2 else False)
		if EstVisible: 
			locat=self.getlisteDossiers()[itemSelected][1]
		else:
			# message ("hors ecran")
			# self.Close()
			nom=self.getlisteDossiers()[itemSelected][0].split(",")[0]
			if y<y1 : 
				o=getNVDAObjectFromPoint(80,y1)
				if o and o.role!= controlTypes.Role.TREEVIEWITEM : o=o.parent
				o.setFocus()
				while o and not nom== o.name:
					o=o.previous 
					if  (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE) in o.states :
						o.scrollIntoView()
				o.setFocus()
				o.doAction()	
			else :
				o=getNVDAObjectFromPoint(80,y2)
				if o and o.role!= controlTypes.Role.TREEVIEWITEM : o=o.parent
				o.setFocus()
				while o and not nom== o.name:
					o=o.next 
					if  o and (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE) in o.states :
						o.scrollIntoView()
				o.setFocus()
				o.doAction()	
			locat=o.location  
		if locat : 
			xyItem=(int(locat[0])+int(locat[2]/2),int(locat[1])+int(locat[3]/2))	
			return xyItem
		else : 
			return False

	def onClose(self, evt):
		global cocheEnterInit
		config.conf["keyboard"]["speechInterruptForEnter"]=cocheEnterInit
		self.Destroy()
		self.destroyed = True  
		evt.Skip()
		
	def onCaseChange(self, evt): 
		if self.taggedObjectsCB.GetValue(): message (_("Folders with unread, checked"))
		else :message (_("Folders with unread, not checked"))
		self.lbComptes.Clear()
		self.lbComptes.SetItems([obj[0] for obj in self.getlisteComptes() ]) 
		self.lbComptes.Select(0) 
		message (self.getlisteComptes()[self.lbComptes.GetSelection()][0])
		self.lbDossiers.Clear()
		try :
			if  self.getlisteDossiers() :
				self.lbDossiers.SetItems([obj[0] for obj in self.getlisteDossiers() ]) 
				self.sayNumberOfElements()
				self.lbDossiers.SetFocus() 
				self.lbDossiers.Select(0) 
			else :
				 self.lbComptes.SetFocus() 
				 return message (_("No result."))
		except : 
			self.lbComptes.SetFocus() 
			return message (_("No result."))
		evt.Skip()  		 

	def onObjectTypeListBoxFocus(self,evt):
		self.sayNumberOfElements()

	def onElementComptesChange(self, evt): 
		self.lbDossiers.Clear()
		self.lbDossiers.SetItems([obj[0] for obj in self.getlisteDossiers() ]	)	
		self.sayNumberOfElements()
		# self.objectTypeHasChanged = True

	def changeSelectionComptes(self): 
		try :
			if self.lbDossiers.GetSelection() :
				index0=self.lbDossiers.GetSelection()
				obj=self.getlisteDossiers()[index0][0].split("dans ")[-1]
				if obj[:1]==" " : obj=obj[1:]
				self.lbComptes.Select(self.getlisteComptes().index(obj)) 
		except: pass  #return

	def onKeydownButton0(self, evt):
		if self.taggedObjectsCB.GetValue() : message(_("unread folders view")) 
		else :message(_("All folders view"))
		st= self.zoneRecherche.GetValue()
		if st=="": message(_("no filter expression"))
		else :
			message(_("filter expression : %s") %st)
			if len(st)>1 :speakSpelling (st) 
		wx.CallAfter(self.sayNumberOfElements)
		return
		evt.Skip()	

	def onKeydownButton(self, evt):
		# keyCode= evt.GetKeyCode()
		keyCode= evt.KeyCode
		if keyCode ==68 and self.lbDossiers.HasFocus(): 
			core.callLater(200,SendKey ,"Alt+d")			
			return 
		if keyCode ==71 and self.lbDossiers.HasFocus(): 
			core.callLater(200,SendKey ,"Alt+g")			
			return 	
		if keyCode ==73 and self.lbDossiers.HasFocus(): 
			core.callLater(200,SendKey ,"Alt+i")			
			return 			
		if keyCode ==wx.WXK_BACK:   
			core.callLater(200,SendKey ,"Alt+s")			
			return 	
		if keyCode ==wx.WXK_LEFT:   
			core.callLater(200,SendKey ,"Shift+Tab")			
			return 	
		if keyCode == wx.WXK_ESCAPE:
			self.Close()
			return
		evt.Skip()

	def onKeydown1(self, evt): 
		keyCode= evt.KeyCode
		if  keyCode ==wx.WXK_RIGHT :
			if  self.lbComptes.HasFocus(): 
				index0=self.lbDossiers.GetSelection()
				if index0 >0 :
					oldSpeechMode = utis.getSpeechMode()
					utis.setSpeechMode_off()
					speech.cancelSpeech()
					sleep(0.2)
					self.lbDossiers.Select(index0) 
					self.lbDossiers.SetFocus() 
					api.processPendingEvents()
					sleep(0.2)
					utis.setSpeechMode(oldSpeechMode)				
					self.lbDossiers.Select(index0) 
				else :
					if len(self.getlisteDossiers()) : self.lbDossiers.Select(0) 
					self.lbDossiers.SetFocus() 
				return 
		if keyCode ==wx.WXK_LEFT:   
			core.callLater(200,SendKey ,"Shift+Tab")				
			return 		
		if keyCode ==wx.WXK_F12:   
			core.callLater(200,SendKey ,"Alt+n")	
			return 			
		if keyCode in [wx.WXK_F11,wx.WXK_PAGEUP,wx.WXK_PAGEDOWN]:  
			core.callLater(200,SendKey ,"Alt+f")	
			return 		
		evt.Skip()

	def onKeydown0(self, evt): 
		keyCode= evt.KeyCode
		if  keyCode ==wx.WXK_UP: 
			if  self.zoneRecherche.HasFocus() :
				core.callLater(200,SendKey ,"Shift+Tab")
				return	
		if keyCode ==wx.WXK_DOWN:  
			if  self.zoneRecherche.HasFocus() :
				core.callLater(200,SendKey ,"Tab")
				return 
		if keyCode ==wx.WXK_F12:   
			if  self.zoneRecherche.HasFocus() :
				core.callLater(200,SendKey ,"Alt+n")	
				return 		 
		if keyCode in [wx.WXK_F11,wx.WXK_PAGEUP,wx.WXK_PAGEDOWN]: 
			if  self.zoneRecherche.HasFocus() :
				filtre = self.zoneRecherche.GetValue()
				if filtre =="" :
					if keyCode ==wx.WXK_F11 : beep (330, 75) 
					message(_("No expression entered"))
					self.lbDossiers.SetFocus() 
					return 
				self.lbDossiers.Clear()
				if self.getlisteDossiers():
					self.lbDossiers.SetItems([obj[0] for obj in self.getlisteDossiers() ]) 
					self.lbDossiers.Select(0)	
					message (filtre)
					self.sayNumberOfElements()
					self.lbDossiers.SetFocus()
				else : 
					message(_("No results, edit your search."))
				self.changeSelectionComptes()
				return 					
		evt.Skip()		

	def onKeydown2(self, evt):  #lbDossiers
		keyCode=evt.KeyCode
		if config.conf["keyboard"]["speechInterruptForEnter"] : config.conf["keyboard"]["speechInterruptForEnter"] = False
		if  keyCode ==wx.WXK_RIGHT :
			if  self.lbDossiers.HasFocus(): #self.lbComptes.HasFocus() or }
				core.callLater(200,SendKey ,"Tab")
				return		
		if keyCode ==wx.WXK_LEFT:   
			core.callLater(200,SendKey ,"Shift+Tab")
			return 
		if keyCode ==wx.WXK_F12:   
			core.callLater(200,SendKey ,"Alt+n")	
			return 			
		if keyCode in [wx.WXK_F11,wx.WXK_PAGEUP,wx.WXK_PAGEDOWN]: 
			core.callLater(200,SendKey ,"Alt+f")	
			return 			
		evt.Skip()

	def onCancelButton(self, evt):
		global cocheEnterInit
		config.conf["keyboard"]["speechInterruptForEnter"]=cocheEnterInit		
		self.Close()
		evt.Skip()

	def onActivate(self, evt):
		global cocheEnterInit
		config.conf["keyboard"]["speechInterruptForEnter"]=cocheEnterInit			
		if not self.destroyed and self.closeIfInactive and not evt.GetActive():  
			self.Close()
		evt.Skip()

	def onLeftMouseButton(self,event):
		if not self.getPositionXY() : return
		(x,y)=self.getPositionXY()
		self.Close()
		winUser.setCursorPos(x,y)
		mouse_event(MOUSEEVENTF_LEFTDOWN,0,0,None,None)
		sleep(0.1)
		mouse_event(MOUSEEVENTF_LEFTUP,0,0,None,None)

	def onRightMouseButton(self,event):
		if not self.getPositionXY() : return 
		(x,y)=self.getPositionXY()
		self.Close()
		winUser.setCursorPos(x,y)
		mouse_event(MOUSEEVENTF_RIGHTDOWN,0,0,None,None)
		sleep(0.1)
		mouse_event(MOUSEEVENTF_RIGHTUP,0,0,None,None)		
		
	def getlisteComptes(self):
		global oDeb
		avecNonLus = self.taggedObjectsCB.GetValue()  
		locat=None 
		visible=False
		name=""
		l=[] 
		o=oDeb
		max=(1 if avecNonLus else o.childCount)
		l.append((_("All accounts"), o.children[1].location,False))   
		for i in range (1,max) :
			o1=o.children[i]
			if  utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") =="1" : 
				name =o1.name
				locat = o1.location
				visible=(o1 and not (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE)  in o1.states)  			
				l.append((name,locat,visible)) 		
		return l 

	def getlisteDossiers(self):
		global oDeb 
		sharedVars.objLooping = True # évite les biendgestures dans folderTreeItem.py
		filtre1=self.filtre0
		avecNonLus = self.taggedObjectsCB.GetValue()  
		try: 
			filtre1=self.filtre0=self.zoneRecherche.GetValue().lower()
		except :	
			filtre1=False
		locat=None 
		name=""
		lev=0
		idx= 0 
		l0=[] 
		l0.append((0,0))
		o=oDeb
		max=o.childCount
		for i in range (1,max) :
			o1=o.children[i]
			if  utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") =="1" :  
				lev=1 ;idx+=1
				locat = o1.location
				l0.append((idx,i))
		indx=(self.lbComptes.GetSelection()  if self.lbComptes.GetSelection() else 0)
		n1=(1 if (avecNonLus or filtre1 or indx==0) else l0[indx][1]) 
		try :
			n2=(max  if (avecNonLus or filtre1 or indx==0)  else l0[indx+1][1])
		except : n2=max  
		l=[] 
		o=oDeb
		o2=o.children[1]
		for i in range (n1,n2) :
			o1=o.children[i]
			name= o1.name
			if (utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") =="1" ) :
				name=o1.name + _(", Email account")
				o2=o1
			if (avecNonLus and not "(" in o1.name ) or (filtre1 and  not filtre1 in o1.name.lower()) : continue
			if  (utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") !="1") and (indx==0    or (avecNonLus and "(" in o1.name ) or (filtre1 and  filtre1 in o1.name.lower())) :	
				if o2:
					name =o1.name+ _(", in  ") +o2.name
			locat = o1.location
			visible=(o1 and not (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE)  in o1.states) 
			# "- ("  permet d'exclure les dossiers dont le nom se termine par un tiret (dossiers oubliettes)
			if _("Deleted") not in o1.name or _("Drafts") not in o1.name or "- (" not in o1.name :
				l.append((name,locat,visible)) 
			# l.append((name,locat,visible)) 
		sharedVars.objLooping =False
		return l

	def getlisteDossiers0(self):
		global oDeb 
		sharedVars.objLooping = True # évite les biendgestures dans folderTreeItem.py
		filtre1=self.filtre0
		avecNonLus = False  #self.taggedObjectsCB.GetValue()  
		filtre1=False
		locat=None 
		name=""
		lev=0
		idx= 0 
		l0=[] 
		l0.append((0,0))
		o=oDeb
		max=o.childCount
		for i in range (1,max) :
			o1=o.children[i]
			if  utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") =="1" :  
				lev=1 ;idx+=1
				locat = o1.location
				l0.append((idx,i))
		indx=0
		n1=(1 if (avecNonLus or filtre1 or indx==0) else l0[indx][1]) 
		try :
			n2=(max  if (avecNonLus or filtre1 or indx==0)  else l0[indx+1][1])
		except : n2=max  
		l=[] 
		o=oDeb
		o2=o.children[1]
		for i in range (n1,n2) :
			o1=o.children[i]
			name= o1.name
			if (utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") =="1" ) :
				name=o1.name+ _(", Email account")
				o2=o1
			if (avecNonLus and not "(" in o1.name ) or (filtre1 and  not filtre1 in o1.name.lower()) : continue
			if  (utis.getIA2Attribute (o1,attribute_value=False,attribute_name ="level") !="1") and (indx==0    or (avecNonLus and "(" in o1.name ) or (filtre1 and  filtre1 in o1.name.lower())) :	
				if o2:
					name =o1.name+ _(", in  ")+o2.name
			locat = o1.location
			visible=(o1 and not (controlTypes.State.INVISIBLE if hasattr(controlTypes, "State") else controlTypes.STATE_INVISIBLE)  in o1.states) 
			# "- ("  permet d'exclure les dossiers dont le nom se termine par un tiret (dossiers oubliettes)
			if _("Deleted") not in o1.name or _("Drafts") not in o1.name or "- (" not in o1.name :
				l.append((name,locat,visible)) 
			# l.append((name,locat,visible)) 
		sharedVars.objLooping =False
		return l

	def run(cls,withUnreadr): #,cocheEnte
		global oDeb ,avecNonLus, cocheEnterInit  #  oDeb est l'arborescence des dossiers
		avecNonLus=withUnreadr  #withUnread
		# cocheEnterInit=cocheEnter
		cocheEnterInit=config.conf["keyboard"]["speechInterruptForEnter"]
		o = api.getForegroundObject ().simpleFirstChild
		sharedVars.objLooping = True
		while o and o.role!= controlTypes.Role.GROUPING : o=o.next  
		o = o.firstChild.firstChild  
		while o and o.role!= controlTypes.Role.TREEVIEW : o=o.next 
		oDeb=o
		bdd = cls(None,wx.ID_ANY,_("Treeview folders"), True) 
		sharedVars.objLooping = False
		config.conf["keyboard"]["speechInterruptForEnter"]=False
		bdd.CenterOnScreen()
		bdd.Show(True)
		PutWindowOnForeground(bdd.GetHandle(), 4, 0.1) 
	run = classmethod(run)

