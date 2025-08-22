# LISS Integration Guide

Advanced timetable integration for schools using LISS (Learning Information Systems Standard) with Sentral.

## 🎯 What Is LISS?

LISS provides detailed timetable data including:

- Individual student timetables
- Teacher assignments
- Room allocations
- Subject codes and periods
- Year group organization

## ⚡ Quick Setup

### Generate LISS Data

Run the optimized LISS generator:

```bash
python generate_liss_info.py
```

This creates `liss_info.json` with complete timetable data for your school.

### Performance Features

- **⚡ 20x faster**: ~1.3 seconds vs 26+ seconds
- **📉 95% fewer API calls**: ~10 calls vs 700+ calls
- **🔧 Bulk operations**: Uses Sentral API include parameters
- **📊 Complete logging**: Generation and validation logs

## 🔧 Configuration

### Basic Setup (`sentral_config.json`)

```json
{
  "base_url": "https://<your-school-sentral>/",
  "api_key": "your-api-key-here",
  "endpoints": {
    "liss_info": "restapi/v1/liss/info"
  }
}
```

### Advanced Options

Edit `generate_liss_info.py` for customization:

- **Days ahead**: How many days to fetch (default: 7)
- **Year groups**: Which years to include (default: all)
- **Data filtering**: Exclude specific periods or subjects

Requires `sentral_config.json` with:

- Sentral API credentials
- School endpoint configuration
- Data range settings (days_ahead: 7)

### Output Format

Creates `liss_info.json` with optimized structure:

```json
{
  "metadata": {
    "school": "TEMPE",
    "generated_at": "2025-08-22T04:43:26.856133",
    "source": "sentral_api_optimized",
    "total_lessons": 350,
    "date_range": "2025-08-22 to 2025-08-29",
    "optimization": "Used includes and bulk operations",
    "api_calls_reduced": "From 700+ to 6 calls total"
  },
  "timetable_data": [
    {
      "DayNumber": 1,
      "Period": "P1",
      "ClassCode": "9MU1",
      "EdvalClassCode": "9MU1",
      "TeacherCode": "LADO",
      "RoomCode": "P5"
    }
  ]
}
```

### Performance Features

- **Bulk API Operations**: Single API call fetches lessons + teachers + classes + rooms
- **Smart Caching**: Reduces redundant API calls
- **Validation**: Automatic data integrity checks
- **Comprehensive Logging**: Timestamped logs with response codes and validation results

## 📊 Edval LISS Bell Times Integration

### Basic Usage

```bash
# Fetch bell times using default config
python3 liss_bell_times.py

# Test connection only
python3 liss_bell_times.py --test-only

# Use custom config file
python3 liss_bell_times.py --config my_config.json
```

### Configuration

#### Method 1: Environment Variables (Recommended)

For security, store credentials in environment variables:

1. **Set environment variables:**

   ```bash
   export LISS_USERNAME=your_username
   export LISS_PASSWORD=your_password
   ```

2. **Configure `liss_config.json` to use environment variables:**

   ```json
   {
     "liss": {
       "endpoint": "https://tempehs-nsw.edval.education/liss",
       "school": "TEMPE",
       "username_env": "LISS_USERNAME",
       "password_env": "LISS_PASSWORD",
       "liss_version": 10002,
       "user_agent": "web.edval",
       "tt_structure": "main"
     },
     "output": {
       "format": "json",
       "file": "current_bell_times.json",
       "pretty_print": true
     },
     "logging": {
       "enabled": true,
       "level": "INFO"
     }
   }
   ```

3. **Or use a .env file** (copy `.env.example` to `.env` and edit):
   ```bash
   cp .env.example .env
   # Edit .env with your credentials
   source .env
   ```

#### Method 2: Direct Configuration (Less Secure)

You can also store credentials directly in the config file (not recommended for production):

```json
{
  "liss": {
    "endpoint": "https://tempehs-nsw.edval.education/liss",
    "school": "TEMPE",
    "username": "your_username",
    "password": "your_password",
    "liss_version": 10002,
    "user_agent": "web.edval",
    "tt_structure": "main"
  }
}
```

## Requirements

- Python 3.6+
- `requests` library: `sudo apt install python3-requests`

## Troubleshooting

### Academic Year Issues

If you get errors about "academic year" or "check the academic year of that file":

1. **Verify credentials** - Your username/password may be scoped to a specific academic year
2. **Contact IT** - Request credentials for the current academic year (2025)
3. **Check data availability** - Ensure 2025 bell times have been imported into Edval

### TimetableStructure Issues

If you get errors about invalid TimetableStructure:

1. **Run test mode** to see available structures:
   ```bash
   python3 liss_bell_times.py --test-only
   ```
2. **Update config** with a valid structure name
3. **Common structures**: `main`, `Main`, `Secondary`, `Primary`, `Default`

### Connection Issues

- Check network connectivity to the Edval server
- Verify the endpoint URL is correct
- Ensure firewall allows HTTPS connections

## Output Format

The script saves bell times to a JSON file with this structure:

```json
{
  "metadata": {
    "fetched_at": "2025-08-20T03:55:03.123456",
    "source": "LISS API",
    "school": "TEMPE",
    "tt_structure": "main",
    "total_entries": 50
  },
  "bell_times": [
    {
      "DayNumber": 1,
      "DayName": "MonA",
      "Period": "P1",
      "StartTime": "08:45",
      "EndTime": "09:40",
      "Type": "T"
    }
  ]
}
```

## Integration with Timetable Kiosk

The bell times JSON can be used by your main timetable kiosk application to display current bell times and determine which period is currently active.

## Technical Notes

- Uses JSON-RPC 2.0 protocol as specified by LISS
- Implements proper error handling and logging
- Handles Edval-specific authentication requirements
- Compatible with LISS specification version 0.9.3
