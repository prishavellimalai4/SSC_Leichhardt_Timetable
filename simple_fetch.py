#!/usr/bin/env python3
"""
Simple browser-based XML fetcher for Tempe High School
Opens URLs in browser, guides you through copying content.
"""

import webbrowser
import time
import os
import subprocess
from datetime import datetime

# URLs to fetch
URLS = {
    'bell_times.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishBellTimes.debug',
    'calendar.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishCalendar.debug',
    'liss_info.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishTimetable.debug'
}

def fetch_xml_content():
    """Open URLs in browser and collect XML content."""
    xml_data = {}
    
    print("🌐 BROWSER-BASED XML FETCHER")
    print("=" * 40)
    print("This script will:")
    print("1. Open each URL in your default browser")
    print("2. Guide you through copying the XML content")
    print("3. Save the content to local files")
    print()
    
    for i, (filename, url) in enumerate(URLS.items(), 1):
        print(f"📄 Step {i}/3: Fetching {filename}")
        print("-" * 40)
        
        # Open URL in browser
        print(f"🔗 Opening: {url}")
        webbrowser.open(url)
        
        print("\n📋 Instructions:")
        print("1. 🔐 Login to Sentral if prompted")
        print("2. ⏳ Wait for the XML content to load")
        print("3. 📝 Select all content (Ctrl+A or Cmd+A)")
        print("4. 📋 Copy to clipboard (Ctrl+C or Cmd+C)")
        print("5. ↩️  Come back here and press Enter")
        
        input(f"\n✋ Press Enter when you've copied the XML for {filename}: ")
        
        # Try to get content from clipboard
        content = None
        try:
            # Try different methods to get clipboard content
            if os.name == 'nt':  # Windows
                import subprocess
                result = subprocess.run(['powershell', 'Get-Clipboard'], capture_output=True, text=True)
                if result.returncode == 0:
                    content = result.stdout
            else:  # macOS/Linux
                try:
                    result = subprocess.run(['pbpaste'], capture_output=True, text=True)  # macOS
                    if result.returncode == 0:
                        content = result.stdout
                except FileNotFoundError:
                    try:
                        result = subprocess.run(['xclip', '-selection', 'clipboard', '-o'], capture_output=True, text=True)  # Linux
                        if result.returncode == 0:
                            content = result.stdout
                    except FileNotFoundError:
                        pass
        except Exception:
            pass
        
        # If clipboard access failed, ask for manual input
        if not content or not content.strip():
            print("⚠️  Couldn't access clipboard. Please paste the content manually:")
            lines = []
            print("Paste XML content (press Enter on empty line to finish):")
            while True:
                try:
                    line = input()
                    if line.strip() == "":
                        break
                    lines.append(line)
                except EOFError:
                    break
            content = "\n".join(lines)
        
        # Validate and store content
        if content and content.strip():
            if '<?xml' in content or '<' in content:
                xml_data[filename] = content.strip()
                print(f"✅ Successfully captured {filename} ({len(content)} characters)")
            else:
                print(f"⚠️  Content doesn't look like XML for {filename}")
                xml_data[filename] = content.strip()
        else:
            print(f"❌ No content captured for {filename}")
            xml_data[filename] = f"<!-- Error: No content captured for {filename} -->"
        
        print()
    
    return xml_data

def save_and_commit(xml_data):
    """Save XML data to files and commit to git."""
    print("💾 SAVING FILES")
    print("=" * 40)
    
    # Save files
    saved_files = []
    for filename, content in xml_data.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✅ Saved {filename}")
            saved_files.append(filename)
        except Exception as e:
            print(f"❌ Error saving {filename}: {e}")
    
    if not saved_files:
        print("❌ No files were saved successfully")
        return
    
    # Git commit
    commit_choice = input(f"\n🔄 Commit {len(saved_files)} files to git? (y/n): ").lower().strip()
    
    if commit_choice in ['y', 'yes']:
        try:
            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            time_str = now.strftime("%H:%M:%S")
            commit_message = f"content update {time_str} and {date_str}"
            
            # Git commands
            print("🔄 Committing to git...")
            
            # Add files
            result = subprocess.run(['git', 'add'] + saved_files, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Git add failed: {result.stderr}")
                return
            
            # Commit
            result = subprocess.run(['git', 'commit', '-m', commit_message], capture_output=True, text=True)
            if result.returncode != 0:
                if "nothing to commit" in result.stdout:
                    print("ℹ️  No changes to commit")
                    return
                else:
                    print(f"❌ Git commit failed: {result.stderr}")
                    return
            
            # Push
            result = subprocess.run(['git', 'push'], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"❌ Git push failed: {result.stderr}")
                return
            
            print("✅ Successfully committed and pushed changes!")
            
        except Exception as e:
            print(f"❌ Git error: {e}")
    else:
        print("ℹ️  Files saved but not committed to git")

def main():
    """Main function."""
    print("🎓 TEMPE HIGH SCHOOL TIMETABLE FETCHER")
    print("=" * 50)
    
    try:
        # Fetch XML content
        xml_data = fetch_xml_content()
        
        # Show summary
        print("📊 SUMMARY")
        print("=" * 40)
        valid_files = 0
        for filename, content in xml_data.items():
            if content and not content.startswith('<!-- Error:'):
                print(f"✅ {filename}: {len(content)} characters")
                valid_files += 1
            else:
                print(f"❌ {filename}: Failed to capture")
        
        print(f"\n📈 {valid_files}/{len(xml_data)} files captured successfully")
        
        if valid_files > 0:
            # Save and commit
            save_and_commit(xml_data)
            print(f"\n🎉 Process complete! {valid_files} files updated.")
        else:
            print("\n😞 No files were captured successfully")
            
    except KeyboardInterrupt:
        print("\n\n⏹️  Process cancelled by user")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()
