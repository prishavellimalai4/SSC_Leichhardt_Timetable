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

# Tempe High School Timetable Kiosk - Complete Documentation

## Overview

The Tempe High School Timetable Kiosk is a modern, web-based application that displays real-time timetable information for students and staff. It features dual data source support (JSON API + XML fallback), intelligent period detection, responsive design, and comprehensive configurability for adaptation to any school.

## 🎯 Key Features

- **Dual Data Sources**: Primary JSON API integration with reliable XML fallback
- **Real-time Display**: Automatic current period detection and timetable updates
- **Fully Configurable**: Comprehensive `config.json` for school-specific customization
- **Responsive Design**: Height-aware layouts for various display sizes and kiosks
- **Smart Period Logic**: Handles special periods, sport scheduling, and year group exclusions
- **Debug Support**: Comprehensive logging and testing tools
- **API Integration**: Modern Sentral Student Management System integration

## 📋 Quick Start Guide

### Production Deployment (Recommended)

**GitHub Pages Hosting:**

1. **Fork this repository** to your GitHub account
2. **Customize configuration**:
   - Edit `config.json` for your school settings
   - Setup `sentral_config.json` for API access (optional)
3. **Add your data**:
   - Generate fresh data via API scripts, or
   - Upload your XML files (`bell_times.xml`, `calendar.xml`, `liss_info.xml`)
4. **Enable GitHub Pages**:
   - Repository Settings → Pages
   - Source: Deploy from branch `main`
   - Root folder: `/ (root)`
5. **Access**: `https://yourusername.github.io/repository-name`

📖 **Detailed deployment guide**: [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md)

### Local Development

**Requirements**: Any modern web browser + local web server (due to CORS policies)

**Quick setup**:

```bash
# Python (most common)
python -m http.server 8000

# Node.js alternative
npx http-server -p 8000

# PHP alternative
php -S localhost:8000
```

Then open: `http://localhost:8000`

**VS Code users**: Install "Live Server" extension → Right-click `index.html` → "Open with Live Server"

## 📁 Required Files & Data Sources

### Modern API Integration (Recommended)

The application now supports dual data sources for maximum reliability:

**Primary: JSON API Data**

- `calendar.json` - Generated from Sentral API via `generate_calendar.py`
- `bell_times.json` - Generated from Sentral API via `generate_bell_times.py`
- `liss_info.json` - Generated from Sentral API via `generate_liss_info.py` (optimized)
- Real-time data with automatic updates
- Structured JSON format for better performance

**Fallback: Traditional XML Files**

- `calendar.xml` - Academic calendar and day type information
- `bell_times.xml` - Period schedules and timing data
- `liss_info.xml` - Lesson assignments and class data
- Reliable backup when API is unavailable

**Core Application Files**

- `index.html` - Main timetable application
- `config.json` - School-specific configuration
- `sentral_config.json` - API endpoints and credentials (optional)

### Data Generation Tools

```bash
# Generate fresh calendar data from Sentral API
python generate_calendar.py

# Generate bell times from Sentral API
python generate_bell_times.py

# Generate LISS timetable data from Sentral API (optimized)
python generate_liss_info.py

# Verify data compatibility
python verify_calendar_compatibility.py
python verify_bell_times.py
```

## ⚙️ Configuration

### Main Configuration File: `config.json`

The application is fully configurable through a comprehensive JSON configuration file. Key areas:

**School Branding**

```json
{
  "school": {
    "name": "Your School Name",
    "logo": {
      "url": "https://your-school.edu/logo.png",
      "opacity": 0.15,
      "size": "auto 100vh"
    }
  }
}
```

**Visual Styling**

- Primary colors and branding
- Tile appearance and hover effects
- Text colors and typography
- Background and overlay settings

**Schedule Logic**

- Ignored days (weekends, holidays)
- School days and period timing rules
- Special period configurations (P0 early showing)
- Sport period handling with year group combinations

**Responsive Design**

- Breakpoints for different screen sizes
- Height-aware compact layout for narrow displays
- Multi-row vs single-row year group layouts

📖 **Complete configuration guide**: [CONFIGURATION.md](CONFIGURATION.md)

### API Configuration: `sentral_config.json`

Optional file for Sentral Student Management System integration:

```json
{
  "sentral_api": {
    "base_url": "https://your-school.sentral.com.au/",
    "tenant": "your_tenant_id",
    "api_key": "${REST_API_KEY}"
  },
  "endpoints": {
    "calendar_dates": "timetables/timetable-calendar-date",
    "timetable_periods": "timetables/timetable-period",
    "timetable_period_in_day": "timetables/timetable-period-in-day"
  }
}
```

## 🔄 How It Works

### Application Flow

1. **Initialization**: Load configuration and apply school-specific settings
2. **Data Loading**: Attempt JSON API first, fallback to XML if needed
3. **Period Detection**: Determine current or next relevant period
4. **Schedule Analysis**: Find lessons for the current period and day
5. **Smart Display**: Show classes organized by year groups
6. **Auto-refresh**: Update every minute to stay current

### Intelligent Period Logic

- **Time-based**: Shows periods based on bell schedule and current time
- **Look-ahead**: Displays upcoming periods when current has no classes
- **Special handling**: P0 can show from Friday afternoon for Monday morning
- **Sport periods**: Combines year groups and handles exclusions
- **Fallback**: Always finds something relevant to display

### Data Source Selection

The application intelligently chooses data sources:

```
1. Try JSON API data (if enabled in config)
   ↓ (if fails)
2. Fallback to XML files (if enabled in config)
   ↓ (if fails)
3. Show error message with helpful troubleshooting
```

Console debug output shows exactly which source is being used.

## 🎨 Customization for Other Schools

### Quick Adaptation Guide

1. **Basic Setup**:

   - Edit school name, logo, and colors in `config.json`
   - Adjust year groups and display preferences
   - Configure period timing rules

2. **Data Integration**:

   - **Option A**: Setup Sentral API integration for real-time data
   - **Option B**: Provide XML files with your school's data
   - **Option C**: Use both for maximum reliability

3. **Advanced Customization**:

   - Configure sport period handling
   - Setup responsive breakpoints for your displays
   - Customize period logic and timing rules

4. **Testing & Deployment**:
   - Test locally with debug mode enabled
   - Deploy to GitHub Pages for production
   - Monitor console logs for any issues

### Example Configurations

- `config.json` - Default Tempe High School setup
- `config-example-riverside.json` - Alternative school example
- Various templates available in documentation

## 🐛 Debugging & Troubleshooting

### Debug Mode

Enable comprehensive logging by setting `"debug": true` in `config.json`:

```json
{
  "ui": {
    "debug": true
  }
}
```

Console output will show:

- Data source selection decisions
- API loading attempts and results
- Period detection logic
- Configuration loading status

### Common Issues

**CORS Errors**

- **Cause**: Opening HTML file directly in browser
- **Solution**: Use web server (GitHub Pages, local server, VS Code Live Server)

**No Classes Displaying**

- Check calendar data for correct dates
- Verify period definitions in bell times
- Ensure lesson data matches current day/period
- Use debug mode to trace data loading

**Configuration Not Loading**

- Verify `config.json` syntax (use JSON validator)
- Check file permissions and accessibility
- Review browser console for error messages

**API Integration Issues**

- Verify `sentral_config.json` credentials
- Check network connectivity to Sentral instance
- Review API endpoint configurations
- Test individual endpoints with provided scripts

📖 **Detailed troubleshooting**: [DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md)

## 📚 Documentation Index

| Document                                                        | Purpose                               | Audience       |
| --------------------------------------------------------------- | ------------------------------------- | -------------- |
| **[📖 README.md](README.md)**                                   | Complete overview and setup guide     | Everyone       |
| **[⚙️ CONFIGURATION.md](CONFIGURATION.md)**                     | Detailed configuration reference      | Administrators |
| **[🚀 GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md)** | Production deployment guide           | IT Staff       |
| **[📊 CALENDAR_API_GUIDE.md](CALENDAR_API_GUIDE.md)**           | Calendar & Bell Times API integration | Developers     |
| **[🐛 DEBUGGING_GUIDE.md](DEBUGGING_GUIDE.md)**                 | Troubleshooting and debug tools       | Support Staff  |
| **[� GITHUB_ACTIONS_SETUP.md](GITHUB_ACTIONS_SETUP.md)**        | CI/CD automation setup                | DevOps         |
| **[📚 LISS_README.md](LISS_README.md)**                         | LISS integration specifics            | LISS Users     |

## 🏗️ Development & Contributing

### Project Structure

```
/
├── index.html                 # Main application
├── config.json              # School configuration
├── sentral_config.json      # API configuration
├── generate_calendar.py     # Calendar data generator
├── generate_bell_times.py   # Bell times data generator
├── generate_liss_info.py    # LISS timetable generator (optimized)
├── verify_*.py              # Data verification tools
├── test_*.py               # Testing utilities
└── docs/                   # Documentation
    ├── README.md           # This file
    ├── CONFIGURATION.md    # Configuration guide
    └── *.md               # Other documentation
```

### Testing Tools

- **Integration tests**: Verify overall functionality
- **Compatibility tests**: Check JSON/XML equivalence
- **Fallback tests**: Ensure reliable data source switching
- **Debug utilities**: Comprehensive logging and diagnostics

### API Integration

- **Sentral REST API**: Modern JSON endpoints
- **Automatic generation**: Fresh data from live systems
- **Verification tools**: Ensure data accuracy and completeness
- **Fallback support**: Graceful degradation to XML sources

## 📄 License

GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

See [LICENSE](../LICENSE) file for complete terms.

## 🏫 Support & Community

Originally developed for Tempe High School, this application is now available for any school to use and adapt. The modular design and comprehensive configuration system make it suitable for various educational environments.

**For questions, issues, or contributions**: Please use the GitHub repository's issue tracking and discussion features.

---

**🎓 Empowering schools with modern, reliable timetable display technology.**
