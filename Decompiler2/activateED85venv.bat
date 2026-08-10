echo off

echo Changing working directory to Falcom\ED85.
cd Falcom\ED85

set PYTHONPATH=%~dp0
echo Adding %PYTHONPATH% to PYTHONPATH.

echo Activating Venv.
cmd /k %~dp0.venv\Scripts\activate.bat
