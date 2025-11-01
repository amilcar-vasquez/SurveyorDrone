@echo off
REM filepath: /workspaces/SurveyorDrone/color-detection-drone/run.bat
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv" (
    echo Virtual environment not found. Running setup...
    call setup.bat
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Run the application
echo Starting Color Detection Drone...
python main.py

pause