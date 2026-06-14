@echo off
title PathoAI — Launch
echo Starting PathoAI server...
start "PathoAI Server" cmd /k "cd /d "%~dp0" && python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload"
timeout /t 3 /nobreak > nul
start chrome --new-window --incognito http://127.0.0.1:8000
