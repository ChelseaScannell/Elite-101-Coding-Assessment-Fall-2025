from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def show_books():
    print("Available Books")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#loops through items in the library books list and gets the "available" element.
    for book in library_books:
        if book.get("available"):
            print(f"{book['id']}: \"{book['title']}\" by {book['author']}")
#if the book is available, prints out the id, title, and author of the book.

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books
def search_books():
    term = input("Type the author or genre of the book you're looking for: ").lower() #changes input to lowercase to avoid case sensitivity
    print("Matching books: ")
    #loops through library books, and if the book matches the term, prints out its id, title, and author. 
    for book in library_books:
        if term in book["author"].lower() or term in book["genre"].lower():
            print(f"{book['id']}: \"{book['title']}\" by {book['author']}")
        
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def check_out():
    check_id = input("Check out a book by ID: ")
#loops through books and checks if the input matches each book's id
    for book in library_books:
        if book["id"] == check_id:
#if the matching book is not available, prints that the book has been checked out already
            if not book.get("available", True):
                print("Book has already been checked out.")
                return
#due date is calculated by today's date + 14 days (2 weeks). If the book is successfully checked out, availability is changed to false and due date is set.
            due_date = datetime.today() + timedelta(days = 14)
            book["available"] = False
            book["due_date"] = due_date
            print(f"Successfully checked out {book['title']}. Return by {book['due_date']}.")

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def return_book():
#function matches the corresponding input id to one of the books, and if it is set to available, then shows that the book is not currently checked out.
    return_id = input("Type the ID of the book you want to return ")
    for book in library_books:
        if book["id"] == return_id:
            if book.get("available", True):
                print("This book is not currently checked out.")
                return
#after being returned, sets book to available and removes due date. 
            book["available"] = True
            book["due_date"] = None
            print(f"Successfully returned book.")

def overdue_books():
#function creates an overdue list for if the book isn't available plus if its due date is before today, then adds it to the list
    today = datetime.today()
    overdue = []
    for book in library_books:
        due = book.get("due_date")
        if (not book.get("available", True)) and due < today:
            overdue.append(book)
        return overdue

# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    show_books()
    print("\nOverdue books:")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#prints out items in overdue list
    overdue = overdue_books()
    if overdue:
        for due in overdue:
            print(f"{due['id']}: \"{due['title']}\" by {due['author']}, due {due['due_date']}")
    else:
        print("none")
    search_books()
    check_out()
    return_book()
