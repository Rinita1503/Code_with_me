import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    newEmployee = employee.merge(employee, left_on = 'managerId', right_on = 'id', suffixes=('_emp', '_mgr'))
    df = newEmployee[newEmployee['salary_emp'] > newEmployee['salary_mgr']]
    return df[['name_emp']].rename(columns = {'name_emp':'Employee'})
    