# from flask import Flask, render_template, request
# import random as rand
from envs.nlp_course_env.Lib.datetime import date

import library

# Create a CSV File
library = library.Library()
make_csv = library.create_csv()
print(make_csv)

sort_dict = library.sort_dictionary(2)
print(sort_dict)
