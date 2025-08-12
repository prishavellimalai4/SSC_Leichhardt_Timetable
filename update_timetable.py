#!/usr/bin/env python3
"""
Timetable Update Script for Tempe High School
Downloads XML content from Sentral and serves it locally.
"""

import requests
import os
import subprocess
import threading
import time
from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

# URLs to download from
URLS = {
    'bell_times.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishBellTimes.debug',
    'calendar.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishCalendar.debug',
    'liss_info.xml': 'https://tempe-h.sentral.com.au/s-mDQd7r/timetables/liss_info?debug=webedval/liss.publishTimetable.debug'
}

class TimetableHandler(SimpleHTTPRequestHandler):
    """Custom HTTP handler to serve XML content and static files."""
    
    def __init__(self, *args, xml_data=None, **kwargs):
        self.xml_data = xml_data or {}
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests."""
        path = self.path.lstrip('/')
        
        # Serve XML files from memory
        if path in self.xml_data:
            self.send_response(200)
            self.send_header('Content-Type', 'application/xml')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(self.xml_data[path].encode('utf-8'))
            return
        
        # Serve static files normally
        return super().do_GET()

def download_xml_content():
    """Download XML content from URLs and return as dictionary."""
    xml_data = {}
    
    print("Downloading XML content...")
    print("⚠️  Note: These URLs require authentication through Sentral")
    
    for filename, url in URLS.items():
        try:
            print(f"Fetching {filename}...")
            
            # Add headers to mimic a browser
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'application/xml,text/xml,*/*',
                'Accept-Language': 'en-US,en;q=0.9',
            }
            
            response = requests.get(url, timeout=30, headers=headers)
            response.raise_for_status()
            
            # Check if we got XML or HTML
            content_type = response.headers.get('content-type', '').lower()
            
            if 'text/html' in content_type or response.text.strip().startswith('<!DOCTYPE html'):
                print(f"⚠️  {filename}: Received HTML (authentication required)")
                xml_data[filename] = f"""<?xml version="1.0" encoding="UTF-8"?>
<error>
    <message>Authentication required for {filename}</message>
    <note>This URL requires login through Sentral system</note>
    <url>{url}</url>
    <content_type>{content_type}</content_type>
</error>"""
            elif 'xml' in content_type or response.text.strip().startswith('<?xml'):
                xml_data[filename] = response.text
                print(f"✓ Successfully fetched {filename}")
            else:
                print(f"⚠️  {filename}: Unknown content type: {content_type}")
                xml_data[filename] = f"""<?xml version="1.0" encoding="UTF-8"?>
<error>
    <message>Unexpected content type for {filename}</message>
    <content_type>{content_type}</content_type>
    <content_preview>{response.text[:200]}</content_preview>
</error>"""
                
        except requests.exceptions.RequestException as e:
            print(f"✗ Error fetching {filename}: {e}")
            xml_data[filename] = f"""<?xml version="1.0" encoding="UTF-8"?>
<error>
    <message>Failed to fetch {filename}</message>
    <error>{str(e)}</error>
</error>"""
    
    return xml_data

def manual_xml_input():
    """Allow manual input of XML content."""
    xml_data = {}
    
    print("\n" + "="*50)
    print("MANUAL XML INPUT MODE")
    print("="*50)
    print("Since the URLs require authentication, you can manually paste XML content.")
    print("1. Login to Sentral in your browser")
    print("2. Visit each URL and copy the XML content")
    print("3. Paste it here when prompted")
    print("\nURLs to visit:")
    for filename, url in URLS.items():
        print(f"  {filename}: {url}")
    print()
    
    for filename in URLS.keys():
        print(f"\n--- {filename} ---")
        print("Paste the XML content (press Enter twice when done):")
        
        lines = []
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
            print(f"✓ Added content for {filename}")
        else:
            xml_data[filename] = f"""<?xml version="1.0" encoding="UTF-8"?>
<error>
    <message>No content provided for {filename}</message>
</error>"""
            print(f"⚠️  No content provided for {filename}")
    
    return xml_data

def start_local_server(xml_data, port=8000):
    """Start a local HTTP server serving XML content and static files."""
    
    def handler_factory(*args, **kwargs):
        return TimetableHandler(*args, xml_data=xml_data, **kwargs)
    
    server = HTTPServer(('localhost', port), handler_factory)
    print(f"🌐 Local server started at http://localhost:{port}")
    print("📄 Available XML files:")
    for filename in xml_data.keys():
        print(f"   - http://localhost:{port}/{filename}")
    print("📱 Main application: http://localhost:{port}/index.html")
    print("\nPress Ctrl+C to stop the server")
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Server stopped")
        server.shutdown()

def update_files_and_commit(xml_data):
    """Update local XML files and commit to git."""
    print("\nUpdating local files...")
    
    # Write XML content to files
    success_count = 0
    for filename, content in xml_data.items():
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"✓ Updated {filename}")
            success_count += 1
        except Exception as e:
            print(f"✗ Error writing {filename}: {e}")
    
    if success_count > 0:
        # Git operations
        try:
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
                print(f"Running: {' '.join(cmd)}")
                result = subprocess.run(cmd, capture_output=True, text=True)
                
                if result.returncode != 0:
                    if "nothing to commit" in result.stdout:
                        print("No changes to commit.")
                        break
                    else:
                        print(f"Git command failed: {result.stderr}")
                        return False
                else:
                    print(f"✓ {cmd[1]} completed successfully")
            
            print("✓ Files updated and committed to git")
            return True
            
        except Exception as e:
            print(f"✗ Error with git operations: {e}")
            return False
    
    return False

def main():
    """Main function to update timetable files and serve them locally."""
    print("=" * 50)
    print("Tempe High School Timetable Update Script")
    print("=" * 50)
    
    # Change to script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    print(f"Working directory: {script_dir}")
    
    # Check command line arguments
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "--server-only":
            # Just start the server with existing files
            xml_data = {}
            for filename in URLS.keys():
                try:
                    with open(filename, 'r', encoding='utf-8') as f:
                        xml_data[filename] = f.read()
                except FileNotFoundError:
                    xml_data[filename] = f"<error>File {filename} not found</error>"
            start_local_server(xml_data)
            return
        elif sys.argv[1] == "--update-only":
            # Just update files without starting server
            xml_data = download_xml_content()
            update_files_and_commit(xml_data)
            return
        elif sys.argv[1] == "--manual":
            # Manual XML input mode
            xml_data = manual_xml_input()
            print("\nOptions:")
            print("1. Start local server")
            print("2. Update local files and commit to git")
            print("3. Both")
            choice = input("\nEnter your choice (1/2/3): ").strip()
            
            if choice == "1":
                start_local_server(xml_data)
            elif choice == "2":
                update_files_and_commit(xml_data)
            elif choice == "3":
                update_files_and_commit(xml_data)
                print("\nStarting local server...")
                start_local_server(xml_data)
            return
    
    # Default: Try to download XML content automatically
    xml_data = download_xml_content()
    
    # Check if we got valid XML or authentication errors
    auth_errors = [k for k, v in xml_data.items() if '<error>' in v and 'authentication' in v.lower()]
    
    if auth_errors:
        print(f"\n⚠️  Authentication required for {len(auth_errors)} files")
        print("\nOptions:")
        print("1. Use manual input mode (recommended)")
        print("2. Start server with error placeholders")
        print("3. Update files with error placeholders")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1/2/3/4): ").strip()
        
        if choice == "1":
            xml_data = manual_xml_input()
        elif choice == "4":
            return
    
    success_count = len([k for k, v in xml_data.items() if not v.strip().startswith('<?xml version="1.0" encoding="UTF-8"?>\n<error>')])
    print(f"\nSummary: {success_count}/{len(xml_data)} files have valid content")
    
    # Ask user what to do
    print("\nOptions:")
    print("1. Start local server")
    print("2. Update local files and commit to git")
    print("3. Both (update files then start server)")
    
    choice = input("\nEnter your choice (1/2/3): ").strip()
    
    if choice == "1":
        start_local_server(xml_data)
    elif choice == "2":
        update_files_and_commit(xml_data)
    elif choice == "3":
        update_files_and_commit(xml_data)
        print("\nStarting local server...")
        start_local_server(xml_data)
    else:
        print("Invalid choice. Starting local server by default...")
        start_local_server(xml_data)

if __name__ == "__main__":
    main()
