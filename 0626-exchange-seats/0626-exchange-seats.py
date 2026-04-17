import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    n = len(seat)
    
    seat['id'] = seat['id'].apply(
        lambda x: x + 1 if x % 2 == 1 and x != n else x - 1 if x % 2 == 0 else x
    )
    
    return seat.sort_values('id')