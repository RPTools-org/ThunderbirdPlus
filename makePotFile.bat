@echo off
call scons pot
del *.pyc
del .sconsign.dblite
set /p pr=Appyez sur Entree pour fermer
