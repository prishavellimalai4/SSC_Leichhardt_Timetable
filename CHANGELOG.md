# Changelog

All notable changes to the Timetable Kiosk project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-08-26

### 🔧 Fixed

- **GitHub Actions Git Conflicts**: Fixed critical issue where workflows failed with "Your local changes would be overwritten by merge" errors
  - Workflows now automatically stash local changes before pulling updates
  - Intelligent recovery mechanism if stash pop fails
  - Applies to both `liss-timetable-updates.yml` and `weekly-data-update.yml`
- **Workflow Error Handling**: Enhanced error recovery and logging in GitHub Actions

### 📚 Documentation

- **Updated all documentation files** with current information and recent fixes
- **Enhanced Debugging Guide**: Added GitHub Actions troubleshooting section
- **Improved GitHub Actions Setup Guide**: Documented git conflict resolution
- **Updated README**: Added recent improvements and enhanced feature list
- **Enhanced Setup Guide**: Updated automation section with v2.1 improvements

### 🚀 Improvements

- **Better Error Messages**: More descriptive error handling in workflows
- **Enhanced Logging**: Improved debug information throughout the system
- **Time Zone Handling**: Better documentation of Sydney time zone handling in workflows

## [2.0.0] - 2025-01-15

### 🆕 Added

- **LISS Timetable Integration**: Real-time timetable updates during school hours
- **Optimized Data Generation**: 20x faster API processing with 95% fewer calls
- **Intelligent Scheduling**: LISS updates every 15 minutes during school hours only
- **Enhanced API Integration**: Complete Sentral REST API implementation
- **Automated GitHub Actions**: Weekly data updates and real-time LISS updates

### 🔧 Enhanced

- **Multi-source Data Loading**: JSON primary with XML fallback
- **Performance Optimizations**: Bulk API operations and reduced network calls
- **Debug System**: Comprehensive logging for troubleshooting
- **Error Handling**: Robust fallback mechanisms

### 📱 UI/UX

- **Responsive Design**: Works on all device sizes
- **Live Period Highlighting**: Current period visual indicators
- **Auto-refresh System**: Smart refresh with memory management
- **Clean Interface**: Modern, professional appearance

## [1.0.0] - 2024-12-01

### 🎉 Initial Release

- **Basic Timetable Display**: Shows daily schedules for all year groups
- **XML Data Support**: Loads data from Sentral XML exports
- **Configurable Display**: Customizable school branding and colors
- **Static File Deployment**: Works on any web server
- **Sample Data**: Includes demonstration data for testing

### 📋 Core Features

- **Bell Times Display**: Period start/end times
- **Teacher Information**: Staff assignments for classes
- **Room Allocations**: Classroom locations
- **Year Group Organization**: Separate views for different year levels

### 🛠️ Technical

- **Pure HTML/CSS/JavaScript**: No framework dependencies
- **Cross-browser Compatible**: Works on all modern browsers
- **Mobile Responsive**: Touch-friendly interface
- **Easy Configuration**: JSON-based settings

---

## Version Numbering

- **Major** (X.0.0): Breaking changes or major new features
- **Minor** (0.X.0): New features, enhancements, significant improvements
- **Patch** (0.0.X): Bug fixes, documentation updates, minor improvements

## Support

For issues related to specific versions:

- **v2.1+**: Check the [Debugging Guide](docs/DEBUGGING_GUIDE.md) for GitHub Actions troubleshooting
- **v2.0+**: See [GitHub Actions Setup](docs/GITHUB_ACTIONS_SETUP.md) for automation configuration
- **All versions**: Review [Configuration Guide](docs/CONFIGURATION.md) for setup help

## Migration Notes

### Upgrading to v2.1

- **No configuration changes required**
- **Workflows auto-update** when you pull latest changes
- **Existing setup continues working** with improved reliability

### Upgrading to v2.0

- **Add repository secrets** for API keys if using automation
- **Update config.json** with new API settings
- **Enable GitHub Actions** for automated updates
- **Previous XML-only setups continue working** as fallback
