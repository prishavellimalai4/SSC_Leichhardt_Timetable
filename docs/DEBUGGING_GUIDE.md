# Debugging Guide

## Overview

The Tempe HS Timetable Kiosk includes a comprehensive debugging system for both calendar and bell times data sources. This guide covers how to enable, use, and interpret debug output for troubleshooting and development.

## ✅ Debug Configuration System

### Configuration in config.json

```json
{
  "ui": {
    "refreshInterval": 60000,
    "cacheBusting": false,
    "debug": false,
    "responsive": {
      // ... other settings
    }
  }
}
```

- **Default**: `"debug": false` (production-ready, clean console)
- **Development**: Set `"debug": true` to enable detailed logging

### Smart Debug Functions

```javascript
// Conditional debug logging - only outputs when CONFIG.ui.debug is true
function debugLog(message, ...args) {
  if (CONFIG && CONFIG.ui && CONFIG.ui.debug) {
    console.log(message, ...args);
  }
}

function debugWarn(message, ...args) {
  if (CONFIG && CONFIG.ui && CONFIG.ui.debug) {
    console.warn(message, ...args);
  }
}

function debugError(message, ...args) {
  if (CONFIG && CONFIG.ui && CONFIG.ui.debug) {
    console.error(message, ...args);
  }
}
```

## 🔧 Data Source Debugging

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
