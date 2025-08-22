#!/usr/bin/env python3
"""
Test script to verify that bell_times.json matches bell_times.xml structure
"""

import json
import xml.etree.ElementTree as ET
from typing import Dict, List, Any


def parse_xml_bell_times() -> List[Dict[str, Any]]:
    """Parse bell_times.xml and extract bell times data"""
    print("📖 Parsing bell_times.xml...")

    try:
        # The XML is in XML-RPC format, so we need to extract the data differently
        with open('bell_times.xml', 'r', encoding='utf-8') as f:
            content = f.read()

        # Find all struct elements within the array (each represents a bell time entry)
        structs = []
        lines = content.split('\n')

        # State tracking
        in_bell_times_array = False
        in_struct = False
        current_struct = {}
        current_member = None
        in_value = False
        value_content = ""

        for line in lines:
            line = line.strip()

            # Look for the start of bell times data (after the first param which is auth info)
            if '<array>' in line:
                in_bell_times_array = True
                continue
            elif '</array>' in line:
                in_bell_times_array = False
                continue

            if not in_bell_times_array:
                continue

            if '<struct>' in line:
                in_struct = True
                current_struct = {}
            elif '</struct>' in line and in_struct:
                # Valid bell time entry
                if current_struct and len(current_struct) >= 6:
                    structs.append(current_struct.copy())
                in_struct = False
                current_struct = {}
            elif in_struct:
                if '<name>' in line and '</name>' in line:
                    # Extract member name
                    start = line.find('<name>') + 6
                    end = line.find('</name>')
                    current_member = line[start:end]
                elif '<value>' in line and current_member:
                    if '</value>' in line:
                        # Single line value
                        start = line.find('<value>') + 7
                        end = line.find('</value>')
                        value_part = line[start:end]

                        # Handle <i4> tags for integers
                        if '<i4>' in value_part and '</i4>' in value_part:
                            i4_start = value_part.find('<i4>') + 4
                            i4_end = value_part.find('</i4>')
                            value = int(value_part[i4_start:i4_end])
                        else:
                            value = value_part

                        current_struct[current_member] = value
                        current_member = None
                    else:
                        # Multi-line value
                        in_value = True
                        start = line.find('<value>') + 7
                        value_content = line[start:]
                elif in_value:
                    if '</value>' in line:
                        # End of multi-line value
                        end = line.find('</value>')
                        value_content += line[:end]

                        # Handle <i4> tags for integers
                        if '<i4>' in value_content and '</i4>' in value_content:
                            i4_start = value_content.find('<i4>') + 4
                            i4_end = value_content.find('</i4>')
                            value = int(value_content[i4_start:i4_end])
                        else:
                            value = value_content.strip()

                        current_struct[current_member] = value
                        current_member = None
                        in_value = False
                        value_content = ""
                    else:
                        # Continue accumulating value content
                        value_content += line

        print(f"✓ Found {len(structs)} bell time entries in XML")
        return structs

    except Exception as e:
        print(f"❌ Error parsing XML: {e}")
        return []


def parse_json_bell_times() -> List[Dict[str, Any]]:
    """Parse bell_times.json and extract bell times data"""
    print("📖 Parsing bell_times.json...")

    try:
        with open('bell_times.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        bell_times = data.get('bell_times', [])
        print(f"✓ Found {len(bell_times)} bell time entries in JSON")
        return bell_times

    except Exception as e:
        print(f"❌ Error parsing JSON: {e}")
        return []


def compare_bell_times(xml_data: List[Dict], json_data: List[Dict]) -> bool:
    """Compare XML and JSON bell times data"""
    print("\n🔍 Comparing XML and JSON data...")

    if len(xml_data) == 0:
        print("⚠️  No XML data to compare")
        return False

    if len(json_data) == 0:
        print("⚠️  No JSON data to compare")
        return False

    print(f"📊 XML entries: {len(xml_data)}")
    print(f"📊 JSON entries: {len(json_data)}")

    # Create lookup for XML data
    xml_lookup = {}
    for entry in xml_data:
        key = f"{entry.get('DayName', '')}-{entry.get('Period', '')}"
        xml_lookup[key] = entry

    # Create lookup for JSON data
    json_lookup = {}
    for entry in json_data:
        key = f"{entry.get('DayName', '')}-{entry.get('Period', '')}"
        json_lookup[key] = entry

    # Compare structure
    xml_keys = set(xml_lookup.keys())
    json_keys = set(json_lookup.keys())

    print(f"\n📋 Unique periods in XML: {len(xml_keys)}")
    print(f"📋 Unique periods in JSON: {len(json_keys)}")

    # Find common periods
    common_keys = xml_keys & json_keys
    xml_only = xml_keys - json_keys
    json_only = json_keys - xml_keys

    print(f"✅ Common periods: {len(common_keys)}")
    print(f"🟡 XML only: {len(xml_only)}")
    print(f"🟡 JSON only: {len(json_only)}")

    if xml_only:
        print(f"   XML only periods (first 5): {list(xml_only)[:5]}")
    if json_only:
        print(f"   JSON only periods (first 5): {list(json_only)[:5]}")

    # Compare common entries
    matches = 0
    mismatches = 0

    print(f"\n🔍 Detailed comparison of {len(common_keys)} common periods:")

    sample_mismatches = []
    for key in sorted(list(common_keys)):
        xml_entry = xml_lookup[key]
        json_entry = json_lookup[key]

        # Compare all fields
        fields_match = True
        field_details = []

        for field in ['DayNumber', 'DayName', 'Period', 'StartTime', 'EndTime', 'Type']:
            xml_val = xml_entry.get(field)
            json_val = json_entry.get(field)

            if xml_val != json_val:
                fields_match = False
                field_details.append(
                    f"{field}: XML='{xml_val}' vs JSON='{json_val}'")

        if fields_match:
            matches += 1
        else:
            mismatches += 1
            if len(sample_mismatches) < 10:  # Show first 10 mismatches
                sample_mismatches.append(
                    f"   ❌ {key}: {'; '.join(field_details)}")

    # Print sample mismatches
    for mismatch in sample_mismatches:
        print(mismatch)

    print(f"\n📊 Final comparison results:")
    print(f"   ✅ Exact matches: {matches}")
    print(f"   ❌ Mismatches: {mismatches}")
    print(f"   📈 Match rate: {(matches/(matches+mismatches)*100):.1f}%" if (
        matches+mismatches) > 0 else "N/A")

    # Show sample data from both sources
    print(f"\n📝 Sample XML entry:")
    if xml_data:
        sample_xml = xml_data[0]
        for field in ['DayNumber', 'DayName', 'Period', 'StartTime', 'EndTime', 'Type']:
            print(f"   {field}: {sample_xml.get(field)}")

    print(f"\n📝 Sample JSON entry:")
    if json_data:
        sample_json = json_data[0]
        for field in ['DayNumber', 'DayName', 'Period', 'StartTime', 'EndTime', 'Type']:
            print(f"   {field}: {sample_json.get(field)}")

    return matches > mismatches


def main():
    """Main comparison function"""
    print("BELL TIMES XML vs JSON COMPARISON")
    print("="*50)

    # Parse both sources
    xml_data = parse_xml_bell_times()
    json_data = parse_json_bell_times()

    # Compare data
    if xml_data and json_data:
        success = compare_bell_times(xml_data, json_data)

        print(f"\n{'='*50}")
        if success:
            print("🎉 COMPARISON SUCCESSFUL!")
            print(
                "The JSON data structure successfully recreates the XML bell times data.")
        else:
            print("⚠️  COMPARISON ISSUES DETECTED")
            print(
                "There are differences between XML and JSON data that may need attention.")
    else:
        print("❌ COMPARISON FAILED")
        print("Could not load data from one or both sources.")


if __name__ == "__main__":
    main()
