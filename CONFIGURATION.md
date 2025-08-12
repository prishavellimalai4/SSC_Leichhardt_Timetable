# School Timetable Kiosk Configuration Guide

This guide explains how to configure the Tempe High School Timetable Kiosk for use by other schools.

## Configuration File

The app uses a `config.json` file to store all school-specific settings. This file must be placed in the same directory as `index.html`.

## Configuration Options

### School Information

```json
{
  "school": {
    "name": "Your School Name",
    "logo": {
      "url": "https://your-school.edu/logo.png",
      "opacity": 0.15,
      "size": "auto 100vh"
    }
  }
}
```

- **name**: The school name that appears in the browser title
- **logo.url**: Direct URL to your school's logo image
- **logo.opacity**: Logo transparency (0.0 to 1.0)
- **logo.size**: CSS background-size property for the logo

### Colors and Styling

```json
{
  "colors": {
    "primary": "#AC0000",
    "background": "#f7f8fc",
    "overlay": "rgba(247, 248, 252, 0.3)",
    "tile": {
      "background": "#EDEDEE",
      "border": "#555",
      "shadow": "#b5b7b9",
      "hover": "#EDEDEE"
    },
    "text": {
      "primary": "#1a2325",
      "secondary": "#b5b7b9",
      "classCode": "#AC0000"
    }
  }
}
```

- **primary**: Main school color (used for year labels and class codes)
- **background**: Page background color
- **overlay**: Semi-transparent overlay color
- **tile**: Colors for class tiles (background, border, shadow, hover effect)
- **text**: Text colors for different elements

### Schedule Configuration

```json
{
  "schedule": {
    "ignoredDays": [0, 6],
    "schoolDays": [1, 2, 3, 4, 5],
    "defaultShowMinutesBefore": 10,
    "periods": {
      "P0": {
        "showFromDay": 5,
        "showFromTime": "15:05",
        "showUntilStart": true,
        "description": "Period 0"
      },
      "P1": {
        "showFromTime": "08:20",
        "description": "Period 1"
      }
    }
  }
}
```

- **ignoredDays**: Array of days to skip (0=Sunday, 1=Monday, ..., 6=Saturday)
- **schoolDays**: Array of school days
- **defaultShowMinutesBefore**: How many minutes before a period starts to show it
- **periods**: Special configurations for specific periods
  - **showFromDay**: Day of week to start showing this period (for cross-day periods)
  - **showFromTime**: Time to start showing the period (HH:MM format)
  - **showUntilStart**: Whether to show until the period actually starts
  - **description**: Display name for the period

### Sport Periods

```json
{
  "sportPeriods": {
    "tuesday": {
      "periods": ["P5", "P6"],
      "yearGroups": {
        "7": {
          "label": "Year 7 & 8 Sport",
          "includesYears": [7, 8],
          "excludeYears": [8]
        },
        "9": {
          "label": "Year 9 & 10 Sport", 
          "includesYears": [9, 10],
          "excludeYears": [10]
        }
      }
    }
  }
}
```

Configure special periods like sport where year groups are combined:

- **periods**: Array of period codes that are sport periods
- **yearGroups**: Configuration for each year group
  - **label**: Display name for the combined years
  - **includesYears**: Years that should show under this label
  - **excludeYears**: Years to exclude from showing individual classes

### Year Groups

```json
{
  "yearGroups": {
    "multiRowYears": [7, 9],
    "displayYears": [7, 8, 9, 10, 11, 12],
    "classCodePattern": "^(\\d+)"
  }
}
```

- **multiRowYears**: Year groups that should display in multiple rows instead of single row
- **displayYears**: Which year levels to display
- **classCodePattern**: Regex pattern to extract year from class codes

### User Interface

```json
{
  "ui": {
    "refreshInterval": 60000,
    "cacheBusting": true,
    "responsive": {
      "breakpoints": {
        "large": 1700,
        "medium": 1280,
        "small": 700
      }
    }
  }
}
```

- **refreshInterval**: How often to refresh the page (milliseconds)
- **cacheBusting**: Whether to add timestamps to prevent caching
- **responsive.breakpoints**: Screen size breakpoints for responsive design

### Data Files

```json
{
  "files": {
    "bellTimes": "bell_times.xml",
    "lessons": "liss_info.xml",
    "calendar": "calendar.xml"
  }
}
```

- **bellTimes**: Filename for bell times XML
- **lessons**: Filename for lessons XML  
- **calendar**: Filename for calendar XML

## Example Configurations

### Different School Example

```json
{
  "school": {
    "name": "Riverside Secondary College",
    "logo": {
      "url": "https://riverside-sc.edu.au/assets/logo.png",
      "opacity": 0.2,
      "size": "contain"
    }
  },
  "colors": {
    "primary": "#003366",
    "background": "#f0f4f8",
    "text": {
      "classCode": "#003366"
    }
  },
  "schedule": {
    "ignoredDays": [0, 6],
    "defaultShowMinutesBefore": 15,
    "periods": {
      "HR": {
        "showFromTime": "08:30",
        "description": "Home Room"
      }
    }
  },
  "yearGroups": {
    "displayYears": [8, 9, 10, 11, 12],
    "multiRowYears": [8, 10]
  }
}
```

### Primary School Example

```json
{
  "school": {
    "name": "Sunshine Primary School",
    "logo": {
      "url": "https://sunshine-ps.edu.au/logo.svg",
      "opacity": 0.1
    }
  },
  "colors": {
    "primary": "#FF6B35",
    "background": "#FFF8E1"
  },
  "yearGroups": {
    "displayYears": [1, 2, 3, 4, 5, 6],
    "multiRowYears": [1, 3, 5],
    "classCodePattern": "^(\\d+)"
  }
}
```

## Setup Instructions

1. **Copy the base files**: `index.html`, `config.json`, and your XML data files
2. **Customize config.json**: Update all settings for your school
3. **Update XML files**: Ensure your bell times, lessons, and calendar data are in the correct format
4. **Test locally**: Use a local web server to test the configuration
5. **Deploy**: Upload all files to your web server

## Testing

The app includes a manual override feature for testing different times and dates. Set `USE_MANUAL_OVERRIDE = true` in the JavaScript section and configure the test date/time.

## Fallback Behavior

If `config.json` cannot be loaded, the app will fall back to the default Tempe High School configuration to ensure it still functions.

## File Structure

```
school-timetable/
├── index.html
├── config.json
├── bell_times.xml
├── liss_info.xml
├── calendar.xml
└── README.md
```

## Support

The configuration system is designed to be flexible and support various school structures. If you need additional configuration options, you can extend the `config.json` file and modify the JavaScript code accordingly.
