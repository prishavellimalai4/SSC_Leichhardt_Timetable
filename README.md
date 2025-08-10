# LISS Timetable Application

## CORS Policy and Local File Access

This timetable application requires access to local XML files. Due to browser security policies (CORS), you cannot simply open the `index.html` file directly in your browser. You need to run it through a local web server.

## Quick Start

### Option 1: Use the provided batch file (Windows)
1. Double-click `start-server.bat`
2. The script will automatically detect and use Python, Node.js, or PHP
3. Open your browser to `http://localhost:8000`

### Option 2: Manual server setup

**If you have Python installed:**
```bash
python -m http.server 8000
```
Then open: http://localhost:8000

**If you have Node.js installed:**
```bash
npx http-server -p 8000
```
Then open the URL provided in the terminal

**If you have PHP installed:**
```bash
php -S localhost:8000
```
Then open: http://localhost:8000

### Option 3: VS Code Live Server
1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## Required Files

Make sure these files are in the same directory:
- `index.html` (main application)
- `bell_times.xml` (period schedule data)
- `liss_info.xml` (lesson data)
- `calendar.xml` (calendar data for Week A/B determination)

## How It Works

The application automatically:
1. Loads the current period based on time and bell schedule
2. Checks if the current period has classes for years 7-12
3. If no classes are found, advances to the next period with classes
4. Displays the timetable with classes organized by year level
5. Refreshes every minute to stay current

## Troubleshooting

**"CORS Error" or "Network Error":**
- You're trying to open the HTML file directly
- Use one of the web server options above

**"Error loading XML files":**
- Check that all XML files are present
- Verify file names match exactly (case-sensitive)
- Ensure files are not corrupted

**"No classes" showing when there should be classes:**
- Check the calendar.xml for correct date entries
- Verify the bell_times.xml has correct period definitions
- Ensure liss_info.xml has lessons for the current day/period
