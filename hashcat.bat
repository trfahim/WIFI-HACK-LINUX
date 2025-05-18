@echo off
color 0A
set /p hashcat_lo="Enter hashcat file location: "
set /p hash_file="Enter target hash Path: "
set /p passlist="Enter password list Path: "

cd %hashcat_lo
hashcat -m 22000 -d 1 %hash_file% %passlist%

echo Hashcat process completed. [Password Not Found]
pause
