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

You can also run the script manually, but you **must** set the environment variables:

```bash
# Set environment variables (REQUIRED)
export BELTIMESURL="your-bell-times-url"
export CALURL="your-calendar-url"
export TTURL="your-timetable-url"

# Run the script
python update_timetable.py
```

**Note:** The script will exit with an error if any of the required environment variables are not set.

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
