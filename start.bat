@echo off
setlocal enabledelayedexpansion

set "config_file=scoreboard.conf"

for /f "tokens=1,* delims==" %%a in ('findstr /r "^host= ^port=" "%config_file%"') do (
    if "%%a"=="host" set "host=%%b"
    if "%%a"=="port" set "port=%%b"
)

@echo off
start python app.py
start "" "http://%host%:%port%/sport"