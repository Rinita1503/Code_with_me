import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    unique_salaries = (
        employee["salary"]
        .drop_duplicates()
        .sort_values(ascending=False)
        .reset_index(drop=True)
    )

    col_name = f"getNthHighestSalary({N})"

    if N <= 0 or len(unique_salaries) < N:
        return pd.DataFrame({col_name: [None]})

    return pd.DataFrame({col_name: [unique_salaries.iloc[N - 1]]})