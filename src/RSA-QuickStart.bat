@echo off
set /p ticker=Enter the ticker symbol: 

REM REPLACE THE PATH BELOW WITH YOUR OWN PATH TO THE PROJECT FOLDER
cd C:\Users\Frost\Desktop\CodingProjects\Auto-StockTrader

python main.py %ticker%

REM Examples of quickstarting with different browsers and profiles
REM Right click on browser-> properties-> target to find the path to the browser
REM Remove 'REM' from the lines below to enable them.

REM set /p open_browsers=Do you want to open browsers? (y/n): 

REM if "%open_browsers%"=="y" (
REM    start msedge.exe --profile-directory="Default"
REM    start brave.exe --profile-directory="Default"
REM    start brave.exe --profile-directory="Profile 1"
REM )
