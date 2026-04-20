import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    df = visits.merge(transactions, on = 'visit_id', how = 'left')
    df = df[df['transaction_id'].isna()]
    result = df.groupby('customer_id').size().reset_index(name='count_no_trans')
    return result