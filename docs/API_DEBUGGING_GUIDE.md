# API Debugging Guide

This document explains the enhanced debugging features added to help diagnose API issues in GitHub Actions.

## 🐛 Debug Mode

### Enabling Debug Mode

**For local testing:**

```bash
# Set environment variable
export LISS_DEBUG=true
python3 generate_liss_info.py

# Or use command line flag
python3 generate_liss_info.py --debug
```

**For GitHub Actions:**
Debug mode is automatically enabled in the workflow via the `LISS_DEBUG=true` environment variable.

### What Debug Mode Shows

When debug mode is enabled, you'll see:

1. **🔧 API Client Initialization**

   - Base URL and tenant information
   - API key length (for validation)
   - Session headers

2. **📡 Request Details**

   - Request number and method
   - Full URL being called
   - Query parameters
   - Request body (if applicable)
   - Timeout settings
   - Retry attempt information

3. **📊 Response Information**

   - HTTP status code
   - Response time in seconds
   - Response headers
   - Response size in bytes
   - Number of records returned
   - Pagination information

4. **🔄 Retry Logic**

   - Exponential backoff timing (2s, 4s, 8s)
   - Rate limiting detection and handling
   - Server error retry attempts

5. **📈 Statistics**
   - Total requests made
   - Total time spent on API calls
   - Average request time

## 🚨 Error Handling Improvements

### New Error Types Detected

- **⏰ Timeout Errors**: Shows actual timeout duration vs limit
- **🔌 Connection Errors**: Network connectivity issues
- **🔧 Server Errors (5xx)**: Automatic retry with exponential backoff
- **⏰ Rate Limiting (429)**: Respects Retry-After header
- **❌ Client Errors (4xx)**: No retry, immediate failure

### Enhanced Error Messages

Each error now includes:

- Error type and classification
- Request duration when error occurred
- Retry attempt information
- Specific error details
- Troubleshooting context

## 📋 GitHub Actions Enhancements

### Pre-Flight Checks

Before running the LISS generation, the action now performs:

1. **🖥️ System Information**

   - OS details, Python version
   - Current time in multiple timezones
   - Memory and disk space

2. **🌐 Network Connectivity**

   - Ping test to Sentral server
   - DNS resolution check

3. **⏱️ Timeout Protection**
   - 300-second (5-minute) timeout for entire script
   - Prevents hanging jobs

### Enhanced Logging

- **📋 Generation Log**: Captured in `liss_generation.log`
- **📊 Structured Output**: Clear success/failure indicators
- **🔍 JSON Validation**: Detailed structure validation
- **📈 Performance Metrics**: Execution time tracking

### Failure Diagnostics

When failures occur, the action now shows:

- **🔍 Diagnostic Information**: Run number, commit, timestamps
- **📋 Recent Logs**: Last 50 lines of generation log
- **📈 Generation History**: Recent attempts from log file
- **🛠️ Troubleshooting Steps**: Specific actions to take
- **💡 Common Issues**: Known problems and solutions

### Artifact Collection

Enhanced artifacts now include:

- `liss_info.json` (if generated)
- `.logs/liss_info_generation.log` (persistent log)
- `liss_generation.log` (detailed debug output)
- Retention increased to 7 days for better analysis

## 🛠️ Manual Testing

### Test Debug Features Locally

```bash
# Test the enhanced API client
python3 test_debug_api.py

# Test LISS generation with debug
LISS_DEBUG=true python3 generate_liss_info.py
```

### Interpreting Debug Output

**Successful Request:**

```
📡 [1] Making GET request to: https://tempe-h.sentral.com.au/restapi/v1/timetables/timetable-calendar-date
📋 Parameters: {'from': '2025-09-02', 'to': '2025-09-09'}
📊 Response Status: 200 (took 1.23s)
📦 Response size: 4567 bytes
✅ Success: Retrieved 7 records
```

**Failed Request with Retry:**

```
📡 [2] Making GET request to: https://tempe-h.sentral.com.au/restapi/v1/timetables/timetable-period
⏰ Request timeout after 30.0s (limit: 30s)
🔄 Retry attempt 1/3 after 2s wait...
📡 [3] Making GET request to: https://tempe-h.sentral.com.au/restapi/v1/timetables/timetable-period
✅ Success: Retrieved 12 records
```

## 🔧 Troubleshooting Common Issues

### API Timeouts

- **Symptoms**: `Request timeout after 30.0s`
- **Debugging**: Check if server is overloaded, try manual testing
- **Solution**: Wait for server recovery, timeouts auto-retry 3 times

### Connection Errors

- **Symptoms**: `Connection error: HTTPSConnectionPool...`
- **Debugging**: Check network connectivity, DNS resolution
- **Solution**: Usually transient, GitHub Actions will retry automatically

### Rate Limiting

- **Symptoms**: `Rate limited! Retry after 60 seconds`
- **Debugging**: Check if too many requests in short time
- **Solution**: Automatic retry with proper delay

### Null Reference Errors

- **Symptoms**: `'NoneType' object has no attribute 'get'`
- **Debugging**: API call returned None, check previous error messages
- **Solution**: Enhanced null checking now prevents this

## 📞 Support

If issues persist after reviewing debug output:

1. **Download Artifacts**: Get the detailed logs from failed GitHub Action run
2. **Check Sentral Status**: Verify Sentral service is operational
3. **Manual Test**: Run `python3 test_debug_api.py` locally
4. **Review Logs**: Look for patterns in `.logs/liss_info_generation.log`
5. **Contact IT**: Provide debug logs and error details

The enhanced debugging should make it much easier to identify whether issues are:

- Temporary (network/server issues) → Auto-retry will handle
- Configuration (API keys, URLs) → Needs manual intervention
- Code bugs (null references, logic errors) → Needs development fix
