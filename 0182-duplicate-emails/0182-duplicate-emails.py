import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby('email').size().reset_index(name='count')
    df = df[df['count'] > 1]
    return df[['email']].rename(columns={'email': 'Email'})
    