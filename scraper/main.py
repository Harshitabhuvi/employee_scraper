
import logging
from scraper.api_client import fetch_employee_data
from scraper.data_transformer import transform_data

def main():
    data = fetch_employee_data()

    if data is None:
        logging.error("Pipeline stopped due to API failure")
        return

    df = transform_data(data)
    logging.info(f"Total records processed: {len(df)}")
    print(df.head())

if __name__ == "__main__":
    main()