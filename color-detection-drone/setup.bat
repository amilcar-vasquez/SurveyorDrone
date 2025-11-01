@echo off
REM filepath: /workspaces/SurveyorDrone/color-detection-drone/setup.bat
echo Setting up Color Detection Drone environment...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate.bat

REM Upgrade pip
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install PyQt5==5.15.9
pip install opencv-python==4.8.1.78
pip install numpy==1.24.3
pip install ultralytics==8.0.196
pip install Pillow==9.5.0

echo Setup complete! Run 'run.bat' to start the application.
pause