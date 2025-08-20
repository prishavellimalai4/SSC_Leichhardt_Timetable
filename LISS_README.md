# LISS Bell Times Integration

This directory contains the LISS (Learning Information Systems Standard) integration for fetching bell times from the Edval timetabling system.

## Files

- **`liss_bell_times.py`** - Main script to fetch bell times from LISS API
- **`liss_config.json`** - Configuration file with LISS connection parameters
- **`bell_times.xml`** - Example XML output from LISS (for reference)

## Usage

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
