@echo off
echo Starting local web server for LISS Timetable...
echo.
echo Checking for available server options...
echo.

REM Check for Python
python --version >nul 2>&1
if %errorlevel% == 0 (
    echo Found Python - Starting server on http://localhost:8000
    echo.
    echo Press Ctrl+C to stop the server
    echo.
    python -m http.server 8000
    goto :end
)

REM Check for Node.js
node --version >nul 2>&1
if %errorlevel% == 0 (
    echo Found Node.js - Installing and starting http-server...
    echo.
    npx http-server -p 8000
    goto :end
)

REM Check for PHP
php --version >nul 2>&1
if %errorlevel% == 0 (
    echo Found PHP - Starting server on http://localhost:8000
    echo.
    echo Press Ctrl+C to stop the server
    echo.
    php -S localhost:8000
    goto :end
)

echo No compatible server found.
echo Please install Python, Node.js, or PHP to run a local web server.
echo.
echo Alternatively, use VS Code with the Live Server extension.
echo.
pause

:end
