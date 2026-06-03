import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    # Join on product_id
    df = prices.merge(units_sold, on='product_id', how='left')

    # Keep only sales within the valid price period
    df = df[
        (df['purchase_date'] >= df['start_date']) &
        (df['purchase_date'] <= df['end_date'])
    ]

    # Revenue for each sale
    df['revenue'] = df['price'] * df['units']

    # Aggregate revenue and units
    result = (
        df.groupby('product_id')
          .agg(total_revenue=('revenue', 'sum'),
               total_units=('units', 'sum'))
          .reset_index()
    )

    # Compute weighted average price
    result['average_price'] = (
        result['total_revenue'] / result['total_units']
    ).round(2)

    # Include products with no sales
    result = (
        prices[['product_id']]
        .drop_duplicates()
        .merge(
            result[['product_id', 'average_price']],
            on='product_id',
            how='left'
        )
    )

    result['average_price'] = result['average_price'].fillna(0)

    return result
    