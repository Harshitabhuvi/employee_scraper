from scraper.api_client import fetch_employee_data
from scraper.data_transformer import transform_data

def main():
    data = fetch_employee_data()

    if not data:
        print("Failed to fetch data")
        return

    df = transform_data(data)
    print(df.head())

if __name__ == "__main__":
    main()
