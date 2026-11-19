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
        print(rand.choice(book_name))

    def add_to_library(self, book_name: str, author_name: str, year: int, pages: int):
        updated_dictionary = {"Book Name": book_name, "Release Date": year, "Pages": pages}
        self.data[author_name] = updated_dictionary

        author_row = {"Author": author_name, **updated_dictionary}
        with open('data.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Author", "Book Name", "Release Date", "Pages"])
            writer.writerow(author_row)
        return self.data
