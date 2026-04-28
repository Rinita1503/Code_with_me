import pandas as pd

def find_books_with_no_available_copies(library_books: pd.DataFrame, borrowing_records: pd.DataFrame) -> pd.DataFrame:
    # 1. Filter for active borrowers (where return_date is null)
    active_borrowers = borrowing_records[borrowing_records['return_date'].isna()]
    
    # 2. Count current borrowers per book
    borrow_counts = (
        active_borrowers.groupby('book_id')
        .size()
        .reset_index(name='current_borrowers')
    )
    
    # 3. Merge with library_books to get total_copies info
    merged_df = library_books.merge(borrow_counts, on='book_id', how='inner')
    
    # 4. Filter for books where current_borrowers equals total_copies
    no_copies_left = merged_df[merged_df['current_borrowers'] == merged_df['total_copies']]
    
    # 5. Select required columns and sort
    # Order by current_borrowers (DESC), then by title (ASC)
    result = no_copies_left[
        ['book_id', 'title', 'author', 'genre', 'publication_year', 'current_borrowers']
    ].sort_values(by=['current_borrowers', 'title'], ascending=[False, True])
    
    return result
