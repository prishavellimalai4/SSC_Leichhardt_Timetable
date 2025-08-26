# Timetable Kiosk

A modern, web-based timetable display system designed for schools using Sentral student information systems. This application provides real-time timetable information in a clean, easy-to-read format perfect for digital displays throughout your school.

## 📱 About This App

**Timetable Kiosk** is a lightweight web application that displays school timetable information in an attractive, easy-to-read format. Originally developed for Tempe High School, it's designed to work with any school using Sentral student management systems.

### Key Features

- **Real-time Display**: Shows current day's schedule with live period highlighting
- **Multi-source Data**: Uses JSON API data with automatic XML fallback
- **Responsive Design**: Works on any device - from large displays to mobile phones
- **Zero Maintenance**: Automatic refresh system with daily 7:30am fresh starts
- **Plug-and-Play**: Works immediately with included sample data
- **Highly Configurable**: Extensive customization options for any school
- **Automated Updates**: GitHub Actions for hands-free data synchronization
- **Robust Error Handling**: Intelligent fallback systems ensure continuous operation

### What It Shows

- **Daily Timetables**: Complete schedule for all year groups (7-12)
- **Current Period**: Live highlighting of what's happening now
- **Bell Times**: Period start/end times with visual indicators
- **Teacher Information**: Staff assignments for each class
- **Room Allocations**: Where each class is taking place
- **Special Periods**: Handles sport periods, assemblies, and other events

## 🎯 Use Cases

- **Reception Areas**: Welcome visitors with current school information
- **Staff Rooms**: Quick reference for teachers and administrators
- **Corridors & Common Areas**: Help students navigate their day
- **Digital Signage**: Perfect for TV displays and information kiosks
- **Mobile Access**: Staff and students can access on their devices

## 🚀 Getting Started

**Want to try it right now?**

1. Download this repository
2. Open `index.html` in any web browser
3. See the kiosk in action with sample data

**Ready to use it at your school?**

See the **[Setup Guide](docs/README.md)** for detailed implementation instructions.

## 🔧 Technical Overview

### Architecture

- **Frontend**: Pure HTML/CSS/JavaScript - no frameworks required
- **Data Sources**: JSON files (primary) with XML fallback support
- **API Integration**: Connects to Sentral REST API for live data
- **Automation**: GitHub Actions for scheduled data updates
- **Deployment**: Static files - works on any web server or GitHub Pages

### Recent Improvements (v2.1)

- **Fixed GitHub Actions conflicts**: Workflows now handle git merge conflicts automatically
- **Enhanced error handling**: Better fallback mechanisms for data loading
- **Improved scheduling**: Optimized LISS updates during school hours only
- **Better logging**: Comprehensive debug information for troubleshooting
- **Performance optimizations**: Faster data loading and processing

### Browser Support

- ✅ Chrome, Firefox, Safari, Edge (all modern versions)
- ✅ Mobile browsers (iOS Safari, Android Chrome)
- ✅ Kiosk mode and embedded iframe support

### System Requirements

- **Server**: Any web server (Apache, Nginx, IIS) or static hosting
- **Client**: Modern web browser with JavaScript enabled
- **API (Optional)**: Sentral student management system with REST API access

## 📊 Data Integration

The kiosk supports multiple data sources for maximum reliability:

1. **Live API Data**: Direct integration with Sentral REST API
2. **Cached JSON**: Local files generated from API calls
3. **Static XML**: Fallback files downloaded from Sentral web interface
4. **Sample Data**: Built-in demonstration data for testing

This multi-tier approach ensures the kiosk always displays useful information, even during network outages or API maintenance.

## 🛠️ Implementation

### For Non-Technical Users

- Download and open `index.html` - it works immediately
- Upload files to your school website for broader access
- No programming or server setup required

### For Technical Staff

- Full API integration with weekly automated data updates
- GitHub Actions workflows for maintenance-free operation
- Extensive configuration options for customization
- Development tools and debugging support

**Complete setup instructions**: [docs/README.md](docs/README.md)

## 📋 File Structure

```
Timetable Kiosk/
├── index.html              # Main application (open this!)
├── config.json             # Display and behavior settings
├── sentral_config.json     # API connection settings
├── *.json                  # Data files (JSON format)
├── *.xml                   # Fallback data files (XML format)
├── generate_*.py           # Data generation scripts
├── requirements.txt        # Python dependencies
├── docs/                   # Implementation guides
│   ├── README.md           # Setup instructions
│   ├── CONFIGURATION.md    # Configuration reference
│   └── *.md               # Additional guides
└── README.md              # This file
```

## 🤝 Contributing

This project welcomes contributions from the educational technology community:

- **Bug Reports**: Found an issue? Please report it with details
- **Feature Requests**: Suggestions for improvements are welcome
- **Code Contributions**: Pull requests for enhancements or fixes
- **Documentation**: Help improve setup guides and examples
- **Testing**: Try it at your school and share feedback

## 🏫 Community

**Schools Using This System:**

- Tempe High School (original implementation)
- _Your school could be listed here!_

**Compatible Systems:**

- Sentral Student Management System (primary target)
- Any system that can export similar XML/JSON data formats

## ⚖️ License

**MIT License**

Copyright (c) 2025 Tempe High School

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## 📞 Support

- **Setup Questions**: See [docs/README.md](docs/README.md) for implementation guide
- **Configuration Help**: Check [docs/CONFIGURATION.md](docs/CONFIGURATION.md) for all options
- **Technical Issues**: Review [docs/DEBUGGING_GUIDE.md](docs/DEBUGGING_GUIDE.md) for troubleshooting
- **Feature Requests**: Open an issue on GitHub
- **Recent Changes**: See [CHANGELOG.md](CHANGELOG.md) for version history and updates

## 📋 Version Information

**Current Version**: 2.1.0

**Recent Updates**:

- ✅ Fixed GitHub Actions git conflict issues
- 🚀 Enhanced automation and error handling
- 📚 Updated all documentation
- 🔧 Improved workflow reliability

See [CHANGELOG.md](CHANGELOG.md) for complete version history.

## 🎖️ Credits

Developed by Tempe High School for the educational community. Special thanks to all schools and developers who have contributed feedback, testing, and improvements to make this system better for everyone.

---

**Ready to get started?** → [Setup Guide](docs/README.md)
