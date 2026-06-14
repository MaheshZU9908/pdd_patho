@echo off
title PathoAI Clinical Suite
color 0A

echo.
echo  ============================================
echo    PathoAI Clinical Suite — Starting Up
echo  ============================================
echo.

:: Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python not found. Please install Python 3.9+
    pause
    exit /b 1
)

:: Install deps
echo [1/2] Installing dependencies...
pip install -r requirements.txt --quiet

echo.
echo [2/2] Starting PathoAI server at http://localhost:8000
echo.
echo  Open your browser at: http://localhost:8000
echo  Press Ctrl+C to stop the server.
echo.

:: Run server from project root so "backend" package resolves
python -m uvicorn backend.app:app --host 127.0.0.1 --port 8000 --reload

pause
