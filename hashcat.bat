@echo off
title Hashcat Wi-Fi Cracker by TR FAHIM
color 0A
cls

:: Set working directory
set "HASHCAT_DIR=C:\Users\trfah\Downloads\Wifi_Crack\hashcat"
cd /d "%HASHCAT_DIR%"

echo ================================
echo      Hashcat Wi-Fi Cracker
echo        By TR FAHIM
echo ================================
echo.

:: Get user input
set /p "hash_file=Enter full path to target hash file (.hccapx or .22000): "
if not exist "%hash_file%" (
    color 0C
    echo Error: Hash file not found!
    pause
    exit /b
)

set /p "passlist=Enter full path to password list: "
if not exist "%passlist%" (
    color 0C
    echo Error: Password list file not found!
    pause
    exit /b
)

:: Choose device
echo.
echo Select device type:
echo 1. GPU (Recommended)
echo 2. CPU (Slower)
set /p "dev=Choice [1/2]: "

if "%dev%"=="2" (
    set "device=-D 1"
) else (
    set "device=-D 2"
)

:: Run Hashcat
echo.
color 0E
echo Starting Hashcat...
echo.
hashcat -m 22000 %device% -a 0 "%hash_file%" "%passlist%" --force

:: Show cracked result
echo.
echo Checking for cracked password...
hashcat -m 22000 "%hash_file%" --show > result.txt

:: Check if result.txt has content (non-empty)
for /f %%A in ('findstr /r /v "^$" result.txt') do (
    set found=true
    goto show_result
)

:show_result
if defined found (
    color 0E
    echo.
    echo Password found:
    type result.txt
) else (
    color 0C
    echo.
    echo Password not found.
)

:: Clean up
del result.txt >nul 2>&1
echo.
pause
