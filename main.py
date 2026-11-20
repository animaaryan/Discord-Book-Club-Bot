# from flask import Flask, render_template, request
import library

# Create a CSV File
library = library.Library()
# make_csv = library.create_csv()
# sort_dict = library.sort_dictionary(1)
# book_random = library.choose_book()
add_book = library.add_to_library("Hunger Games", "Suzanne Collins", 2012, 520)
library.sort_dictionary(2)
print(library.remove_from_library("Hunger Games"))
library.sort_dictionary(2)

