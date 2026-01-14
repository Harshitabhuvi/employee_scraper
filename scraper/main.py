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

    display_cols = [
        "id", "full_name", "designation", "phone", "hire_date"
    ]

    print("\nSample Output (Key Fields):")
    print(df[display_cols].head())   # ✅ no fake values

if __name__ == "__main__":
    main()
