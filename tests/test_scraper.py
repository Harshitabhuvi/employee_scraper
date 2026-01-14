import pytest
from unittest.mock import patch
from scraper.api_client import fetch_employee_data
from scraper.data_transformer import transform_data

def test_json_download():
    with patch("scraper.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"employees": []}
        assert fetch_employee_data() is not None

def test_full_name_creation():
    data = {"employees": [{"first_name": "John", "last_name": "Doe"}]}
    df = transform_data(data)
    assert df.iloc[0]["full_name"] == "John Doe"

def test_designation_logic():
    data = {"employees": [{"years_of_experience": 8}]}
    df = transform_data(data)
    assert df.iloc[0]["designation"] == "senior data engineer"

def test_phone_validation():
    data = {"employees": [{"phone": "123x456"}]}
    df = transform_data(data)
    assert df.iloc[0]["phone"] == "Invalid Number"

def test_hire_date_format():
    data = {"employees": [{"hire_date": "2021-06-15T00:00:00Z"}]}
    df = transform_data(data)
    assert df.iloc[0]["hire_date"] == "2021-06-15"

def test_invalid_status_code():
    with patch("scraper.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 500
        assert fetch_employee_data() is None
