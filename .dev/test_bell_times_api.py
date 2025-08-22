#!/usr/bin/env python3
"""
Test script to explore Sentral API endpoints for bell times data
to recreate bell_times.xml as JSON from the API
"""

import sys
import json
import os
from sentral_rest_client import SentralAPIClient


def load_config():
    """Load configuration from sentral_config.json"""
    try:
        with open('sentral_config.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("ERROR: sentral_config.json not found")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON in sentral_config.json: {e}")
        sys.exit(1)


def print_section(title, data=None):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    if data:
        print(json.dumps(data, indent=2))


def test_endpoint(client, endpoint_name, params=None):
    """Test an API endpoint and return the response"""
    print(f"\nTesting endpoint: {endpoint_name}")
    if params:
        print(f"Parameters: {params}")

    try:
        # Map endpoint names to client methods
        if endpoint_name == 'timetable_days':
            # Use direct API call since there's no specific method
            response_data = client._make_request(
                'GET', 'timetables/timetable-day', params)
        elif endpoint_name == 'timetable_periods':
            response_data = client._make_request(
                'GET', 'timetables/timetable-period', params)
        elif endpoint_name == 'timetable_period_in_day':
            response_data = client._make_request(
                'GET', 'timetables/timetable-period-in-day', params)
        else:
            print(f"✗ Unknown endpoint: {endpoint_name}")
            return None

        if response_data:
            data_list = response_data.get('data', [])
            print(f"✓ Success: Retrieved {len(data_list)} records")
            return response_data
        else:
            print("✗ Failed: No data returned")
            return None
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return None


def analyze_bell_times_xml():
    """Analyze the current bell_times.xml structure"""
    print_section("CURRENT BELL_TIMES.XML STRUCTURE")

    try:
        with open('bell_times.xml', 'r') as f:
            content = f.read()
            print("Sample content from bell_times.xml:")
            lines = content.split('\n')
            for i, line in enumerate(lines[:20]):  # Show first 20 lines
                print(f"{i+1:2d}: {line}")

            if len(lines) > 20:
                print(f"... (and {len(lines) - 20} more lines)")

    except FileNotFoundError:
        print("bell_times.xml not found")


def main():
    """Main test function"""
    print("SENTRAL API BELL TIMES EXPLORATION")
    print("="*60)

    # Initialize API client
    client = SentralAPIClient.from_config('sentral_config.json')

    # Analyze current XML structure
    analyze_bell_times_xml()

    # Test bell times related endpoints
    print_section("TESTING BELL TIMES API ENDPOINTS")

    # 1. Test timetable-day endpoint
    print_section("1. TIMETABLE DAYS")
    days_response = test_endpoint(client, 'timetable_days', {'limit': 10})
    if days_response:
        print("Sample timetable day data:")
        if days_response.get('data'):
            print(json.dumps(days_response['data'][0], indent=2))

    # 2. Test timetable-period endpoint
    print_section("2. TIMETABLE PERIODS")
    periods_response = test_endpoint(
        client, 'timetable_periods', {'limit': 20})
    if periods_response:
        print("Sample timetable period data:")
        if periods_response.get('data'):
            print(json.dumps(periods_response['data'][0], indent=2))

    # 3. Test timetable-period-in-day endpoint
    print_section("3. TIMETABLE PERIODS IN DAY")
    period_in_day_response = test_endpoint(
        client, 'timetable_period_in_day', {'limit': 50})
    if period_in_day_response:
        print("Sample period in day data:")
        if period_in_day_response.get('data'):
            print(json.dumps(period_in_day_response['data'][0], indent=2))

        # Show a few more examples to understand the structure
        print("\nAdditional examples:")
        for i, item in enumerate(period_in_day_response.get('data', [])[:5]):
            attrs = item.get('attributes', {})
            rels = item.get('relationships', {})
            day_id = rels.get('day', {}).get('data', {}).get('id', 'N/A')
            period_id = rels.get('period', {}).get('data', {}).get('id', 'N/A')
            print(f"  {i+1}. Day:{day_id} Period:{period_id} Start:{attrs.get('startTime')} End:{attrs.get('endTime')} Order:{attrs.get('order')}")

    # 4. Test with specific day filters if we got day data
    if days_response and days_response.get('data'):
        print_section("4. PERIODS FOR SPECIFIC DAYS")
        for day in days_response.get('data', [])[:3]:  # Test first 3 days
            day_id = day.get('id')
            day_name = day.get('attributes', {}).get('name', 'Unknown')
            print(f"\nTesting periods for Day {day_id} ({day_name}):")

            day_periods = test_endpoint(client, 'timetable_period_in_day', {
                'dayIds': day_id,
                'limit': 20
            })

            if day_periods and day_periods.get('data'):
                print(
                    f"Found {len(day_periods['data'])} periods for {day_name}")
                for period in day_periods['data']:
                    attrs = period.get('attributes', {})
                    print(
                        f"  - Order:{attrs.get('order')} Start:{attrs.get('startTime')} End:{attrs.get('endTime')}")

    print_section("ANALYSIS COMPLETE")
    print("Based on the API responses above, we can determine:")
    print("1. What bell times data is available from the API")
    print("2. How it maps to the bell_times.xml structure")
    print("3. Whether we can recreate bell_times.xml as JSON from API data")


if __name__ == "__main__":
    main()
