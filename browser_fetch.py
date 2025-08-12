#!/usr/bin/env python3
"""
Browser-based XML fetcher for Tempe High School Timetable
Opens URLs in browser for authentication, then extracts content.
"""

import webbrowser
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
import os

# URLs to fetch
URLS = {
    'bell_times.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishBellTimes.debug',
    'calendar.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishCalendar.debug',
    'liss_info.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishTimetable.debug'
}

def method1_selenium_automated():
    """Method 1: Use Selenium to automate browser and extract content."""
    print("=== METHOD 1: Selenium Automated Fetching ===")
    print("This will open a browser window for you to login, then automatically extract content.")
    
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # chrome_options.add_argument("--headless")  # Uncomment for headless mode
    
    xml_data = {}
    
    try:
        # Initialize the driver
        driver = webdriver.Chrome(options=chrome_options)
        print("✓ Browser opened")
        
        for filename, url in URLS.items():
            print(f"\nFetching {filename}...")
            
            # Navigate to URL
            driver.get(url)
            print(f"📖 Opened: {url}")
            
            # Wait for user to authenticate if needed
            print("⏳ Waiting for authentication...")
            print("   Please log in if prompted, then press Enter to continue...")
            input("   Press Enter when the XML content is displayed: ")
            
            # Get page source
            page_source = driver.page_source
            
            # Check if we got XML
            if page_source.strip().startswith('<?xml') or '<' in page_source:
                # Try to extract just the XML content
                if '<?xml' in page_source:
                    start_idx = page_source.find('<?xml')
                    xml_content = page_source[start_idx:]
                    # Remove any HTML wrapper if present
                    if '</html>' in xml_content:
                        end_idx = xml_content.find('</html>')
                        before_html = xml_content[:end_idx]
                        if before_html.count('<') > before_html.count('>'): 
                            xml_content = before_html
                else:
                    xml_content = page_source
                
                xml_data[filename] = xml_content
                print(f"✓ Successfully captured {filename}")
            else:
                xml_data[filename] = f"<error>No XML content found for {filename}</error>"
                print(f"⚠️  No XML content found for {filename}")
        
        driver.quit()
        print("✓ Browser closed")
        
    except Exception as e:
        print(f"✗ Error with Selenium method: {e}")
        print("Make sure you have Chrome and chromedriver installed")
        return None
    
    return xml_data

def method2_browser_clipboard():
    """Method 2: Open URLs in default browser and use clipboard."""
    print("=== METHOD 2: Browser + Clipboard ===")
    print("This will open URLs in your default browser. You copy the XML content.")
    
    try:
        import pyperclip
    except ImportError:
        print("⚠️  pyperclip not installed. Run: pip install pyperclip")
        return None
    
    xml_data = {}
    
    for filename, url in URLS.items():
        print(f"\n--- {filename} ---")
        print(f"📖 Opening: {url}")
        
        # Open URL in default browser
        webbrowser.open(url)
        
        print("Instructions:")
        print("1. Login to Sentral if prompted")
        print("2. Wait for XML content to load")
        print("3. Select all content (Ctrl+A)")
        print("4. Copy to clipboard (Ctrl+C)")
        print("5. Press Enter here to capture from clipboard")
        
        input("Press Enter when you've copied the XML content: ")
        
        # Get content from clipboard
        try:
            content = pyperclip.paste()
            if content and (content.strip().startswith('<?xml') or '<' in content):
                xml_data[filename] = content
                print(f"✓ Captured {len(content)} characters for {filename}")
            else:
                print(f"⚠️  No XML content in clipboard for {filename}")
                xml_data[filename] = f"<error>No XML content in clipboard for {filename}</error>"
        except Exception as e:
            print(f"✗ Error reading clipboard: {e}")
            xml_data[filename] = f"<error>Clipboard error for {filename}: {e}</error>"
    
    return xml_data

def method3_manual_input():
    """Method 3: Manual input with browser opening."""
    print("=== METHOD 3: Manual Input ===")
    print("This will open URLs and let you paste content manually.")
    
    xml_data = {}
    
    for filename, url in URLS.items():
        print(f"\n--- {filename} ---")
        print(f"📖 Opening: {url}")
        
        # Open URL in default browser
        webbrowser.open(url)
        
        print("Instructions:")
        print("1. Login to Sentral if prompted")
        print("2. Wait for XML content to load")
        print("3. Copy the XML content")
        print("4. Paste it below (press Enter twice when done)")
        
        # Collect input
        lines = []
        print("Paste XML content:")
        while True:
            try:
                line = input()
                if line.strip() == "" and lines and lines[-1].strip() == "":
                    break
                lines.append(line)
            except EOFError:
                break
        
        content = "\n".join(lines).strip()
        
        if content:
            xml_data[filename] = content
            print(f"✓ Added {len(content)} characters for {filename}")
        else:
            xml_data[filename] = f"<error>No content provided for {filename}</error>"
            print(f"⚠️  No content provided for {filename}")
    
    return xml_data

def save_xml_data(xml_data):
    """Save XML data to files and optionally commit to git."""
    if not xml_data:
        print("No data to save")
        return
    
    print("\n=== SAVING DATA ===")
    
    # Save to files
    for filename, content in xml_data.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Saved {filename}")
        except Exception as e:
            print(f"✗ Error saving {filename}: {e}")
    
    # Ask about git commit
    commit = input("\nCommit changes to git? (y/n): ").lower().strip()
    if commit == 'y':
        try:
            from datetime import datetime
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            commit_message = f"content update {time_str} and {date_str}"
            
            commands = [
                ["git", "add", "bell_times.xml", "calendar.xml", "liss_info.xml"],
                ["git", "commit", "-m", commit_message],
                ["git", "push"]
            ]
            
            for cmd in commands:
                result = subprocess.run(cmd, capture_output=True, text=True)
                if result.returncode != 0:
                    if "nothing to commit" in result.stdout:
                        print("No changes to commit.")
                        break
                    else:
                        print(f"Git error: {result.stderr}")
                        return
                else:
                    print(f"✓ {cmd[1]} completed")
            
            print("✓ Changes committed and pushed")
            
        except Exception as e:
            print(f"✗ Git error: {e}")

def main():
    """Main function."""
    print("=" * 60)
    print("BROWSER-BASED XML FETCHER")
    print("Tempe High School Timetable")
    print("=" * 60)
    
    print("\nAvailable methods:")
    print("1. Selenium Automated (requires chromedriver)")
    print("2. Browser + Clipboard (requires pyperclip)")
    print("3. Manual Input")
    
    choice = input("\nChoose method (1/2/3): ").strip()
    
    xml_data = None
    
    if choice == "1":
        xml_data = method1_selenium_automated()
    elif choice == "2":
        xml_data = method2_browser_clipboard()
    elif choice == "3":
        xml_data = method3_manual_input()
    else:
        print("Invalid choice. Using manual input method...")
        xml_data = method3_manual_input()
    
    if xml_data:
        # Show summary
        print("\n=== SUMMARY ===")
        for filename, content in xml_data.items():
            if content.startswith('<error>'):
                print(f"⚠️  {filename}: Error")
            else:
                print(f"✓ {filename}: {len(content)} characters")
        
        save_xml_data(xml_data)
    else:
        print("No data captured.")

if __name__ == "__main__":
    main()
