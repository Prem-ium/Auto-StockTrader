@echo off
setlocal

REM set directory variable to the path of the project folder
set directory=

REM Display examples of usage
echo 1. Pass a Stock Ticker as an argument to update all .side files:
echo    Enter: AAPL
echo.
echo 2. Separate multiple tickers with commas:
echo    Enter: NVDA,TSLA,AAPL
echo.

set /p arguments=Enter tickers (comma-separated): 

REM Navigate to the project folder using the directory variable
cd %directory%

python main.py %arguments%

choice /c yn /n /m "Do you want to open browsers? (y/n): " /t 10 /d n
set open_browsers=%errorlevel%

if %open_browsers%==1 (
    echo Attempting to open browsers...

    REM Attempt to open Brave Browser
    if exist "%ProgramFiles%\BraveSoftware\Brave-Browser\Application\brave.exe" (
        echo Opening Brave...
        start "" "%ProgramFiles%\BraveSoftware\Brave-Browser\Application\brave.exe" --new-window --app="chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html"
    ) else if exist "%ProgramFiles(x86)%\BraveSoftware\Brave-Browser\Application\brave.exe" (
        echo Opening Brave...
        start "" "%ProgramFiles(x86)%\BraveSoftware\Brave-Browser\Application\brave.exe" --new-window --app="chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html"
    ) else if exist "%LocalAppData%\BraveSoftware\Brave-Browser\Application\brave.exe" (
        echo Opening Brave...
        start "" "%LocalAppData%\BraveSoftware\Brave-Browser\Application\brave.exe" --new-window --app="chrome-extension://mooikfkahbdckldjjndioackbalphokd/index.html"
    ) else (
        echo Brave not found.
    )

    REM Attempt to open Microsoft Edge
    if exist "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" (
        echo Opening Edge...
        start "" "%ProgramFiles%\Microsoft\Edge\Application\msedge.exe" --app="chrome-extension://ajdpfmkffanmkhejnopjppegokpogffp/index.html"
    ) else if exist "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" (
        echo Opening Edge...
        start "" "%ProgramFiles(x86)%\Microsoft\Edge\Application\msedge.exe" --app="chrome-extension://ajdpfmkffanmkhejnopjppegokpogffp/index.html"
    ) else if exist "%LocalAppData%\Microsoft\Edge\Application\msedge.exe" (
        echo Opening Edge...
        start "" "%LocalAppData%\Microsoft\Edge\Application\msedge.exe" --app="chrome-extension://ajdpfmkffanmkhejnopjppegokpogffp/index.html"
    ) else (
        echo Edge not found.
    )
    echo Finished attempting to open browsers.
) else (
    echo Browsers will not be opened.
)

timeout /t 3 /nobreak >nul
endlocal