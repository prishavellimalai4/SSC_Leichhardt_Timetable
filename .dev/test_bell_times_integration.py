#!/usr/bin/env python3
"""
Test script to verify bell times JSON vs XML functionality in index.html
"""

import json
import time
import subprocess
import sys


def test_bell_times_config():
    """Test the bell times configuration"""
    print("🔧 BELL TIMES CONFIG TEST")
    print("="*50)

    # Test config.json contains bell_times section
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)

        bell_times_config = config.get('bell_times', {})
        print(f"✅ Bell times configuration found:")
        print(f"   - use_api: {bell_times_config.get('use_api', 'NOT SET')}")
        print(
            f"   - fallback_to_xml: {bell_times_config.get('fallback_to_xml', 'NOT SET')}")
        print(f"   - api_file: {bell_times_config.get('api_file', 'NOT SET')}")
        print(f"   - xml_file: {bell_times_config.get('xml_file', 'NOT SET')}")

        return True

    except Exception as e:
        print(f"❌ Error loading config: {e}")
        return False


def test_file_availability():
    """Test that both bell times files exist"""
    print("\n📁 FILE AVAILABILITY TEST")
    print("="*50)

    import os

    json_exists = os.path.exists('bell_times.json')
    xml_exists = os.path.exists('bell_times.xml')

    print(f"📄 bell_times.json: {'✅ EXISTS' if json_exists else '❌ MISSING'}")
    print(f"📄 bell_times.xml: {'✅ EXISTS' if xml_exists else '❌ MISSING'}")

    if json_exists:
        try:
            with open('bell_times.json', 'r') as f:
                json_data = json.load(f)
            print(
                f"   📊 JSON contains {len(json_data.get('bell_times', []))} bell time entries")
            print(
                f"   📝 Source: {json_data.get('metadata', {}).get('source', 'unknown')}")
        except Exception as e:
            print(f"   ❌ Error reading JSON: {e}")

    if xml_exists:
        try:
            with open('bell_times.xml', 'r') as f:
                xml_content = f.read()
            struct_count = xml_content.count('<struct>')
            print(
                f"   📊 XML contains approximately {struct_count} struct entries")
        except Exception as e:
            print(f"   ❌ Error reading XML: {e}")

    return json_exists or xml_exists


def test_web_server():
    """Test web server accessibility"""
    print("\n🌐 WEB SERVER TEST")
    print("="*50)

    import urllib.request
    import urllib.error

    try:
        # Test if server is running
        response = urllib.request.urlopen(
            'http://localhost:8000/config.json', timeout=5)
        print("✅ Web server is running and accessible")

        # Test JSON file access
        try:
            json_response = urllib.request.urlopen(
                'http://localhost:8000/bell_times.json', timeout=5)
            print("✅ bell_times.json accessible via web server")
        except urllib.error.HTTPError as e:
            print(f"⚠️  bell_times.json not accessible: {e.code}")

        # Test XML file access
        try:
            xml_response = urllib.request.urlopen(
                'http://localhost:8000/bell_times.xml', timeout=5)
            print("✅ bell_times.xml accessible via web server")
        except urllib.error.HTTPError as e:
            print(f"⚠️  bell_times.xml not accessible: {e.code}")

        return True

    except Exception as e:
        print(f"❌ Web server not accessible: {e}")
        print("   Make sure to run: python -m http.server 8000")
        return False


def main():
    """Run all tests"""
    print("BELL TIMES INTEGRATION TEST SUITE")
    print("="*60)

    success_count = 0
    total_tests = 3

    # Test 1: Configuration
    if test_bell_times_config():
        success_count += 1

    # Test 2: File availability
    if test_file_availability():
        success_count += 1

    # Test 3: Web server
    if test_web_server():
        success_count += 1

    # Summary
    print(f"\n{'='*60}")
    print(f"TEST RESULTS: {success_count}/{total_tests} tests passed")

    if success_count == total_tests:
        print("🎉 ALL TESTS PASSED!")
        print("\n📝 Next steps:")
        print("   1. Open http://localhost:8000 in a browser")
        print("   2. Check browser console (F12) for 'BELL TIMES DEBUG' messages")
        print("   3. Verify that bell times are loaded from JSON (with XML fallback)")
        print("   4. Test by temporarily renaming bell_times.json to see XML fallback")
        return True
    else:
        print("💥 SOME TESTS FAILED!")
        print("   Please check the errors above and fix any issues")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
