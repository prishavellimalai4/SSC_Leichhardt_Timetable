#!/usr/bin/env python3
"""
Test bell times fallback functionality by temporarily modifying config
"""

import json
import shutil
import time
import os


def test_fallback_functionality():
    """Test JSON to XML fallback"""
    print("🔄 BELL TIMES FALLBACK TEST")
    print("="*50)

    # Backup original config
    shutil.copy('config.json', 'config.json.backup')

    try:
        # Load config
        with open('config.json', 'r') as f:
            config = json.load(f)

        # Test 1: Disable JSON API
        print("📝 Test 1: Disable JSON API, enable XML fallback")
        config['bell_times']['use_api'] = False
        config['bell_times']['fallback_to_xml'] = True

        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)

        print("✅ Config updated: JSON disabled, XML fallback enabled")
        print("   - In browser console, you should see 'USING XML BELL TIMES'")

        time.sleep(2)

        # Test 2: Enable JSON API but simulate missing file
        print("\n📝 Test 2: Enable JSON API, rename JSON file to test fallback")
        config['bell_times']['use_api'] = True
        config['bell_times']['fallback_to_xml'] = True

        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)

        # Temporarily rename JSON file
        if os.path.exists('bell_times.json'):
            shutil.move('bell_times.json', 'bell_times.json.temp')
            print("✅ Temporarily moved bell_times.json")
            print("   - In browser console, you should see fallback to XML")

            time.sleep(2)

            # Restore JSON file
            shutil.move('bell_times.json.temp', 'bell_times.json')
            print("✅ Restored bell_times.json")

        # Test 3: Restore normal operation
        print("\n📝 Test 3: Restore normal JSON API operation")
        config['bell_times']['use_api'] = True
        config['bell_times']['fallback_to_xml'] = True

        with open('config.json', 'w') as f:
            json.dump(config, f, indent=2)

        print("✅ Config restored: JSON API enabled with XML fallback")
        print("   - In browser console, you should see 'USING JSON BELL TIMES'")

    finally:
        # Always restore original config
        shutil.copy('config.json.backup', 'config.json')
        os.remove('config.json.backup')
        print("\n🔄 Original configuration restored")


def main():
    print("BELL TIMES FALLBACK FUNCTIONALITY TEST")
    print("="*60)
    print("⚠️  This test will temporarily modify config.json")
    print("📝 Watch browser console (F12) for debug messages while test runs")
    print("🔄 Refresh the browser page after each test step\n")

    input("Press Enter to start fallback test...")

    test_fallback_functionality()

    print(f"\n{'='*60}")
    print("🎉 FALLBACK TEST COMPLETED!")
    print("\n📋 Summary of what should happen in browser console:")
    print("   1. XML bell times when JSON is disabled")
    print("   2. XML fallback when JSON file is missing")
    print("   3. JSON bell times when everything is restored")
    print("\n✅ Configuration has been restored to original state")


if __name__ == "__main__":
    main()
