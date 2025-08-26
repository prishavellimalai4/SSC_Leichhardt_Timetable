# Troubleshooting Guide

Quick solutions for common issues with the timetable kiosk.

## 🔍 Quick Diagnostics

### Kiosk Not Loading

**Check the basics**:

1. Open browser console (F12)
2. Look for red error messages
3. Refresh the page (Ctrl+F5 for hard refresh)

**Common causes**:

- Missing data files (`*.json` or `*.xml`)
- JavaScript errors (check console)
- Network connectivity issues

### No Data Showing

**Verify data files exist**:

```bash
# Check for data files
ls -la *.json *.xml
```

**Files needed**:

- `bell_times.json` or `bell_times.xml`
- `calendar.json` or `calendar.xml`
- `liss_info.json` or `liss_info.xml`

### Wrong School Data

**Update configuration**:

1. Edit `config.json` for school name/settings and API connection
2. Run data generation scripts to fetch fresh data

## 🔧 Enable Debug Mode

### Turn On Detailed Logging

Edit `config.json`:

```json
{
  "ui": {
    "debug": true
  }
}
```

### View Debug Information

1. **Open browser console** (F12)
2. **Refresh the page**
3. **Look for detailed logs** about data loading and processing

Debug output shows:

- Which data files are being loaded
- API connection status
- Data processing steps
- Error details

## 📊 Data Issues

### API Not Working

**Test your API key**:

1. Visit: `https://<your-school-sentral>/restapi/v1/ping`
2. Include your API key in request headers
3. Should return successful response

**Check configuration**:

```json
{
  "api": {
    "sentral": {
      "base_url": "https://<your-school-sentral>/",
      "api_key": "your-actual-api-key",
      "tenant": "your-tenant-id"
    }
  }
}
```

### Stale Data Warning

**What it means**: Data is older than configured threshold (default: 7 days)

**Solutions**:

- Run `python generate_*.py` scripts to refresh data
- Use GitHub Actions for weekly automated updates
- Download fresh XML files from Sentral portal

### Generation Script Errors

**Common Python issues**:

```bash
# Install dependencies
pip install -r requirements.txt

# Check Python version (needs 3.6+)
python --version

# Test API connection
python generate_liss_info.py
```

The debug system provides detailed logging for both calendar and bell times data sources.

### Calendar Source Debugging

#### JSON Calendar Source Debugging

- ✅ Logs when attempting JSON calendar loading
- ✅ Shows the exact file being fetched
- ✅ Reports HTTP response status codes
- ✅ Indicates cache-busting usage
- ✅ Counts and shows sample JSON entries
- ✅ Clear success/failure messages

#### XML Calendar Source Debugging

- ✅ Logs when falling back to XML
- ✅ Shows XML file being loaded
- ✅ Counts XML struct nodes processed
- ✅ Reports parsing warnings for invalid entries
- ✅ Shows sample XML entries parsed
- ✅ Clear success/failure messages

### Bell Times Source Debugging

#### JSON Bell Times Source Debugging

- ✅ Logs when attempting JSON bell times loading
- ✅ Shows configuration parameters
- ✅ Reports HTTP response status codes
- ✅ Shows metadata from API source
- ✅ Counts periods processed per day
- ✅ Clear success/failure messages

#### XML Bell Times Source Debugging

- ✅ Logs when falling back to XML
- ✅ Shows XML file being loaded
- ✅ Counts bell periods processed
- ✅ Reports day numbering and classifications
- ✅ Shows sample bell time entries
- ✅ Clear success/failure messages

## 🎯 Console Output Examples

### Calendar Debugging Examples

#### When JSON Calendar is Used:

```
🔧 CALENDAR DEBUG: Starting calendar data loading...
🔧 CALENDAR DEBUG: Configuration: {use_api: true, fallback_to_xml: true, api_file: "calendar.json", xml_file: "calendar.xml", cache_busting: false}
🗓️  CALENDAR DEBUG: Attempting to load calendar from JSON API source...
📁 CALENDAR DEBUG: Trying to fetch: calendar.json
📊 CALENDAR DEBUG: JSON fetch response status: 200
✅ CALENDAR DEBUG: Successfully loaded calendar from JSON API source
📈 CALENDAR DEBUG: JSON contains 10 calendar entries
🔧 CALENDAR DEBUG: Starting JSON calendar parsing...
📊 CALENDAR DEBUG: JSON metadata: {generated: "2025-08-22T02:06:06.849032", source: "sentral_api", total_days: 10}
📋 CALENDAR DEBUG: Processing 10 JSON calendar entries
✅ CALENDAR DEBUG: Successfully parsed 10 JSON calendar entries
🎯 CALENDAR DEBUG: Final decision - USING JSON CALENDAR
🎯 MAIN DEBUG: ===== CALENDAR SOURCE DECISION =====
📅 MAIN DEBUG: Using calendar data from: JSON (Sentral API)
📊 MAIN DEBUG: Calendar date range: 2025-08-22 to 2025-08-31
🎯 MAIN DEBUG: =====================================
```

#### When XML Calendar is Used (Fallback):

```
🔧 CALENDAR DEBUG: Starting calendar data loading...
🔧 CALENDAR DEBUG: Configuration: {use_api: true, fallback_to_xml: true, api_file: "calendar.json", xml_file: "calendar.xml", cache_busting: false}
🗓️  CALENDAR DEBUG: Attempting to load calendar from JSON API source...
📁 CALENDAR DEBUG: Trying to fetch: calendar.json
📊 CALENDAR DEBUG: JSON fetch response status: 404
⚠️  CALENDAR DEBUG: JSON calendar file calendar.json not found (404)
🗓️  CALENDAR DEBUG: Falling back to XML calendar source...
📁 CALENDAR DEBUG: Trying to fetch XML: calendar.xml
✅ CALENDAR DEBUG: Successfully loaded calendar from XML fallback source
🔧 CALENDAR DEBUG: Starting XML calendar parsing...
📋 CALENDAR DEBUG: Found 365 XML struct nodes to process
✅ CALENDAR DEBUG: Successfully parsed 365 XML calendar entries
🎯 CALENDAR DEBUG: Final decision - USING XML CALENDAR
🎯 MAIN DEBUG: ===== CALENDAR SOURCE DECISION =====
📅 MAIN DEBUG: Using calendar data from: XML (calendar.xml)
📊 MAIN DEBUG: Calendar date range: 2025-01-01 to 2025-12-31
🎯 MAIN DEBUG: =====================================
```

### Bell Times Debugging Examples

#### When JSON Bell Times is Used:

```
� BELL TIMES DEBUG: Starting bell times data loading...
� BELL TIMES DEBUG: Configuration: {use_api: true, fallback_to_xml: true, api_file: "bell_times.json", xml_file: "bell_times.xml"}
⏰ BELL TIMES DEBUG: Attempting to load bell times from JSON API source...
📁 BELL TIMES DEBUG: Trying to fetch: bell_times.json
📊 BELL TIMES DEBUG: JSON fetch response status: 200
✅ BELL TIMES DEBUG: Successfully loaded bell times from JSON API source
📈 BELL TIMES DEBUG: JSON contains bell times data
🔧 BELL TIMES DEBUG: Starting JSON bell times parsing...
📊 BELL TIMES DEBUG: JSON metadata: {generated: "2025-01-10T07:30:15.123456", source: "sentral_api", total_days: 7}
📋 BELL TIMES DEBUG: Processing bell times for 7 days
✅ BELL TIMES DEBUG: Successfully parsed JSON bell times data
🎯 BELL TIMES DEBUG: Final decision - USING JSON BELL TIMES
🎯 MAIN DEBUG: ===== BELL TIMES SOURCE DECISION =====
🔔 MAIN DEBUG: Using bell times data from: JSON (Sentral API)
📊 MAIN DEBUG: Bell times available for 7 day types
🎯 MAIN DEBUG: =====================================
```

#### When XML Bell Times is Used (Fallback):

```
🔔 BELL TIMES DEBUG: Starting bell times data loading...
🔔 BELL TIMES DEBUG: Configuration: {use_api: true, fallback_to_xml: true, api_file: "bell_times.json", xml_file: "bell_times.xml"}
⏰ BELL TIMES DEBUG: Attempting to load bell times from JSON API source...
📁 BELL TIMES DEBUG: Trying to fetch: bell_times.json
� BELL TIMES DEBUG: JSON fetch response status: 404
⚠️  BELL TIMES DEBUG: JSON bell times file bell_times.json not found (404)
🔔 BELL TIMES DEBUG: Falling back to XML bell times source...
📁 BELL TIMES DEBUG: Trying to fetch XML: bell_times.xml
✅ BELL TIMES DEBUG: Successfully loaded bell times from XML fallback source
🔧 BELL TIMES DEBUG: Starting XML bell times parsing...
📋 BELL TIMES DEBUG: Found bell times XML structure
✅ BELL TIMES DEBUG: Successfully parsed XML bell times data
🎯 BELL TIMES DEBUG: Final decision - USING XML BELL TIMES
🎯 MAIN DEBUG: ===== BELL TIMES SOURCE DECISION =====
🔔 MAIN DEBUG: Using bell times data from: XML (bell_times.xml)
📊 MAIN DEBUG: Bell times available for traditional structure
🎯 MAIN DEBUG: =====================================
```

## 🛠️ Testing and Usage

### Enable Debugging (Development/Testing)

1. **Edit config.json**:

   ```json
   {
     "ui": {
       "debug": true
     }
   }
   ```

2. **Reload the timetable kiosk**

3. **Open Developer Tools (F12) → Console**

4. **View detailed debug output for both calendar and bell times**

### Disable Debugging (Production)

1. **Edit config.json**:

   ```json
   {
     "ui": {
       "debug": false
     }
   }
   ```

2. **Reload the timetable kiosk**

3. **Console will be clean** - no debug messages displayed

### Testing Calendar Sources

#### Test JSON Calendar Usage (Default)

```bash
# Start server and open in browser
python -m http.server 8000
# Open http://localhost:8000
# Check browser console for JSON calendar debug messages
```

#### Test XML Calendar Fallback

1. **Rename calendar.json temporarily:**

   ```bash
   mv calendar.json calendar.json.backup
   ```

2. **Reload page and check console for XML fallback messages**

3. **Restore JSON file:**
   ```bash
   mv calendar.json.backup calendar.json
   ```

### Testing Bell Times Sources

#### Test JSON Bell Times Usage

```bash
# Ensure bell_times.json exists
ls -la bell_times.json
# Reload page and check console for JSON bell times debug messages
```

#### Test XML Bell Times Fallback

1. **Rename bell_times.json temporarily:**

   ```bash
   mv bell_times.json bell_times.json.backup
   ```

2. **Reload page and check console for XML fallback messages**

3. **Restore JSON file:**
   ```bash
   mv bell_times.json.backup bell_times.json
   ```

### Quick Toggle Commands

#### Enable Debug via Python:

```python
import json
with open('config.json', 'r') as f:
    config = json.load(f)
config['ui']['debug'] = True
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)
```

#### Disable Debug via Python:

```python
import json
with open('config.json', 'r') as f:
    config = json.load(f)
config['ui']['debug'] = False
with open('config.json', 'w') as f:
    json.dump(config, f, indent=2)
```

## 🔍 Debug Information Provided

When enabled, the debug system shows:

### For Calendar Data:

- **Configuration Settings**: All calendar-related config parameters
- **File Operations**: Which files are being fetched and their status
- **HTTP Responses**: Network request results and status codes
- **Data Processing**: Number of entries processed from each source
- **Source Decision**: Clear indication of JSON vs XML usage
- **Sample Data**: Examples of parsed calendar entries
- **Metadata**: Generation timestamps and data source information

### For Bell Times Data:

- **Configuration Settings**: Bell times API and fallback settings
- **File Operations**: JSON and XML file fetch attempts
- **HTTP Responses**: API response status and metadata
- **Data Processing**: Number of periods and days processed
- **Source Decision**: Clear indication of JSON vs XML usage
- **Sample Data**: Examples of bell time entries
- **Metadata**: Generation timestamps and source information

## 🎯 How to Use the Debugging

1. **Open Browser Developer Tools** (F12)
2. **Go to Console tab**
3. **Load the timetable kiosk**
4. **Look for debug messages starting with:**
   - `🔧 CALENDAR DEBUG:` - Calendar configuration and parsing details
   - `🔔 BELL TIMES DEBUG:` - Bell times configuration and parsing details
   - `📅 MAIN DEBUG:` - Final calendar source decision
   - `🔔 MAIN DEBUG:` - Final bell times source decision
   - `🎯 MAIN DEBUG:` - Summary sections

## 🎉 Benefits

### For Development:

- **Troubleshooting**: Easy to see which data sources are being used
- **Configuration Validation**: Debug shows all config parameters
- **Performance Monitoring**: Track loading times and success/failure
- **Data Validation**: See sample entries and metadata
- **API Integration**: Monitor JSON API responses and fallback behavior

### For Production:

- **Clean Console**: Professional appearance with no debug noise
- **Performance**: No unnecessary console output overhead
- **User Experience**: No debug information confusing end users
- **Maintainability**: Debug can be toggled without code changes

This comprehensive debugging system makes it clear whether the kiosk is using the new JSON data from the Sentral API or falling back to the traditional XML files for both calendar and bell times data sources.

## 🤖 GitHub Actions Issues

### Git Conflict Errors (Fixed in v2.1)

If GitHub Actions fail with errors like:

```
error: Your local changes to the following files would be overwritten by merge:
    .logs/liss_info_generation.log
    liss_info.json
Please commit your changes or stash them before you merge.
```

**This issue has been resolved** in version 2.1 of the workflows. The actions now:

1. **Automatically stash** local changes before pulling updates
2. **Pull latest changes** from the remote repository
3. **Restore stashed files** with the newly generated data
4. **Commit and push** successfully without conflicts

### Updating to Fixed Workflows

If you're still experiencing git conflicts:

1. **Check your workflow files** are up to date
2. **Compare with the latest versions** in the repository
3. **Update the workflow files** if needed:
   - `.github/workflows/liss-timetable-updates.yml`
   - `.github/workflows/weekly-data-update.yml`

### Workflow Debugging

**Check workflow status**:

1. Go to **Actions** tab in your GitHub repository
2. Click on the failed workflow run
3. Expand the failing step to see detailed logs

**Common workflow issues**:

- **Invalid API key**: Check `REST_API_KEY` secret is set correctly
- **Network timeouts**: Retry the workflow manually
- **Permissions**: Ensure workflow has `contents: write` permission
- **File conflicts**: Should be automatically resolved in v2.1+

### Manual Recovery

If workflows are still failing after updating:

1. **Clear any stale data**:

   ```bash
   git stash clear
   git reset --hard origin/main
   ```

2. **Re-run the workflow** manually from the Actions tab

3. **Check the logs** for any remaining issues

## 🔄 Data Update Scheduling

### Current Schedule

**LISS Timetable Updates**: Every 15 minutes during school hours (7:30 AM - 3:30 PM Sydney time, weekdays only)

**Weekly Data Updates**: Every Monday at 5:00 AM Sydney time

### Time Zone Handling

The workflows automatically handle Sydney time zone changes:

- **AEST (Standard Time)**: UTC+10
- **AEDT (Daylight Saving Time)**: UTC+11

Both schedules are included in the cron expressions to ensure consistent operation year-round.

### Manual Triggers

You can trigger any workflow manually:

1. Go to **Actions** tab
2. Select the workflow
3. Click **Run workflow**
4. Choose the branch (usually `main`)
5. Click **Run workflow**
