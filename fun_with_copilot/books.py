#import csv
import csv

def highest_grossing_book(books):
    """
    This function takes a csv file containing book data and returns the title of the book with the highest grossing sales.
    The csv file should have the following columns: Title, Author, Price, and Quantity. The book's highest grossing sales is calculated by
    multiplying the price by the quantity sold. Return the title of the highest grossing book.
    If multiple books have the same highest grossing sales, return the first such book.
    >>> highest_grossing_book('books.csv')
    'Darkfall'
    """
    highest_grossing = 0
    title = ""
    with open(books, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            try:
                if len(row) >= 4:  # Ensure the row has at least 4 elements
                    price = float(row[2])
                    quantity = int(row[3])
                    grossing = price * quantity
                    if grossing > highest_grossing:
                        highest_grossing = grossing
                        title = row[0]
            except ValueError:
                # Skip rows with invalid data
                continue
    return title

import doctest
doctest.testmod(verbose=True)

