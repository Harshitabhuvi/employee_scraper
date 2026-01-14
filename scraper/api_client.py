import requests
import logging
import time
from requests.exceptions import RequestException, Timeout

URL = "https://api.slingacademy.com/v1/sample-data/files/employees.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def fetch_employee_data(retries=3, timeout=10, backoff=2):
    for attempt in range(1, retries + 1):
        try:
            logging.info(f"API call attempt {attempt}")
            response = requests.get(URL, timeout=timeout)

            if response.status_code != 200:
                logging.error(f"Non-200 status code received: {response.status_code}")
                return None

            logging.info("Data fetched successfully")
            return response.json()

        except Timeout:
            logging.warning("Request timed out")
        except RequestException as e:
            logging.error(f"Request failed: {e}")

        sleep_time = backoff ** attempt
        logging.info(f"Retrying after {sleep_time} seconds...")
        time.sleep(sleep_time)

    logging.critical("All retry attempts failed")
    return None
