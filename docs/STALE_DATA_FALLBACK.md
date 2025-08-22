# Automatic Data Fallback System

How the kiosk ensures reliable data display even when primary sources are outdated.

## 🎯 How It Works

The kiosk uses a smart fallback system to always show relevant data:

1. **Primary**: JSON files from API (most current)
2. **Fallback**: XML files when JSON is stale
3. **Backup**: Sample data if nothing else works

## ⚙️ Stale Data Detection

### What Makes Data "Stale"

Data is considered stale when it's older than the configured threshold:

**Default**: 7 days (configurable in `config.json`)

```json
{
  "api": {
    "sync_days": 7
  }
}
```

### Automatic Detection

The system checks timestamps in JSON metadata:

- `liss_info.json`: Uses `metadata.generated_at`
- `bell_times.json`: Uses `metadata.generated_at`
- `calendar.json`: Uses `metadata.generated`

## 🔄 Fallback Process

### Step-by-Step Process

1. **Try JSON first**: Load JSON data files
2. **Check freshness**: Compare timestamp with current date
3. **Detect staleness**: If older than `sync_days` threshold
4. **Switch to XML**: Automatically load XML equivalent
5. **Log decision**: Record why fallback occurred

### File Mapping

| JSON File         | XML Fallback     | Purpose          |
| ----------------- | ---------------- | ---------------- |
| `liss_info.json`  | `liss_info.xml`  | Timetable data   |
| `bell_times.json` | `bell_times.xml` | Period schedules |
| `calendar.json`   | `calendar.xml`   | School calendar  |

## 🛠️ Configuration

### Basic Settings

Edit `config.json` to control fallback behavior:

```json
{
  "api": {
    "sync_days": 7,
    "fallback_to_xml": true
  }
}
```

**Options**:

- `sync_days`: How many days before data is "stale"
- `fallback_to_xml`: Enable/disable automatic fallback

### Data Source Configuration

The kiosk automatically knows which files to use:

```json
{
  "dataSources": {
    "calendar": {
      "json_file": "calendar.json",
      "xml_file": "calendar.xml"
    },
    "bell_times": {
      "json_file": "bell_times.json",
      "xml_file": "bell_times.xml"
    },
    "liss_info": {
      "json_file": "liss_info.json",
      "xml_file": "liss_info.xml"
    }
  }
}
```

## 🔍 Troubleshooting

### Check Current Data Age

Enable debug mode to see data freshness:

```json
{
  "ui": {
    "debug": true
  }
}
```

Look for console messages about:

- Data load attempts
- Staleness detection
- Fallback decisions

### Force Refresh

**Update JSON data**:

```bash
python generate_liss_info.py
python generate_bell_times.py
python generate_calendar.py
```

**Download fresh XML**:

- Get files from `https://<your-school-sentral>/ABCDE/timetables/`
- Replace existing XML files

### Common Issues

**"Data always stale"**:

- Check system clock is correct
- Verify JSON metadata timestamps
- Ensure generation scripts ran successfully

**"Fallback not working"**:

- Verify XML files exist and contain valid data
- Check `fallback_to_xml` is enabled in config
- Enable debug mode to see error details

## 📋 Benefits

**Reliability**: Kiosk always shows useful information
**Maintenance**: Reduces need for manual intervention  
**Flexibility**: Works with various data update schedules
**Transparency**: Debug logging shows all decisions
"xml_file": "liss_info.xml",
"generation_script": "generate_liss_info.py"
}
}
}

```

**Key Settings:**

- **`api.sync_days`**: Number of days before JSON data is considered stale (default: 7)
- **`api.use_json`**: Enable JSON API loading (default: true)
- **`api.fallback_to_xml`**: Enable XML fallback when JSON fails or is stale (default: true)
- **`dataSources`**: File paths and scripts for each data source

```

## Benefits

### Reliability During API Outages

- **Continuous Operation**: Kiosk continues working even when API fails for extended periods
- **Relevant Data**: Falls back to longer-term XML data instead of displaying outdated short-term JSON
- **Automatic Recovery**: No manual intervention required

### Configurable Thresholds

- **Flexible Timing**: Each data source can have different staleness thresholds
- **School-Specific**: Adjust based on your school's timetable update cycles
- **Easy Changes**: Modify thresholds without code changes

## Debug Information

When debug mode is enabled (`config.ui.debug: true`), the system logs:

```

🕐 STALE CHECK: Data generated at 2025-08-15T07:05:20.479629, age: 8.2 days
⚠️ STALE CHECK: Data is 8.2 days old (exceeds 7 day limit)
⚠️ LISS DEBUG: JSON data is stale (older than 7 days), falling back to XML
🎯 LISS DEBUG: Final decision - USING XML LISS DATA

```

## Use Cases

### Scenario 1: Weekend API Outage

- **Friday**: Last JSON generation
- **Monday**: JSON is 3 days old (fresh)
- **Tuesday**: JSON is 4 days old (fresh)
- **Wednesday**: JSON is 5 days old (fresh)
- **Next Monday**: JSON is 10 days old (stale → XML fallback)

### Scenario 2: Extended Maintenance

- **API down for 2 weeks**: Automatic XML fallback after 7 days
- **API restored**: Next successful generation switches back to JSON
- **No manual intervention**: System handles transition automatically

### Scenario 3: Metadata Issues

- **Missing timestamp**: Treated as stale (XML fallback)
- **Invalid timestamp**: Treated as stale (XML fallback)
- **Corrupted metadata**: Treated as stale (XML fallback)

## Technical Implementation

### Functions Added

1. **`isDataStale(metadata, maxAgeDays)`**

   - Checks timestamp age against threshold
   - Handles different timestamp formats
   - Returns `true` for stale data, `false` for fresh

2. **Enhanced Data Loaders**
   - `loadBellTimesData()`: Checks bell times freshness
   - `loadLissData()`: Checks LISS data freshness
   - `loadCalendarData()`: Checks calendar freshness

### Error Handling

- **Parse Errors**: Invalid timestamps treated as stale
- **Missing Metadata**: No metadata treated as stale
- **Network Errors**: Standard fallback logic applies
- **JSON Format Errors**: Standard fallback logic applies

## Testing

Use the included test file to verify stale data detection:

```bash
# Open in browser
file:///workspaces/Tempe_HS_Timetable_Kiosk/test_stale_data.html
```

Test cases include:

- Fresh data (today)
- 3-day old data (fresh)
- 8-day old data (stale)
- 15-day old data (stale)
- Missing metadata (stale)
- Invalid timestamps (stale)

## Monitoring

Monitor the system by:

1. **Enable Debug Mode**: Set `config.ui.debug: true`
2. **Check Browser Console**: Look for stale data warnings
3. **Monitor Data Sources**: Check which source is being used
4. **Verify Timestamps**: Ensure JSON files have current timestamps

## Migration Notes

### Existing Systems

- **No Breaking Changes**: Feature is backward compatible
- **Default Behavior**: 7-day threshold if not configured
- **Gradual Rollout**: Can be enabled per data source

### Configuration Updates

```json
// Centralized API configuration
"api": {
  "sync_days": 7,        // Days before data is stale
  "use_json": true,      // Enable JSON loading
  "fallback_to_xml": true // Enable XML fallback
}

// Data source file paths
"dataSources": {
  "calendar": {
    "json_file": "calendar.json",
    "xml_file": "calendar.xml"
  }
  // ... other sources
}
```

## Troubleshooting

### Common Issues

1. **Always Using XML**

   - Check JSON file timestamps
   - Verify threshold configuration
   - Enable debug logging

2. **Never Using XML**

   - Check `fallback_to_xml: true` setting
   - Verify XML files exist
   - Check XML file accessibility

3. **Incorrect Timestamps**
   - Verify generation script timestamps
   - Check timezone handling
   - Validate ISO format compliance

### Debug Commands

```javascript
// Check current data age in browser console
fetch("liss_info.json")
  .then((r) => r.json())
  .then((d) => {
    const age =
      (new Date() - new Date(d.metadata.generated_at)) / (1000 * 60 * 60 * 24);
    console.log(`Data is ${age.toFixed(1)} days old`);
  });
```

## Future Enhancements

- **Smart Thresholds**: Different thresholds for different periods
- **Notification System**: Alert administrators about stale data
- **Health Dashboard**: Visual status of data freshness
- **Automatic Recovery**: Attempt JSON reload after XML fallback
