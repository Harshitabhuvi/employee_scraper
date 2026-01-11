# Employee Scraper – User Story 1

## 📌 Project Purpose
This project implements **User Story 1** by fetching employee data from an API,
transforming it into a structured format, and validating it using unit tests with mocking.

---

## 🛠 Tech Stack
- Python 3.12
- Requests
- Pandas
- Pytest
- unittest.mock

---

## 📂 Project Structure
employee_scraper/
│
├── scraper/
│ ├── init.py
│ ├── api_client.py
│ ├── data_transformer.py
│ └── main.py
│
├── tests/
│ ├── init.py
│ └── test_scraper.py
│
├── requirements.txt
├── pytest.ini
└── README.md

---

## ▶️ How to Run the Project
```bash
python -m scraper.main
pytest -v

✅ Test Cases Covered

Verify JSON file download (mocked API)

Verify JSON extraction

Validate file type and format

Validate data structure

Handle missing or invalid data

📝 Notes

API calls are mocked to avoid real network dependency

Virtual environment (venv/) is excluded using .gitignore
---

### 2️⃣ Commit the fix
```bash
git add README.md
git commit -m "Clean README for User Story 1"
git push origin user-story-1