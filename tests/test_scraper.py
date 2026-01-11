import pytest
from unittest.mock import patch

from scraper.api_client import fetch_employee_data
from scraper.data_transformer import transform_data


# ---------------- Testacase1----------------
# Verify JSON File Download
def test_json_download():
    with patch("scraper.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "employees": []
        }

        result = fetch_employee_data()

        assert result is not None
        assert isinstance(result, dict)
        assert "employees" in result


# ---------------- Testcase2----------------
# Verify JSON File Extraction
def test_json_extraction():
    data = {
        "employees": [
            {"id": 1, "first_name": "John", "salary": 5000}
        ]
    }

    df = transform_data(data)

    assert len(df) == 1
    assert df.iloc[0]["first_name"] == "John"


# ---------------- Testcase3 ----------------
# Validate File Type & Format
def test_file_type_and_format():
    with patch("scraper.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "employees": []
        }

        result = fetch_employee_data()

        assert isinstance(result, dict)              # JSON object
        assert isinstance(result["employees"], list) # JSON array


# ---------------- Testcase4 ----------------
# Validate Data Structure
def test_data_structure():
    data = {
        "employees": [
            {
                "id": 1,
                "first_name": "Alice",
                "last_name": "Smith",
                "salary": 7000
            }
        ]
    }

    df = transform_data(data)

    assert "id" in df.columns
    assert "first_name" in df.columns
    assert "salary" in df.columns


# -Testcase5----------------
# Handle Missing or Invalid Data
def test_invalid_status_code():
    with patch("scraper.api_client.requests.get") as mock_get:
        mock_get.return_value.status_code = 404

        result = fetch_employee_data()
        assert result is None
