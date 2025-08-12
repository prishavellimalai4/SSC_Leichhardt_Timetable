#!/usr/bin/env python3
"""
Timetable Update Script for Tempe High School
Downloads XML content from Sentral and updates local files, then commits to git.
"""

import requests
import os
import sys
import subprocess
from datetime import datetime

# URLs to download from - using environment variables for security
URLS = {
    'bell_times.xml': os.getenv('BELTIMESURL'),
    'calendar.xml': os.getenv('CALURL'),
    'liss_info.xml': os.getenv('TTURL')
}

def download_file(url, filename):
    """Download content from URL and save to file."""
    try:
        print(f"Downloading {filename}...")
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        # Write content to file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(response.text)
        
        print(f"✓ Successfully updated {filename}")
        return True
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error downloading {filename}: {e}")
        return False
    except Exception as e:
        print(f"✗ Error saving {filename}: {e}")
        return False

def git_commit_and_push():
    """Commit changes and push to repository."""
    try:
        # Get current date and time
        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M:%S")
        commit_message = f"content update {time_str} and {date_str}"
        
        # Git commands
        commands = [
            ["git", "add", "bell_times.xml", "calendar.xml", "liss_info.xml"],
            ["git", "commit", "-m", commit_message],
            ["git", "push"]
        ]
        
        for cmd in commands:
            print(f"Running: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            
            if result.returncode != 0:
                if "nothing to commit" in result.stdout:
                    print("No changes to commit.")
                    return True
                else:
                    print(f"Git command failed: {result.stderr}")
                    return False
            else:
                print(f"✓ {cmd[1]} completed successfully")
        
        print(f"✓ Successfully committed and pushed changes")
        return True
        
    except Exception as e:
        print(f"✗ Error with git operations: {e}")
        return False

def main():
    """Main function to update timetable files."""
    print("=" * 50)
    print("Tempe High School Timetable Update Script")
    print("=" * 50)
    
    # Check for local testing mode
    if len(sys.argv) > 1 and sys.argv[1] == "--local-test":
        print("🧪 LOCAL TESTING MODE - Using hardcoded URLs")
        print("⚠️  WARNING: This mode should only be used for development/testing!")
        print()
        
        # Use hardcoded URLs for local testing
        global URLS
        URLS = {
            'bell_times.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishBellTimes.debug',
            'calendar.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishCalendar.debug',
            'liss_info.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishTimetable.debug'
        }
    else:
        # Validate environment variables
        required_vars = ['BELTIMESURL', 'CALURL', 'TTURL']
        missing_vars = [var for var in required_vars if not os.getenv(var)]
        
        if missing_vars:
            print("ERROR: The following required environment variables are not set:")
            for var in missing_vars:
                print(f"  - {var}")
            print("\nOptions:")
            print("1. Set these environment variables (for local testing)")
            print("2. Configure them as GitHub repository secrets (for production)")
            print("3. Run with '--local-test' flag for development testing")
            print("\nSee SCRIPT_SETUP.md for detailed instructions.")
            return
        
        # Validate that URLs are not None
        invalid_urls = [(filename, url) for filename, url in URLS.items() if url is None]
        if invalid_urls:
            print("ERROR: Some URLs are None. Check your environment variables:")
            for filename, url in invalid_urls:
                print(f"  - {filename}: {url}")
            return
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working directory: {script_dir}")
    
    # Download all files
    success_count = 0
    for filename, url in URLS.items():
        if download_file(url, filename):
            success_count += 1
    
    print(f"\nDownload Summary: {success_count}/{len(URLS)} files updated successfully")
    
    # Only commit if at least one file was downloaded successfully
    if success_count > 0:
        print("\nCommitting changes to git...")
        if git_commit_and_push():
            print("\n✓ Timetable update completed successfully!")
        else:
            print("\n✗ Timetable files updated but git operations failed")
    else:
        print("\n✗ No files were updated successfully - skipping git operations")

if __name__ == "__main__":
    main()
