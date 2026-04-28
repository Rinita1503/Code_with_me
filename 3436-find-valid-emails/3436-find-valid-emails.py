import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    regex = r"^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$"
    df = users[users['email'].str.match(regex)].sort_values(by = 'user_id', ascending = True)
    return df[['user_id','email']]