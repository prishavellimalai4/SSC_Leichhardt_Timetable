#!/usr/bin/env python3
"""
Test script for Sentral Calendar API endpoints
"""

import json
from datetime import datetime, timedelta
from sentral_rest_client import SentralAPIClient


def test_calendar_endpoints():
    """Test various calendar-related API endpoints"""

    print("Testing Sentral Calendar API Endpoints")
    print("=" * 50)

    # Initialize client
    client = SentralAPIClient.from_config()
    if not client:
        print("❌ Failed to initialize API client")
        return

    # Test basic connection first
    if not client.test_connection():
        print("❌ API connection test failed")
        return

    print("\n🗓️  Testing Calendar Endpoints")
    print("-" * 30)

    # Get current date and a date range for testing
    today = datetime.now()
    date_from = today.strftime('%Y-%m-%d')
    date_to = (today + timedelta(days=7)).strftime('%Y-%m-%d')

    # Test 1: Get all calendar dates (limited)
    print(f"\n1. Getting calendar dates (limited to 5 records)...")
    calendar_dates = client.get_timetable_calendar_dates(limit=5)

    if calendar_dates:
        print(f"✅ Retrieved {len(calendar_dates)} calendar date records")
        print("Sample calendar date record:")
        print(json.dumps(calendar_dates[0], indent=2, default=str))
    else:
        print("❌ No calendar dates retrieved")

    # Test 2: Get calendar dates for current week
    print(f"\n2. Getting calendar dates from {date_from} to {date_to}...")
    weekly_calendar = client.get_timetable_calendar_dates(
        date_from=date_from,
        date_to=date_to
    )

    if weekly_calendar:
        print(
            f"✅ Retrieved {len(weekly_calendar)} calendar records for this week")
        for record in weekly_calendar:
            date_info = record.get('date', 'Unknown date')
            day_type = record.get('day_type', 'Unknown type')
            print(f"  📅 {date_info}: {day_type}")
    else:
        print("❌ No weekly calendar data retrieved")

    # Test 3: Get calendar dates with specific filters
    print(f"\n3. Testing various filter combinations...")

    # Try different filter combinations
    filter_tests = [
        {"academic_year": datetime.now().year},
        {"include_holidays": True},
        {"day_type": "NORMAL"},  # Common day type
    ]

    for i, filters in enumerate(filter_tests, 1):
        print(f"  Test 3.{i}: Filters {filters}")
        filtered_dates = client.get_timetable_calendar_dates(
            **filters, limit=3)

        if filtered_dates:
            print(f"    ✅ Retrieved {len(filtered_dates)} records")
        else:
            print(f"    ❌ No records with filters {filters}")

    print("\n📊 Calendar API Test Summary")
    print("-" * 30)
    print("✅ Calendar endpoint testing completed")
    print("💡 Use these methods in your timetable kiosk application:")
    print("   - get_timetable_calendar_dates() for date ranges")
    print("   - Filter by date_from/date_to for specific periods")
    print("   - Use academic_year filter for school year data")


def demonstrate_calendar_usage():
    """Demonstrate practical usage of calendar data for a timetable kiosk"""

    print("\n🏫 Practical Calendar Usage for Timetable Kiosk")
    print("=" * 50)

    client = SentralAPIClient.from_config()
    if not client:
        return

    # Get today's calendar information
    today = datetime.now().strftime('%Y-%m-%d')
    print(f"Getting today's timetable information for {today}...")

    today_info = client.get_timetable_calendar_dates(
        date_from=today,
        date_to=today
    )

    if today_info:
        for day_info in today_info:
            print(f"\n📅 Today ({today}):")
            print(f"   Day Type: {day_info.get('day_type', 'Unknown')}")
            print(f"   Calendar: {day_info.get('calendar_name', 'Unknown')}")
            print(
                f"   Academic Year: {day_info.get('academic_year', 'Unknown')}")

            # Check if it's a school day
            day_type = day_info.get('day_type', '').upper()
            if day_type in ['NORMAL', 'TIMETABLE', 'SCHOOL']:
                print("   🟢 Regular school day - display full timetable")
            elif day_type in ['HOLIDAY', 'PUPIL_FREE']:
                print("   🔴 No classes today")
            else:
                print(f"   🟡 Special day type: {day_type}")
    else:
        print("❌ Could not retrieve today's calendar information")

    # Get next week's overview
    print(f"\n📋 Next 7 days overview:")
    next_week = client.get_timetable_calendar_dates(
        date_from=today,
        date_to=(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')
    )

    if next_week:
        for day in next_week:
            date = day.get('date', 'Unknown')
            day_type = day.get('day_type', 'Unknown')
            print(f"   {date}: {day_type}")
    else:
        print("❌ Could not retrieve next week's information")


if __name__ == "__main__":
    test_calendar_endpoints()
    demonstrate_calendar_usage()
