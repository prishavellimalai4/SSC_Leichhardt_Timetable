# Timetable Kiosk - Implementation Guide

This guide provides step-by-step instructions for implementing the timetable kiosk at your school.

## 🚀 Quick Implementation

### Option 1: Use As-Is (Immediate Setup)

1. **Download**: Clone or download this repository
2. **Open**: Navigate to `index.html` in any web browser
3. **Done**: The kiosk displays with sample data and is ready to use

### Option 2: GitHub Pages Deployment (Free Hosting)

1. **Fork**: Fork this repository to your GitHub account
2. **Enable Pages**: Go to Settings → Pages → Deploy from branch `main`
3. **Access**: Your kiosk is available at `https://yourusername.github.io/Tempe_HS_Timetable_Kiosk/`

### Option 3: School Website Integration

1. **Upload**: Copy all files to your school's web server
2. **Link**: Create links to `index.html` from your school website
3. **Embed**: Use in iframes or as standalone kiosk displays

## 🔧 Connecting Your School Data

### Step 1: Get Your Sentral API Key

1. Login to your Sentral portal: `https://<your-school-sentral>/`
2. Navigate to: **Admin** → **Integrations** → **REST API** → **Configure**
3. Generate or copy your API key

### Step 2: Configure API Connection

Edit `sentral_config.json`:

```json
{
  "base_url": "https://<your-school-sentral>/",
  "api_key": "your-api-key-here",
  "endpoints": {
    "liss_info": "restapi/v1/liss/info"
  }
}
```

### Step 3: Set Up Automated Updates (Optional)

For automatic data updates using GitHub Actions:

1. **Add Repository Secrets** (Settings → Secrets and variables → Actions):

   - `REST_API_KEY`: Your Sentral API key
   - `LISS_PASSWORD`: Your LISS system password (if used)

2. **Enable Workflows**:

   - Go to Actions tab in your repository
   - Enable workflows if prompted

3. **Manual Updates**: Use "Run workflow" button to update data anytime

## 📊 Using Your School's Data

### Automatic API Updates (Recommended)

- Run the Python generation scripts to fetch live data
- Data refreshes automatically via GitHub Actions
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

Control how often data is checked:

```json
{
  "api": {
    "sync_days": 7,
    "refresh_minutes": 30
  }
}
```

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
