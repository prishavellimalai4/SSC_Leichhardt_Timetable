#!/usr/bin/env python3
"""
Test script to verify calendar debugging functionality
"""

import json
import subprocess
import time
import os
from pathlib import Path


def update_config_debug(debug_value):
    """Update the debug setting in config.json"""
    config_file = 'config.json'

    with open(config_file, 'r') as f:
        config = json.load(f)

    # Update debug setting
    if 'ui' not in config:
        config['ui'] = {}
    config['ui']['debug'] = debug_value

    with open(config_file, 'w') as f:
        json.dump(config, f, indent=2)

    print(f"✅ Updated config.json debug setting to: {debug_value}")


def test_debug_functionality():
    """Test the debug functionality"""
    print("🧪 Testing Calendar Debug Functionality")
    print("=" * 45)

    # Test 1: Debug disabled (default)
    print("\n📋 Test 1: Debug DISABLED")
    update_config_debug(False)
    print("   - Debug messages should NOT appear in console")
    print("   - Only essential error messages should show")
    print("   - Console should be clean for production use")

    # Test 2: Debug enabled
    print("\n📋 Test 2: Debug ENABLED")
    update_config_debug(True)
    print("   - All calendar debug messages should appear")
    print("   - Configuration details should be logged")
    print("   - Source decision should be clearly indicated")

    print("\n🔧 Instructions:")
    print("1. Start server: python -m http.server 8000")
    print("2. Open http://localhost:8000 in browser")
    print("3. Open Developer Tools (F12) → Console tab")
    print("4. Check console output for debug messages")

    print("\n🎯 Expected Results:")
    print("- With debug=false: Clean console, no CALENDAR DEBUG messages")
    print("- With debug=true: Detailed CALENDAR DEBUG messages visible")

    # Leave debug enabled for testing
    print(f"\n✅ Config is now set to debug={True} for testing")


def show_config_debug_section():
    """Show the current debug configuration"""
    try:
        with open('config.json', 'r') as f:
            config = json.load(f)

        debug_setting = config.get('ui', {}).get('debug', 'not set')
        print(f"\n📊 Current debug setting: {debug_setting}")

        ui_section = config.get('ui', {})
        print(f"\n📋 UI configuration section:")
        for key, value in ui_section.items():
            print(f"   {key}: {value}")

    except Exception as e:
        print(f"❌ Error reading config: {e}")


if __name__ == "__main__":
    # Change to the correct directory
    os.chdir('/workspaces/Tempe_HS_Timetable_Kiosk')

    show_config_debug_section()
    test_debug_functionality()
    show_config_debug_section()
