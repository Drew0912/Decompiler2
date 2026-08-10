echo off

set Decompiler2Path=%~dp0..\..\

set PYTHONPATH=%Decompiler2Path%
echo Adding %PYTHONPATH% to PYTHONPATH.

echo Activating Venv.
cmd /k %Decompiler2Path%.venv\Scripts\activate.bat
