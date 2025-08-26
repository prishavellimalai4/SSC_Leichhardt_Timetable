# Timetable Kiosk - Setup Guide

This guide provides step-by-step instructions for setting up the timetable kiosk at your school.

## 🚀 Quick Setup Options

### Option 1: GitHub Pages (Recommended - Free Hosting)

1. **Fork this repository** to your GitHub account
2. **Edit `config.json`** with your school details (see Configuration section below)
3. **Enable GitHub Pages**: Settings → Pages → Deploy from branch `main`
4. **Access your kiosk**: `https://yourusername.github.io/Tempe_HS_Timetable_Kiosk/`

### Option 2: Download and Host Locally

1. **Download**: Clone or download this repository
2. **Customize**: Edit `config.json` with your school settings
3. **Upload**: Copy all files to your school's web server
4. **Access**: Navigate to `index.html` in any web browser

## 🔧 Essential Configuration

### School Information

Edit the `school` section in `config.json`:

```json
{
  "school": {
    "name": "Your School Name",
    "term": "Term 1 2025",
    "colours": {
      "primary": "#1e3a8a",
      "secondary": "#3b82f6",
      "text": "#ffffff"
    },
    "logo": {
      "url": "https://your-school.edu/logo.png",
      "opacity": 0.15
    }
  }
}
```

### Connecting Live Data (Optional)

To connect your Sentral API for automated live data updates:

1. **Get API Key**: Login to Sentral → Admin → Integrations → REST API → Configure
2. **Update config.json with school details** (keep the placeholder for API key):

```json
{
  "api": {
    "sentral": {
      "base_url": "https://your-school-sentral.com.au/",
      "api_key": "${REST_API_KEY}",
      "tenant": "your-tenant-id"
    }
  }
}
```

3. **Add Repository Secret** (Settings → Secrets and variables → Actions):

   - Name: `REST_API_KEY`
   - Value: Your actual Sentral API key

4. **Enable automated updates** (see GitHub Actions Setup guide below)

⚠️ **Security Note**: Never put your actual API key directly in config.json. Always use the `${REST_API_KEY}` placeholder and store the real key as a repository secret.

## 🤖 Automated Data Updates

### GitHub Actions Workflows (v2.1 - Enhanced)

For hands-free operation with weekly automatic data updates:

1. **Add Repository Secrets** (Settings → Secrets and variables → Actions):

   - `REST_API_KEY`: Your Sentral API key
   - `LISS_PASSWORD`: Your LISS system password (if used)

2. **Enable Workflows**:

   - Go to Actions tab in your repository
   - Enable workflows if prompted
   - **Weekly Data Update**: Runs every Monday at 5:00 AM Sydney time
   - **LISS Timetable Update**: Runs every 15 minutes during school hours (7:30 AM - 3:30 PM weekdays)

3. **Enhanced Features** (v2.1):

   - **Automatic git conflict resolution**: No more merge errors
   - **Smart scheduling**: LISS updates only during school hours
   - **Robust error handling**: Automatic stashing and recovery
   - **Time zone awareness**: Handles Sydney AEST/AEDT automatically

4. **Manual Updates**: Use "Run workflow" button to update data anytime

## 📱 Usage

### For Kiosk Displays

- Open in full-screen mode (F11)
- **Automatic refresh system**: No manual setup required!
  - Data updates every minute (smooth, no page flash)
  - Hourly full reload for memory management
  - Daily 7:30am fresh start for optimal performance
- Use on tablets, monitors, or touch screens
- Perfect for continuous display in hallways, offices, or student areas

### For School Websites

- Embed using iframe
- Link directly from school portal
- Works on all devices and browsers

## 📚 Additional Guides

- **[Configuration Reference](CONFIGURATION.md)** - Complete configuration options
- **[GitHub Actions Setup](GITHUB_ACTIONS_SETUP.md)** - Automated data updates
- **[GitHub Pages Deployment](GITHUB_PAGES_DEPLOYMENT.md)** - Detailed hosting setup
- **[LISS Integration](LISS_README.md)** - Advanced timetable features
- **[Troubleshooting](DEBUGGING_GUIDE.md)** - Common issues and solutions
- **[Version History](../CHANGELOG.md)** - Recent updates and fixes

## 🆘 Support

If you encounter issues:

1. Check the [Troubleshooting Guide](DEBUGGING_GUIDE.md)
2. Review your `config.json` settings
3. Open browser console (F12) for error messages
4. Ensure all required files are uploaded correctly

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](../LICENSE) file for details.

## 📊 Using Your School's Data

### Automatic API Updates (Recommended)

- Run the Python generation scripts to fetch live data
- Data refreshes automatically every Monday via GitHub Actions
- Falls back to XML files if API is unavailable

### Manual XML Files (Alternative)

If you prefer not to use the API:

1. **Download XML files** from your Sentral portal:

   - Bell times: `https://<your-school-sentral>/ABCDE/timetables/bell_times`
   - Calendar: `https://<your-school-sentral>/ABCDE/timetables/calendar`
   - Timetable: `https://<your-school-sentral>/ABCDE/timetables/liss_info`

2. **Replace the included XML files** with your school's versions

3. **The kiosk automatically detects and uses your data**

## ⚙️ Customization Options

### Display Settings (`config.json`)

```json
{
  "school": {
    "name": "Your School Name",
    "term": "Current Term"
  },
  "display": {
    "showCurrentPeriod": true,
    "showUpcomingPeriod": true,
    "defaultView": "day"
  },
  "api": {
    "sync_days": 7
  }
}
```

### Styling and Branding

- Edit CSS in `index.html` for colors and fonts
- Replace logo images with your school branding
- Modify layout sections for specific display requirements

## 🛠️ Technical Implementation

### Data Sources Priority

The kiosk uses an intelligent data loading system:

1. **JSON Files** (Primary): Generated from Sentral API for real-time data
2. **XML Files** (Fallback): Used when JSON is stale (>7 days) or unavailable
3. **Sample Data** (Backup): Ensures kiosk always displays something

### File Structure

```
📦 Implementation Files
├── 🌐 index.html              # Main application (open this!)
├── ⚙️ config.json            # School configuration
├── 📊 *.json                 # Live data (API generated)
├── 📊 *.xml                  # Fallback data (manual/download)
├── 🔌 sentral_config.json    # API settings (optional)
└── 📖 docs/                  # Implementation guides
```

### Python Scripts (Optional)

Only needed if using API automation:

```bash
# Install dependencies
pip install -r requirements.txt

# Generate current data
python generate_liss_info.py
python generate_bell_times.py
python generate_calendar.py
```

## 🎨 Customization Examples

### Change School Branding

Edit the `school` section in `config.json`:

```json
{
  "school": {
    "name": "Lincoln High School",
    "term": "Term 1 2025",
    "colors": {
      "primary": "#003366",
      "secondary": "#FFD700"
    }
  }
}
```

### Adjust Display Behavior

Configure what information is shown:

```json
{
  "display": {
    "showCurrentPeriod": true,
    "showUpcomingPeriod": true,
    "showTomorrowSchedule": false,
    "defaultView": "day",
    "compactMode": false
  }
}
```

### Modify Refresh Settings

Control automatic refresh behavior:

```json
{
  "ui": {
    "refreshInterval": 60000,
    "autoRefresh": true,
    "hourlyReload": true
  }
}
```

**Refresh Options:**

- **refreshInterval**: Data refresh frequency in milliseconds (60000 = 1 minute)
- **autoRefresh**: Enable/disable automatic data updates (true/false)
- **hourlyReload**: Enable/disable hourly full page reload (true/false)
- **Daily 7:30am reload**: Always enabled for optimal kiosk performance

## 🔍 Troubleshooting

### Kiosk Shows No Data

1. **Check file presence**: Ensure `*.json` or `*.xml` files exist
2. **Verify format**: Open data files to check they're not empty/corrupted
3. **Browser console**: Press F12 and check for JavaScript errors

### API Not Working

1. **Test API key**: Visit `https://<your-school-sentral>/restapi/v1/ping` with your key
2. **Check config**: Verify `sentral_config.json` has correct base_url and api_key
3. **Run manual test**: Execute `python generate_liss_info.py` to test connection

### Display Issues

1. **Clear browser cache**: Hard refresh with Ctrl+F5
2. **Check CSS**: Ensure styling isn't being overridden
3. **Test different browsers**: Try Chrome, Firefox, Safari, Edge

## 📞 Support Resources

### Implementation Help

- **[Configuration Guide](CONFIGURATION.md)**: Detailed configuration options
- **[GitHub Actions Setup](GITHUB_ACTIONS_SETUP.md)**: Automated data updates
- **[LISS Integration](LISS_README.md)**: Advanced timetable features

### API Documentation

- **[Sentral API Guide](sentral_api_guide.pdf)**: Official API documentation
- **[OpenAPI Spec](openapi.json)**: Technical API reference

### Quick References

- **[Stale Data Fallback](STALE_DATA_FALLBACK.md)**: How automatic fallback works
- **[Debugging Guide](DEBUGGING_GUIDE.md)**: Troubleshooting techniques

## 🎯 Production Checklist

Before deploying to your school:

- [ ] **Test locally**: Open `index.html` and verify display
- [ ] **Add your data**: Either via API scripts or manual XML files
- [ ] **Customize branding**: Update school name, colors, logo
- [ ] **Configure display**: Set appropriate periods and views
- [ ] **Test on target devices**: Verify on actual kiosk hardware/browsers
- [ ] **Set up monitoring**: Consider automated health checks
- [ ] **Document for staff**: Create simple user guide for your school

## 📄 License & Credits

This timetable kiosk is open source software released under the MIT License. It was originally developed for Tempe High School but is designed to work with any school using Sentral Student Management System.

Free to use, modify, and distribute for educational purposes.
