@echo off
setlocal

echo Instalando PyInstaller...
py -m pip install -r requirements.txt
if errorlevel 1 goto :error

echo.
echo Compilando RenPy Tools...
py -m PyInstaller --noconfirm --clean --onefile --windowed --name "RenPy Tools" RenPy_Tools.py
if errorlevel 1 goto :error

echo.
echo ==========================================
 echo Compilacion terminada correctamente.
echo El ejecutable esta en: dist\RenPy Tools.exe
echo ==========================================
pause
exit /b 0

:error
echo.
echo Ocurrio un error durante la compilacion.
pause
exit /b 1
