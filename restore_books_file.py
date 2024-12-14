import json
import os

def restore_all_books(all_books):
    if os.path.exists("all_books.json"):
        with open("all_books.json", "r") as fp:
            all_books = json.load(fp)
    else:
        print("No book data found. Starting with an empty library.")
        all_books = []

    return all_books
