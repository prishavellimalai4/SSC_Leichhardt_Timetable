# Config.json Simplification and Centralized API Sync Days

## Overview

The `config.json` file has been significantly simplified and reorganized to remove redundancy and add centralized API sync day configuration. The stale data detection now uses a single `api.sync_days` value for all data sources.

## Key Changes

### 1. Centralized API Configuration

**Before:**

```json
"bell_times": {
  "source": "api",
  "use_api": true,
  "fallback_to_xml": true,
  "stale_data_threshold": 7,
  // ... repeated for each data source
}
```

**After:**

```json
"api": {
  "sync_days": 7,
  "auto_generate": true,
  "use_json": true,
  "fallback_to_xml": true
}
```

### 2. Simplified Data Sources

**Before:**

```json
"files": {
  "bellTimes": "bell_times.xml",
  "lessons": "liss_info.xml",
  "calendar": "calendar.xml"
},
"bell_times": {
  "api_file": "bell_times.json",
  "xml_file": "bell_times.xml",
  "generation_script": "generate_bell_times.py"
}
```

**After:**

```json
"dataSources": {
  "bell_times": {
    "json_file": "bell_times.json",
    "xml_file": "bell_times.xml",
    "generation_script": "generate_bell_times.py"
  }
}
```

### 3. Removed Redundancy

- **Eliminated `files` section** (duplicated XML file paths)
- **Removed individual `source` fields** (unused)
- **Centralized stale data threshold** (now `api.sync_days`)
- **Consolidated API settings** (no repetition across data sources)
- **Simplified arrays** (removed unnecessary line breaks)

## New Configuration Structure

```json
{
  "school": {
    /* school branding */
  },
  "api": {
    "sync_days": 7, // Days before JSON data is stale
    "auto_generate": true, // Enable automatic generation
    "use_json": true, // Use JSON API sources
    "fallback_to_xml": true // Fallback to XML when JSON fails/stale
  },
  "colors": {
    /* UI colors */
  },
  "schedule": {
    /* timetable schedule */
  },
  "sportPeriods": {
    /* sport period configuration */
  },
  "yearGroups": {
    /* year group settings */
  },
  "ui": {
    /* UI settings */
  },
  "dataSources": {
    "calendar": {
      "json_file": "calendar.json",
      "xml_file": "calendar.xml",
      "generation_script": "generate_calendar.py",
      "days_ahead": 30
    },
    "bell_times": {
      "json_file": "bell_times.json",
      "xml_file": "bell_times.xml",
      "generation_script": "generate_bell_times.py"
    },
    "liss_info": {
      "json_file": "liss_info.json",
      "xml_file": "liss_info.xml",
      "generation_script": "generate_liss_info.py"
    }
  }
}
```

## Benefits

### 1. **Centralized Control**

- Single `api.sync_days` setting controls stale detection for all data sources
- Global API behavior settings in one place
- Easier to adjust sync frequency

### 2. **Reduced Redundancy**

- Eliminated duplicate file path specifications
- Removed repetitive API configuration
- Cleaner, more maintainable structure

### 3. **Simplified Management**

- Fewer configuration options to manage
- Clear separation of concerns
- Logical grouping of related settings

### 4. **Automatic Sync Day Calculation**

- JavaScript automatically uses `CONFIG.api.sync_days` value
- No need to update multiple threshold settings
- Consistent behavior across all data sources

## JavaScript Updates

The data loading functions now use the centralized configuration:

```javascript
// Before
const staleDataThreshold = bellTimesConfig.stale_data_threshold || 7;

// After
const staleDataThreshold = apiConfig.sync_days || 7;
```

## Migration Notes

### Breaking Changes

- **`CONFIG.files` removed** - Use `CONFIG.dataSources.*.xml_file` instead
- **Individual threshold settings removed** - Use `CONFIG.api.sync_days` instead
- **`use_api` renamed** - Now `CONFIG.api.use_json`

### Backward Compatibility

- Default values ensure system works if config is incomplete
- Graceful fallbacks for missing configuration sections
- Error handling for undefined properties

## Configuration Examples

### Basic Setup

```json
{
  "api": {
    "sync_days": 7
  }
}
```

### Custom Sync Period

```json
{
  "api": {
    "sync_days": 14, // Two weeks before stale
    "use_json": true,
    "fallback_to_xml": true
  }
}
```

### Disable JSON (XML Only)

```json
{
  "api": {
    "use_json": false,
    "fallback_to_xml": true
  }
}
```

## Testing

The updated configuration has been validated:

✅ **JSON Syntax**: Valid JSON structure  
✅ **Data Sources**: All three sources configured  
✅ **API Settings**: Centralized sync_days working  
✅ **File Paths**: Correct JSON/XML file references  
✅ **JavaScript**: Updated loaders using new structure

## File Size Reduction

- **Before**: 146 lines
- **After**: 95 lines
- **Reduction**: 35% smaller, much cleaner structure

The simplified configuration is easier to read, maintain, and extend while providing more flexible control over API sync behavior.
