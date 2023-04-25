@echo off
set /p ticker=Enter the ticker symbol: 

REM REPLACE THE PATH BELOW WITH YOUR OWN PATH TO THE PROJECT FOLDER
cd C:\Users\Frost\Desktop\CodingProjects\Auto-StockTrader

python main.py %ticker%

REM Examples of quickstarting with different browsers and profiles
REM Right click on browser-> properties-> target to find the path to the browser

REM start msedge.exe --profile-directory="Default"
REM start brave.exe --profile-directory="Default"
REM start brave.exe --profile-directory="Profile 1"
