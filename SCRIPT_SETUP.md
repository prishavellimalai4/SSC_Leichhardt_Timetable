# Time### Required Secrets

1. **BELTIMESURL**
   - The URL for downloading bell times data

2. **CALURL**
   - The URL for downloading calendar data

3. **TTURL**
   - The URL for downloading lesson information (timetable)Script Setup

## Repository Secrets Configuration

To use the automated timetable update script, you need to configure the following repository secrets in GitHub:

### Required Secrets

1. **BELL_TIMES_URL**
   - The URL for downloading bell times data
   - Example: `https://tempe-h.sentral.com.au/abc123/timetables/liss_info?debug=webedval/liss.publishBellTimes.debug`

2. **CALENDAR_URL**
   - The URL for downloading calendar data
   - Example: `https://tempe-h.sentral.com.au/abc123/timetables/liss_info?debug=webedval/liss.publishCalendar.debug`

3. **LISS_INFO_URL**
   - The URL for downloading lesson information
   - Example: `https://tempe-h.sentral.com.au/abc123/timetables/liss_info?debug=webedval/liss.publishTimetable.debug`

### How to Add Repository Secrets

1. Go to your GitHub repository
2. Click on **Settings** tab
3. In the left sidebar, click **Secrets and variables** → **Actions**
4. Click **New repository secret**
5. Add each of the three secrets listed above

### Manual Script Execution

You have several options for running the script manually:

#### Option 1: Local Testing Mode (Development Only)
```bash
# Quick test with hardcoded URLs (for development/testing only)
python update_timetable.py --local-test
```
⚠️ **Warning**: This mode uses hardcoded URLs and should only be used for development/testing.

#### Option 2: With Environment Variables
```bash
# Set environment variables (REQUIRED for production)
export BELTIMESURL="your-bell-times-url"
export CALURL="your-calendar-url"
export TTURL="your-timetable-url"

# Run the script
python update_timetable.py
```

#### Option 3: One-line with Environment Variables
```bash
# Run with environment variables in one command
BELTIMESURL="url1" CALURL="url2" TTURL="url3" python update_timetable.py
```

**Note:** For production use, the script requires environment variables to be set. Repository secrets are automatically available when running via GitHub Actions.

### Automated Updates

The GitHub Actions workflow is configured to:
- Run automatically every 4 hours during school days (Monday-Friday, 6 AM to 6 PM AEST)
- Can be triggered manually from the Actions tab

### Script Features

- Downloads XML data from URLs configured via environment variables/secrets
- Updates local XML files (bell_times.xml, calendar.xml, liss_info.xml)
- Commits changes with timestamp
- Pushes updates to the repository
- Handles errors gracefully
- Requires all environment variables to be set (no fallback URLs for security)
