#-*- coding:utf-8 -*
objLooping = False
oCurFrame = None
groupingIdx = 35 # index of child object of role grouping in the foregroundObject children  
curFrame = ""
curTab = "init2"
prevObj = ""
chichi = None
menuCommands = {} # parallel to some menu items
FTnoNavLetter =FTnoSpace = TTnoSpace = TTnoFilterBar = False
useKeyNav = True
directKeyNav = True
lockEditMenu = None
scriptCategory = "Thunderbird+ 4"
virtualSpellChk = False
delayReadWnd = 99
testMode = False
debug = False
debugLog = ""

import inspect
oSettings = None # options menu
import menuSettings
import controlTypes
# controlTypes module compatibility with old versions of NVDA
if not hasattr(controlTypes, "Role"):
	setattr(controlTypes, "Role", type('Enum', (), dict(
	[(x.split("ROLE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("ROLE_")])))
	setattr(controlTypes, "State", type('Enum', (), dict(
	[(x.split("STATE_")[1], getattr(controlTypes, x)) for x in dir(controlTypes) if x.startswith("STATE_")])))
	setattr(controlTypes, "role", type("role", (), {"_roleLabels": controlTypes.roleLabels}))
# End of compatibility fixes
import globalVars
from ui import message

def initSettingsMenu(appMod) :
	global oSettings
	oSettings = menuSettings.Settings(appMod)

def setLooping(value) :
	global objLooping, debug, debugLog
	objLooping = value
	if not debug : return
	lastFunction = inspect.stack()[1][3]
	debugLog = debugLog + "setLooping fonction :{0}, valeur : {1}".format(lastFunction, str(value)) + "\n"

def log(o, msg="Objet", withStep=False):
	global debugLog
	if withStep :
		step = "step " + str(globalVars.TBStep) + " "
		curFunc = inspect.stack()[1][3] 
		prevFunc = inspect.stack()[2][3]
		lastFunction = " fonk {0}, {1} : ".format(curFunc, prevFunc)
	else :
		step = lastFunction = ""
	if not o : 
		debugLog = debugLog + step + msg + " : objet None, " + lastFunction + "\n"
		return
	foc =  ("focused, " if hasattr(o, "hasFocus") and o.hasFocus else "")
	nm = (str(o.name) if hasattr(o, "name") else "")
	if hasattr(o, "IA2Attributes") :
		ID = str(o.IA2Attributes.get("id"))
	else : ID = ""
	t =  foc + " : {0}, ID : {1}, childCount : {2} \nName : {3}".format(str(o.role), ID, o.childCount, nm)
	debugLog = debugLog + step + lastFunction + msg +  t + "\n"

def debugMess(o, msg="Objet") :
	lastFunc = inspect.stack()[1][3]
	foc =  ("focused, " if o.hasFocus else "")
	sel = (", selected" if controlTypes.State.SELECTED in o.states else "non selected")
	nm = str(o.name)
	ID = str(o.IA2Attributes.get("id"))
	t =  foc + sel + " : role : {0}, ID : {1}, childCount : {2}name : {3}".format(o.role, ID, o.childCount, nm[:15])
	message(lastFunc + msg + t )
