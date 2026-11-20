# Import pandas library
import csv

import pandas as pd

# Import random module
import random as rand

# File path
FILE_PATH = "data.csv"


# Create a class named Library
class Library:
    def __init__(self):
        self.data = {
            'Author 01': {"Book Name": "Alice in Wonderland", "Release Date": 2022, "Pages": 500},
            'Author 02': {"Book Name": "The Wizard of Oz", "Release Date": 2002, "Pages": 300},
            'Author 03': {"Book Name": "Macbeth", "Release Date": 1992, "Pages": 200}
        }

    # Sort by release date or page count
    def sort_dictionary(self, user_prompt):

        if user_prompt == 1:
            print("Sorting by Release Date...")
            by_years = dict(sorted(self.data.items(),
                                   key=lambda x: x[1]["Release Date"]))
            for year in by_years.items():
                print(year)

        elif user_prompt == 2:
            print("Sorting by Page Count...")
            by_pages = dict(sorted(self.data.items(),
                                   key=lambda x: x[1]["Pages"], reverse=True))

            for page in by_pages.items():
                print(page)

        else:
            raise "Incorrect Number Entered"

    def create_csv(self) -> str:
        # Create DataFrame
        df = pd.DataFrame(self.data)

        # Write to the CSV File
        df.to_csv(FILE_PATH, index=False)

        # Print if done
        return f'CSV file "{FILE_PATH}" has been created successfully.'

    def choose_book(self):
        book_name = [name["Book Name"] for name in self.data.values()]
        print(f"Book for the month is: {rand.choice(book_name)}")

    def add_to_library(self, book_name: str, author_name: str, year: int, pages: int):

        # Store a dictionary
        updated_dictionary = {"Book Name": book_name, "Release Date": year, "Pages": pages}

        # Let's keep fieldnames separate
        fieldnames = ["Author", "Book Name", "Release Date", "Pages"]

        # Assign the author name to updated dictionary
        self.data[author_name] = updated_dictionary

        # **kwargs, we'll throw in the argument
        author_row = {"Author": author_name, **updated_dictionary}

        # Open the csv file and add a row
        with open('data.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            print(f"Added '{updated_dictionary["Book Name"]}' to the library")
            writer.writerow(author_row)
        return self.data

    def remove_from_library(self, book_name: str):

        # Store the found book in a list
        found_book = [name for name in self.data.items() if book_name == name[1]['Book Name']]

        # If we do not find a book
        if not found_book:
            print(f"'{book_name}' not found.")
            return self.data

        # Remove the book at index
        for name in found_book:
            print(f"Removing {book_name}")
            del self.data[name[0]]

        return self.data
