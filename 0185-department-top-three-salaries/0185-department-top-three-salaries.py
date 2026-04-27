import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(department, left_on='departmentId', right_on='id')
    result['rank'] = result.groupby('name_y')['salary'].rank(method='dense', ascending=False)
    result = result[result['rank'] <= 3]
    result = result[['name_y', 'name_x', 'salary']].rename(
    columns={'name_y': 'Department', 'name_x': 'Employee', 'salary': 'Salary'})
    return result[['Department','Employee','Salary']]

    