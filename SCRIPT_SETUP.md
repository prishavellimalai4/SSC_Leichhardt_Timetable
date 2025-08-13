# Additional Scripts Setup Guide

This repository includes several utility scripts for development and XML data management.

## 🐍 **Python Scripts**

### 1. **server.py** - Local Development Server
**Purpose**: Serves the timetable application locally with CORS headers

**Usage**:
```bash
python server.py
```

**Features**:
- Automatically opens browser to http://localhost:8000
- Adds CORS headers for local file access
- Serves files from the script's directory
- Press Ctrl+C to stop

### 2. **browser_fetch.py** - Advanced XML Fetcher
**Purpose**: Automated XML content fetching with multiple methods

**Usage**:
```bash
python browser_fetch.py
```

**Methods**:
1. **Selenium Automated** - Uses Chrome WebDriver for full automation
2. **Browser + Clipboard** - Opens URLs and captures from clipboard  
3. **Manual Input** - Guided manual content entry

**Requirements**:
- For Method 1: `pip install selenium` + ChromeDriver
- For Method 2: `pip install pyperclip`
- For Method 3: No additional requirements

### 3. **simple_fetch.py** - Simple XML Fetcher (Recommended)
**Purpose**: User-friendly XML content fetching

**Usage**:
```bash
python simple_fetch.py
```

**Features**:
- Opens URLs automatically in your default browser
- Step-by-step guidance for each XML file
- Automatic clipboard detection (where supported)
- Manual fallback input
- Automatic file saving and git commit options

**Process**:
1. Script opens each URL in your browser
2. You login to Sentral and copy the XML content
3. Script captures content and saves to files
4. Optional git commit and push

### 4. **update_timetable.py** - Automated Update Script
**Status**: Currently empty - placeholder for future automated updates

## 🚀 **Batch Files**

### **start-server.bat** - Windows Local Server
**Purpose**: Automatically detects and starts a local web server on Windows

**Usage**: Double-click the file or run from command prompt

**Detection Order**:
1. Python (`python -m http.server 8000`)
2. Node.js (`npx http-server -p 8000`)
3. PHP (`php -S localhost:8000`)

## 📋 **Recommended Workflow**

### For Regular Updates:
1. **Use simple_fetch.py** for easy XML content updates
2. **Use server.py** for local development and testing
3. **Use start-server.bat** on Windows for quick local serving

### For Advanced Users:
1. **Use browser_fetch.py** for more automated workflows
2. **Customize update_timetable.py** for school-specific automation

## 🔧 **Installation Requirements**

### Basic Usage (No installation required):
- `server.py`
- `start-server.bat`
- `simple_fetch.py` (manual mode)

### Advanced Features:
```bash
# For automated browser control
pip install selenium

# For clipboard access
pip install pyperclip

# For HTTP requests (usually built-in)
pip install requests
```

### ChromeDriver Setup (for Selenium):
1. Download ChromeDriver from https://chromedriver.chromium.org/
2. Add to PATH or place in script directory
3. Ensure version matches your Chrome browser

## 📁 **File Organization**

```
repository/
├── index.html              # Main application
├── config.json            # School configuration
├── server.py              # Local development server
├── simple_fetch.py        # Simple XML fetcher (recommended)
├── browser_fetch.py       # Advanced XML fetcher
├── update_timetable.py    # Automated updates (placeholder)
├── start-server.bat       # Windows batch server starter
├── docs/                  # Documentation
└── *.xml                  # XML data files
```

## 🚨 **Troubleshooting**

**Python not found**:
- Install Python from https://python.org
- Ensure Python is added to PATH

**Permission errors**:
- Run scripts with appropriate permissions
- On Linux/Mac: `chmod +x script.py`

**Browser doesn't open automatically**:
- Manually navigate to http://localhost:8000
- Check firewall settings

**XML fetching fails**:
- Ensure you're logged into Sentral
- Check network connectivity
- Try manual mode in simple_fetch.py

**ChromeDriver errors**:
- Update ChromeDriver to match Chrome version
- Ensure ChromeDriver is in PATH
- Try browser_fetch.py Method 2 or 3 instead
