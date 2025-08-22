#!/usr/bin/env python3
"""
Tempe High School Timetable Kiosk
Copyright (C) 2025 TempeHS

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <https://www.gnu.org/licenses/>.

Sentral REST API Client
=======================

This script provides access to Sentral's REST API endpoints including:
- Activity Vehicle endpoints
- Timetable data
- Student information
- And other school management data

Based on Sentral API documentation: https://development.sentral.com.au/

Usage:
    python sentral_rest_client.py
"""

import requests
import json
import sys
import os
import re
from typing import Optional, Dict, Any, List


def load_env_file(env_file_path: str = ".env") -> None:
    """
    Load environment variables from a .env file.

    Args:
        env_file_path (str): Path to the .env file
    """
    try:
        if os.path.exists(env_file_path):
            with open(env_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    # Skip empty lines and comments
                    if line and not line.startswith('#') and '=' in line:
                        key, value = line.split('=', 1)
                        key = key.strip()
                        value = value.strip()
                        # Remove quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        # Only set if not already in environment
                        if key not in os.environ:
                            os.environ[key] = value
    except Exception as e:
        print(f"Warning: Could not load .env file: {e}")


def load_config(config_file: str = "sentral_config.json") -> Dict[str, Any]:
    """
    Load configuration from JSON file and resolve environment variables.
    Automatically loads .env file if it exists.

    Args:
        config_file (str): Path to configuration file

    Returns:
        dict: Configuration data with environment variables resolved
    """
    # Load .env file if it exists
    load_env_file()

    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config_content = f.read()

        # Resolve environment variables in the format ${VAR_NAME}
        def replace_env_var(match):
            var_name = match.group(1)
            env_value = os.getenv(var_name)
            if env_value is None:
                print(f"❌ Environment variable '{var_name}' not found")
                return match.group(0)  # Return original if not found
            return env_value

        # Replace ${VAR_NAME} patterns with environment variable values
        resolved_content = re.sub(
            r'\$\{([^}]+)\}', replace_env_var, config_content)

        return json.loads(resolved_content)
    except FileNotFoundError:
        print(f"Configuration file '{config_file}' not found.")
        print("Please create the configuration file with your API credentials.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing configuration file: {e}")
        return None
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return None


class SentralAPIClient:
    """Client for interacting with Sentral REST API"""

    def __init__(self, base_url: str, api_key: str, tenant: str):
        """
        Initialize the Sentral API client.

        Args:
            base_url (str): Base URL for the Sentral instance (e.g., "https://tempe-h.sentral.com.au")
            api_key (str): API key for authentication
            tenant (str): Tenant identifier
        """
        self.base_url = base_url.rstrip('/')
        self.api_key = api_key
        self.tenant = tenant
        self.session = requests.Session()

        # Set default headers
        self.session.headers.update({
            'X-API-KEY': api_key,
            'X-API-TENANT': tenant,
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'User-Agent': 'Sentral-Python-Client/1.0'
        })

    @classmethod
    def from_config(cls, config_file: str = "sentral_config.json"):
        """
        Create SentralAPIClient from configuration file.

        Args:
            config_file (str): Path to configuration file

        Returns:
            SentralAPIClient: Configured client instance
        """
        config = load_config(config_file)
        if not config:
            return None

        api_config = config.get('sentral_api', {})
        base_url = api_config.get('base_url')
        api_key = api_config.get('api_key')
        tenant = api_config.get('tenant')

        if not all([base_url, api_key, tenant]):
            print("❌ Invalid configuration. Required: base_url, api_key, tenant")
            missing = []
            if not base_url:
                missing.append("base_url")
            if not api_key:
                missing.append("api_key (LISS_PASSWORD environment variable)")
            if not tenant:
                missing.append("tenant")
            print(f"❌ Missing configuration: {', '.join(missing)}")
            return None

        # Check if the API key still contains unresolved environment variable pattern
        if '${' in str(api_key):
            print("❌ API key environment variable was not resolved properly")
            print("❌ Please ensure 'LISS_PASSWORD' environment variable is set")
            return None

        if api_key == "your-sentral-rest-api-key-here":
            print("❌ Please update the API key in configuration file")
            return None

        return cls(base_url, api_key, tenant)

    def _make_request(self, method: str, endpoint: str, params: Optional[Dict] = None,
                      data: Optional[Dict] = None) -> Optional[Dict[str, Any]]:
        """
        Make a request to the Sentral API.

        Args:
            method (str): HTTP method (GET, POST, PUT, DELETE)
            endpoint (str): API endpoint (without base URL)
            params (dict): Query parameters
            data (dict): Request body data

        Returns:
            dict or None: Response data if successful, None if failed
        """
        url = f"{self.base_url}/restapi/v1/{endpoint.lstrip('/')}"

        try:
            print(f"Making {method} request to: {url}")
            if params:
                print(f"Parameters: {params}")
            if data:
                print(f"Data: {json.dumps(data, indent=2)}")

            response = self.session.request(
                method=method,
                url=url,
                params=params,
                json=data,
                timeout=30
            )

            print(f"Response Status Code: {response.status_code}")

            if response.status_code in [200, 201]:
                try:
                    return response.json()
                except json.JSONDecodeError:
                    print("Response is not valid JSON")
                    print(f"Response content: {response.text[:500]}...")
                    return None
            else:
                print(
                    f"API request failed with status code: {response.status_code}")
                print(f"Response: {response.text[:500]}...")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return None

    # Activity Vehicle Endpoints
    def get_activity_vehicles(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get activity vehicles.

        Args:
            **filters: Optional filters like date_from, date_to, activity_id, etc.

        Returns:
            List of activity vehicle records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request('GET', 'activity-vehicle', params=params)
        return response.get('data', []) if response else None

    def create_activity_vehicle(self, vehicle_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Create a new activity vehicle record.

        Args:
            vehicle_data (dict): Vehicle data to create

        Returns:
            Created vehicle record
        """
        return self._make_request('POST', 'activity-vehicle', data=vehicle_data)

    def update_activity_vehicle(self, vehicle_id: int, vehicle_data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Update an activity vehicle record.

        Args:
            vehicle_id (int): ID of the vehicle to update
            vehicle_data (dict): Updated vehicle data

        Returns:
            Updated vehicle record
        """
        return self._make_request('PUT', f'activity-vehicle/{vehicle_id}', data=vehicle_data)

    def delete_activity_vehicle(self, vehicle_id: int) -> bool:
        """
        Delete an activity vehicle record.

        Args:
            vehicle_id (int): ID of the vehicle to delete

        Returns:
            True if successful, False otherwise
        """
        response = self._make_request(
            'DELETE', f'activity-vehicle/{vehicle_id}')
        return response is not None

    # Timetable Endpoints
    def get_timetable(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get timetable data.

        Args:
            **filters: Filters like date_from, date_to, student_id, teacher_id, etc.

        Returns:
            List of timetable records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request('GET', 'timetable', params=params)
        return response.get('data', []) if response else None

    def get_timetable_periods(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get timetable periods.

        Args:
            **filters: Optional filters

        Returns:
            List of period records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request(
            'GET', 'timetable/periods', params=params)
        return response.get('data', []) if response else None

    def get_timetable_calendar_dates(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get timetable calendar dates.

        This endpoint retrieves calendar information including dates, day types,
        and associated timetable structure information.

        Args:
            **filters: Optional filters such as:
                - date_from (str): Start date (YYYY-MM-DD format)
                - date_to (str): End date (YYYY-MM-DD format)
                - calendar_id (int): Specific calendar ID
                - day_type (str): Filter by day type
                - include_holidays (bool): Include holiday dates
                - academic_year (int): Filter by academic year

        Returns:
            List of calendar date records with timetable information
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request(
            'GET', 'timetables/timetable-calendar-date', params=params)
        return response.get('data', []) if response else None

    # Student Endpoints
    def get_students(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get student data.

        Args:
            **filters: Filters like active_only, year_level, etc.

        Returns:
            List of student records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request(
            'GET', 'enrolments/student', params=params)
        return response.get('data', []) if response else None

    # Teacher/Staff Endpoints
    def get_staff(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get staff data.

        Args:
            **filters: Optional filters

        Returns:
            List of staff records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request('GET', 'staff', params=params)
        return response.get('data', []) if response else None

    # Activity Endpoints
    def get_activities(self, **filters) -> Optional[List[Dict[str, Any]]]:
        """
        Get activities.

        Args:
            **filters: Filters like date_from, date_to, activity_type, etc.

        Returns:
            List of activity records
        """
        params = {k: v for k, v in filters.items() if v is not None}
        response = self._make_request('GET', 'activities', params=params)
        return response.get('data', []) if response else None

    # Utility methods
    def test_connection(self) -> bool:
        """
        Test the API connection and authentication.

        Returns:
            True if connection successful, False otherwise
        """
        print("Testing Sentral API connection...")

        # Try different endpoints to test connectivity
        endpoints_to_try = [
            ('enrolments/student', 'students endpoint'),
            ('activities/activity', 'activities endpoint'),
            ('timetables/timetable-calendar-date', 'timetable calendar endpoint'),
            ('staff/staff', 'staff endpoint')
        ]

        for endpoint, description in endpoints_to_try:
            print(f"  Trying {description}...")
            response = self._make_request('GET', endpoint, params={'limit': 1})

            if response is not None:
                print(f"✅ API connection successful via {description}!")
                return True
            else:
                print(f"❌ Failed on {description}")

        print("❌ All endpoints failed - API connection unsuccessful!")
        return False

    def get_api_info(self) -> Optional[Dict[str, Any]]:
        """
        Get API information and available endpoints.

        Returns:
            API information
        """
        return self._make_request('GET', '')


def main():
    """Main function - load config and test API connection."""
    print("Sentral REST API Client")
    print("=" * 50)

    # Initialize client from configuration file
    client = SentralAPIClient.from_config()
    if not client:
        sys.exit(1)

    print(f"Base URL: {client.base_url}")
    print(f"Tenant: {client.tenant}")
    print(f"API Key: {client.api_key[:8]}...")

    # Test connection
    if client.test_connection():
        print("✅ API connection successful!")
        print("Client is ready to use.")

        # Example usage:
        print("\nExample usage:")
        print("vehicles = client.get_activity_vehicles()")
        print("timetable = client.get_timetable()")
        print("calendar_dates = client.get_timetable_calendar_dates()")
        print("students = client.get_students()")

    else:
        print("❌ API connection failed!")
        print("Please check your API key and credentials in sentral_config.json")


if __name__ == "__main__":
    main()
