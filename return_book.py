import json
import save_all_books

def return_book(all_books):
    try:
        with open("lended_books.json", "r") as file:
            lended_books = json.load(file)
    except FileNotFoundError:
        lended_books = []

    book_title = input("Enter the title of the book you're returning: ")
    borrower_name = input("Enter your name: ")

    
    for lend in lended_books:
        if lend["book_title"].lower() == book_title.lower() and lend["borrower_name"].lower() == borrower_name.lower():
            lended_books.remove(lend)
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    save_all_books.save_all_books(all_books)
                    print(f"Book returned successfully. Thank you!")
                    break
            with open("lended_books.json", "w") as file:
                json.dump(lended_books, file, indent=4)
            return all_books

    print("No matching lending record found.")
    return all_books
