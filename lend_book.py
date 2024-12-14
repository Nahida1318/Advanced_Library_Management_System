
import json
import save_all_books
from datetime import datetime, timedelta


def lend_book(all_books):
    try:
        with open("lended_books.json", "r") as file:
            lended_books = json.load(file)
    except FileNotFoundError:
        lended_books = []

    
    book_title = input("Enter the title of the book you want to borrow: ")
    book_found = False

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            book_found = True
            if book["quantity"] > 0:
                borrower_name = input("Enter your name: ")
                borrower_phone = input("Enter your phone number: ")
                return_date = datetime.now() + timedelta(days=14)

                lend_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book["title"],
                    "return_due_date": return_date.strftime("%d-%m-%Y %H:%M:%S")
                }

                lended_books.append(lend_info)

                
                with open("lended_books.json", "w") as file:
                    json.dump(lended_books, file, indent=4)

                
                book["quantity"] -= 1
        
                save_all_books.save_all_books(all_books)
                print(f"Book lent successfully. Please return by {return_date.strftime('%d-%m-%Y')}")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books

    if not book_found:
        print("Book not found.")
    return all_books
