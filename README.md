# Employee Scraper – User Story 1

## 📌 Project Purpose
This project implements **User Story 1**, which involves fetching employee data from an API, transforming it into a structured format, and validating it using unit tests with mocking.

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
│   ├── __init__.py
│   ├── api_client.py
│   ├── data_transformer.py
│   └── main.py
│
├── tests/
│   ├── __init__.py
│   └── test_scraper.py
│
├── requirements.txt
├── pytest.ini
└── README.md

---

---

## 🔧 What I fixed (important)

✅ Replaced **`init.py` → `__init__.py`** (Python requirement)  
✅ Proper Markdown formatting  
✅ Removed terminal instructions from README body  
✅ Clear structure for reviewers  
✅ Matches **User Story + PR expectations**

---

## 📌 What to do next (VERY IMPORTANT)

1. Save this as **README.md**
2. Commit it:
```bash
git add README.md
git commit -m "Add README for User Story 1"
git push origin user-story-1

## ▶️ How to Run the Project

### 1️⃣ Run the application
```bash
python -m scraper.main
