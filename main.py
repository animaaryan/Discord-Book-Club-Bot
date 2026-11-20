from flask import Flask, render_template, url_for, request, redirect
import library

app = Flask(__name__)

library = library.Library()


@app.route('/')
def index():
    return render_template("index.html")


@app.route("/random/", methods=['POST'])
def select_book():
    book_random = library.choose_book()
    return render_template('index.html', book=book_random)


@app.route("/add/", methods=['POST'])
def add_book():
    name = request.form["name"]
    author = request.form["author"]
    year = int(request.form["year"])
    pages = int(request.form["pages"])
    library.add_to_library(name, author, year, pages)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

# Create a CSV File
# make_csv = library.create_csv()
# # sort_dict = library.sort_dictionary(1)
# # book_random = library.choose_book()
# print("_" * 20)
# library.sort_dictionary(2)
# print("_" * 20)
# # library.sort_dictionary(1)
# # print("_" * 20)
# library.remove_from_library("Hunger Games")
# print("_" * 20)
# library.sort_dictionary(2)
