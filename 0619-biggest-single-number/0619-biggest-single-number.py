import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    singles = my_numbers['num'].value_counts()
    singles = singles[singles == 1].index
    return pd.DataFrame({'num': [singles.max() if len(singles) else None]})

