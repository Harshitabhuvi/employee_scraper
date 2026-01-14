
import pandas as pd

EXPECTED_SCHEMA = [
    "id", "first_name", "last_name", "full_name", "email", "phone",
    "gender", "age", "job_title", "designation",
    "years_of_experience", "salary", "department", "hire_date"
]

def get_designation(years):
    if pd.isna(years):
        return None
    if years < 3:
        return "system engineer"
    elif 3 <= years <= 5:
        return "data engineer"
    elif 5 < years <= 10:
        return "senior data engineer"
    else:
        return "lead"

def transform_data(json_data):
    if not json_data:
        return pd.DataFrame(columns=EXPECTED_SCHEMA)

    employees = json_data.get("employees", []) if isinstance(json_data, dict) else json_data
    df = pd.DataFrame(employees)

    # Ensure schema
    for col in EXPECTED_SCHEMA:
        if col not in df.columns:
            df[col] = None

    # Full Name
    df["full_name"] = (
        df["first_name"].fillna("") + " " + df["last_name"].fillna("")
    ).str.strip()

    # Phone validation
    df["phone"] = df["phone"].astype(str)
    df.loc[df["phone"].str.contains("x", na=False), "phone"] = "Invalid Number"

    # Designation logic
    df["years_of_experience"] = pd.to_numeric(df["years_of_experience"], errors="coerce")
    df["designation"] = df["years_of_experience"].apply(get_designation)

    # Hire date formatting
    df["hire_date"] = pd.to_datetime(
        df["hire_date"], errors="coerce"
    ).dt.strftime("%Y-%m-%d")

    # Enforce data types
    df["email"] = df["email"].astype(str)
    df["gender"] = df["gender"].astype(str)
    df["job_title"] = df["job_title"].astype(str)
    df["department"] = df["department"].astype(str)

    df["age"] = pd.to_numeric(df["age"], errors="coerce").astype("Int64")
    df["salary"] = pd.to_numeric(df["salary"], errors="coerce").astype("Int64")
    df["years_of_experience"] = df["years_of_experience"].astype("Int64")

    return df[EXPECTED_SCHEMA]