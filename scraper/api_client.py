import requests
import logging

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

def fetch_employee_data(retries=3):
    try:
        response = requests.get(URL, timeout=10)

        if response.status_code != 200:
            logging.error(f"Failed with status code {response.status_code}")
            return None

        return response.json()

    except requests.exceptions.RequestException as e:
        logging.error(f"API error: {e}")
        if retries > 0:
            return fetch_employee_data(retries - 1)
        return None

