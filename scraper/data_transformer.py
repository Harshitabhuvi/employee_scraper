import pandas as pd

def transform_data(json_data):
    """
    Accepts either:
    - a list of employees
    - or a dict with 'employees' key
    """

    # Handle both possible formats safely
    if isinstance(json_data, list):
        employees = json_data
    elif isinstance(json_data, dict):
        employees = json_data.get("employees", [])
    else:
        raise ValueError("Unsupported data format")

    df = pd.DataFrame(employees)

    # Handle hire_date only if present
    if "hire_date" in df.columns:
        df["hire_date"] = (
            pd.to_datetime(df["hire_date"], errors="coerce")
            .dt.strftime("%Y-%m-%d")
        )

    return df
