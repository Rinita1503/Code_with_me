import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    result = employee.merge(department, left_on='departmentId', right_on='id')
    # After merging two columns names are: name_x is employee name and name_y is department name.
    result = result[result['salary'] == result.groupby('name_y')['salary'].transform('max')]
    result = result[['name_y', 'name_x', 'salary']].rename(
    columns={'name_y': 'Department', 'name_x': 'Employee'})
    return result[['Department','Employee','salary']]
