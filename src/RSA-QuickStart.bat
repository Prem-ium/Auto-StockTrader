@echo off
set /p ticker=Enter the ticker symbol: 

REM REPLACE THE PATH BELOW WITH YOUR OWN PATH TO THE PROJECT FOLDER
cd C:\Users\Frost\Desktop\CodingProjects\Auto-StockTrader

python main.py %ticker%
