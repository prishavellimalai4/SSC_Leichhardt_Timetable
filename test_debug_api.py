#!/usr/bin/env python3
"""
Test script to validate the enhanced debugging capabilities.
This can be run manually to test the new API debugging features.
"""

import sys
import os
from sentral_rest_client import SentralAPIClient

def test_api_debugging():
    """Test the enhanced API debugging features."""
    print("🧪 Testing Enhanced API Debugging")
    print("=" * 50)
    
    # Test with debug mode enabled
    print("🐛 Creating client with debug mode enabled...")
    client = SentralAPIClient.from_config('config.json', debug=True)
    
    if not client:
        print("❌ Failed to create API client")
        return False
    
    print("✅ Client created successfully with debug mode")
    print(f"🌐 Base URL: {client.base_url}")
    print(f"🏢 Tenant: {client.tenant}")
    print("")
    
    # Test a simple API call
    print("🔍 Testing API connectivity with enhanced debugging...")
    print("📡 Making test request to timetable calendar endpoint...")
    
    # This should show detailed debugging information
    response = client.get_timetable_calendar_dates(limit=1)
    
    if response:
        print("✅ Test API call successful!")
        print(f"📊 Response contains {len(response)} records")
    else:
        print("❌ Test API call failed")
    
    print("")
    
    # Show request statistics
    client.print_request_stats()
    
    print("")
    print("🧪 Debug test completed!")
    
    return response is not None

if __name__ == "__main__":
    success = test_api_debugging()
    if not success:
        sys.exit(1)
    print("✅ All debugging tests passed!")
