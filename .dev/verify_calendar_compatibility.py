#!/usr/bin/env python3
"""
Calendar Structure Verification Script
Verifies that calendar.json and calendar.xml have compatible structures.
"""

import json
import re
from datetime import datetime


def parse_xml_calendar():
    """Parse calendar.xml and extract structured data"""
    try:
        with open('calendar.xml', 'r', encoding='utf-8') as f:
            xml_content = f.read()

        # Extract calendar data using regex
        date_pattern = r'<dateTime\.iso8601>(\d{8}T\d{2}:\d{2}:\d{2})</dateTime\.iso8601>'
        day_name_pattern = r'<name>DayName</name>\s*<value>([^<]+)</value>'
        day_number_pattern = r'<name>DayNumber</name>\s*<value>\s*<i4>(\d+)</i4>'
        rotation_pattern = r'<name>Rotation</name>\s*<value>\s*<i4>(\d+)</i4>'

        dates = re.findall(date_pattern, xml_content)
        day_names = re.findall(day_name_pattern, xml_content)
        day_numbers = re.findall(day_number_pattern, xml_content)
        rotations = re.findall(rotation_pattern, xml_content)

        xml_data = []
        for i, date_str in enumerate(dates):
            if i < len(day_names) and i < len(day_numbers):
                date = date_str[:8]  # YYYYMMDD
                formatted_date = f'{date[:4]}-{date[4:6]}-{date[6:8]}'

                xml_data.append({
                    'date': formatted_date,
                    'dayName': day_names[i],
                    'dayNumber': int(day_numbers[i]),
                    'rotation': int(rotations[i]) if i < len(rotations) else 1,
                    'source': 'xml'
                })

        return xml_data
    except Exception as e:
        print(f"Error parsing XML calendar: {e}")
        return []


def parse_json_calendar():
    """Parse calendar.json and extract structured data"""
    try:
        with open('calendar.json', 'r', encoding='utf-8') as f:
            json_data = json.load(f)

        calendar_data = []
        for entry in json_data.get('calendar', []):
            calendar_data.append({
                'date': entry['date'],
                'dayName': entry['day_name'],
                'dayNumber': entry['day_number'],
                'isSchoolDay': entry.get('is_school_day', False),
                'cycle': entry.get('cycle'),
                'source': 'json'
            })

        return calendar_data
    except Exception as e:
        print(f"Error parsing JSON calendar: {e}")
        return []


def verify_structures():
    """Verify that both calendar structures are compatible"""
    print("🔍 Calendar Structure Verification")
    print("=" * 40)

    # Parse both calendars
    xml_data = parse_xml_calendar()
    json_data = parse_json_calendar()

    print(f"📄 XML calendar entries: {len(xml_data)}")
    print(f"📋 JSON calendar entries: {len(json_data)}")

    if not xml_data:
        print("❌ No XML data found")
        return False

    if not json_data:
        print("❌ No JSON data found")
        return False

    # Check structure compatibility
    print(f"\n🔍 Structure Analysis:")

    # XML structure
    xml_sample = xml_data[0] if xml_data else {}
    json_sample = json_data[0] if json_data else {}

    print(f"\n📄 XML Sample Entry:")
    for key, value in xml_sample.items():
        print(f"   {key}: {value} ({type(value).__name__})")

    print(f"\n📋 JSON Sample Entry:")
    for key, value in json_sample.items():
        print(f"   {key}: {value} ({type(value).__name__})")

    # Check essential fields
    print(f"\n✅ Essential Field Verification:")

    essential_fields = ['date', 'dayName', 'dayNumber']
    xml_has_fields = all(field in xml_sample for field in essential_fields)
    json_has_fields = all(field in json_sample for field in essential_fields)

    print(f"   XML has essential fields: {'✅' if xml_has_fields else '❌'}")
    print(f"   JSON has essential fields: {'✅' if json_has_fields else '❌'}")

    # Find overlapping dates for comparison
    xml_dates = {entry['date'] for entry in xml_data}
    json_dates = {entry['date'] for entry in json_data}
    common_dates = xml_dates.intersection(json_dates)

    print(f"\n📅 Date Range Comparison:")
    print(
        f"   XML date range: {min(xml_dates) if xml_dates else 'N/A'} to {max(xml_dates) if xml_dates else 'N/A'}")
    print(
        f"   JSON date range: {min(json_dates) if json_dates else 'N/A'} to {max(json_dates) if json_dates else 'N/A'}")
    print(f"   Common dates: {len(common_dates)}")

    # Check compatibility on common dates
    if common_dates:
        print(f"\n🔍 Data Consistency Check (first 5 common dates):")

        for date in sorted(common_dates)[:5]:
            xml_entry = next((e for e in xml_data if e['date'] == date), None)
            json_entry = next(
                (e for e in json_data if e['date'] == date), None)

            if xml_entry and json_entry:
                day_name_match = xml_entry['dayName'] == json_entry['dayName']
                day_number_match = xml_entry['dayNumber'] == json_entry['dayNumber']

                status = "✅" if day_name_match and day_number_match else "⚠️"
                print(f"   {status} {date}:")
                print(
                    f"      XML: {xml_entry['dayName']} (Day {xml_entry['dayNumber']})")
                print(
                    f"      JSON: {json_entry['dayName']} (Day {json_entry['dayNumber']})")

                if not day_name_match:
                    print(f"      ❌ Day name mismatch!")
                if not day_number_match:
                    print(f"      ❌ Day number mismatch!")

    # Summary
    print(f"\n📊 Compatibility Summary:")
    compatibility_score = 0
    total_checks = 4

    if xml_has_fields:
        compatibility_score += 1
        print(f"   ✅ XML has essential fields")
    else:
        print(f"   ❌ XML missing essential fields")

    if json_has_fields:
        compatibility_score += 1
        print(f"   ✅ JSON has essential fields")
    else:
        print(f"   ❌ JSON missing essential fields")

    if len(common_dates) > 0:
        compatibility_score += 1
        print(f"   ✅ Calendars have overlapping dates")
    else:
        print(f"   ❌ No overlapping dates found")

    # Check if index.html can handle both formats
    data_consistency = True
    if common_dates:
        for date in sorted(common_dates)[:10]:  # Check first 10 common dates
            xml_entry = next((e for e in xml_data if e['date'] == date), None)
            json_entry = next(
                (e for e in json_data if e['date'] == date), None)

            if xml_entry and json_entry:
                if xml_entry['dayName'] != json_entry['dayName'] or xml_entry['dayNumber'] != json_entry['dayNumber']:
                    data_consistency = False
                    break

    if data_consistency:
        compatibility_score += 1
        print(f"   ✅ Data consistency maintained")
    else:
        print(f"   ⚠️  Some data inconsistencies found")

    print(
        f"\n🎯 Overall Compatibility: {compatibility_score}/{total_checks} ({compatibility_score/total_checks*100:.0f}%)")

    return compatibility_score >= 3  # At least 75% compatibility


if __name__ == "__main__":
    verify_structures()
