<!--
Tempe High School Timetable Kiosk
Copyright (C) 2025 TempeHS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.
-->

# School Timetable Kiosk Application

## Overview

This is a configurable timetable kiosk application originally designed for Tempe High School but adaptable for any school. The app displays the current period's timetable in real-time.

## 🔧 Configuration for Other Schools

**This app is now fully configurable!** See [`CONFIGURATION.md`](CONFIGURATION.md) for detailed instructions on how to customize the app for your school.

Key configurable features:
- School name and logo
- Colors and styling
- Period timing rules
- Sport period handling
- Year group configurations
- Ignored days (weekends, holidays)
- Responsive layout breakpoints (including height-based compact mode)
- File names and paths

## CORS Policy and Local File Access

This timetable application requires access to local XML files. Due to browser security policies (CORS), you cannot simply open the `index.html` file directly in your browser. You need to run it through a local web server.

## Quick Start

### Option 1: GitHub Pages (Recommended for Production)

**For hosting on the web:**
1. **Fork this repository** or create a new repository with your files
2. **Upload your files** to the repository:
   - `index.html`
   - `config.json` (customized for your school)
   - `bell_times.xml`
   - `liss_info.xml` 
   - `calendar.xml`
3. **Enable GitHub Pages**:
   - Go to your repository's Settings
   - Scroll down to "Pages" section
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/ (root)" folder
   - Click "Save"
4. **Access your timetable** at: `https://yourusername.github.io/your-repository-name`

📖 **Detailed Instructions**: See [`GITHUB_PAGES_DEPLOYMENT.md`](GITHUB_PAGES_DEPLOYMENT.md) for complete step-by-step deployment guide.

**Benefits of GitHub Pages:**
- Free hosting
- Automatic HTTPS
- No CORS issues
- Easy updates via Git
- Perfect for school kiosks and displays

### Option 2: Use the provided batch file (Windows - Local Development)
1. Double-click `start-server.bat`
2. The script will automatically detect and use Python, Node.js, or PHP
3. Open your browser to `http://localhost:8000`

### Option 3: Manual server setup (Local Development)

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

### Option 4: VS Code Live Server (Local Development)
1. Install the "Live Server" extension in VS Code
2. Right-click on `index.html`
3. Select "Open with Live Server"

## Required Files

Make sure these files are in the same directory:
- `index.html` (main application)
- `config.json` (school configuration - **NEW!**)
- `bell_times.xml` (period schedule data)
- `liss_info.xml` (lesson data)
- `calendar.xml` (calendar data for Week A/B determination)

## Documentation Files

- [`README.md`](README.md) - Main documentation (this file)
- [`CONFIGURATION.md`](CONFIGURATION.md) - Complete configuration guide
- [`GITHUB_PAGES_DEPLOYMENT.md`](GITHUB_PAGES_DEPLOYMENT.md) - GitHub Pages deployment guide
- [`../SCRIPT_SETUP.md`](../SCRIPT_SETUP.md) - Python scripts and development tools
- [`config-example-riverside.json`](docs/config-example-riverside.json) - Example configuration for another school

## How It Works

The application automatically:
1. Loads the school configuration from `config.json`
2. Applies school-specific styling, colors, and logic
3. Adapts the layout based on screen dimensions (height-responsive compact mode)
4. Loads the current period based on time and bell schedule
5. Checks if the current period has classes for configured year levels
6. If no classes are found, advances to the next period with classes
7. Displays the timetable with classes organized by year level
8. Handles special cases like sport periods with combined year groups

## Configuration Examples

The repository includes example configurations:
- `config.json` - Default Tempe High School configuration
- [`docs/config-example-riverside.json`](docs/config-example-riverside.json) - Example for a different school

## For Other Schools

### Quick Setup Guide:

1. **For GitHub Pages (Production):**
   - Fork this repository
   - Replace `config.json` with your school's configuration
   - Replace XML files with your school's data
   - Enable GitHub Pages in repository settings
   - Access at `https://yourusername.github.io/repository-name`

2. **For Local Development:**
   - Download/clone the repository
   - Create your `config.json` based on [`CONFIGURATION.md`](CONFIGURATION.md)
   - Add your XML data files
   - Use any local server option above

### Detailed Configuration:
1. **Create your `config.json`** - See [`CONFIGURATION.md`](CONFIGURATION.md) for full details
2. **Prepare your XML data files** with your school's bell times, lessons, and calendar
3. **Customize colors and styling** to match your school branding
4. **Test locally** before deploying to production
5. **Deploy to GitHub Pages** or your preferred hosting service

### Key Configuration Areas:
- **School branding**: Name, logo, colors
- **Period timing**: Bell schedules, show-before times
- **Sport periods**: Combined year groups, exclusions
- **Year groups**: Display years, multi-row layouts
- **Schedule logic**: Ignored days, special periods
- **Responsive design**: Screen size breakpoints including height-based compact layout

The app will fall back to default settings if the configuration file cannot be loaded, ensuring it always functions.
5. Refreshes every minute to stay current

## Troubleshooting

**"CORS Error" or "Network Error":**
- You're trying to open the HTML file directly in your browser
- **Solution**: Use GitHub Pages, or one of the local web server options above
- GitHub Pages automatically resolves CORS issues

**"Error loading XML files" or "Error loading config.json":**
- Check that all required files are present in the same directory
- Verify file names match exactly (case-sensitive)
- Ensure files are not corrupted or have valid syntax
- For GitHub Pages: ensure files are committed and pushed to the repository

**"No classes" showing when there should be classes:**
- Check the `calendar.xml` for correct date entries
- Verify the `bell_times.xml` has correct period definitions  
- Ensure `liss_info.xml` has lessons for the current day/period
- Check the `config.json` for correct year group and period configurations

**Sport periods not working correctly:**
- Verify day names in `calendar.xml` (e.g., "TueB", "MonA")
- Check sport period configuration in `config.json`
- Ensure excluded years are configured correctly
- Use browser console (F12) to check for JavaScript errors

**Styling issues:**
- Check `config.json` color values are valid CSS colors
- Ensure logo URL is accessible and valid
- Verify responsive breakpoints in configuration

## Production Deployment

**GitHub Pages (Recommended):**
- Automatic HTTPS encryption
- Global CDN for fast loading
- No server maintenance required
- Easy updates via Git commits
- Perfect for school displays and kiosks

**Alternative Hosting:**
- Any web server that can serve static files
- Ensure HTTPS is enabled for security
- Consider CDN for better performance
