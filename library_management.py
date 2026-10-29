
class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
        book = input("Enter book name: ").strip()

        if book:
            self.books.append(book)
            print("Book added successfully!")
        else:
            print("Book name cannot be empty.")

    def remove_book(self):
        book = input("Enter book name to remove: ").strip()

        if book in self.books:
            self.books.remove(book)
            print("Book removed successfully!")
        else:
            print("Book not found!")

    def issue_book(self):
        book = input("Enter book name to issue: ").strip()

        if book in self.books:
            self.books.remove(book)
            print("Book issued successfully!")
        else:
            print("Book not available!")

    def return_book(self):
        book = input("Enter book name to return: ").strip()

        if book:
            self.books.append(book)
            print("Book returned successfully!")
        else:
            print("Book name cannot be empty.")

    def display_books(self):
        if self.books:
            print("\nAvailable Books:")
            for book in self.books:
                print("-", book)
        else:
            print("No books available.")


library = Library()

while True:
    print("\n--- LIBRARY MANAGEMENT SYSTEM ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.remove_book()
    elif choice == "3":
        library.issue_book()
    elif choice == "4":
        library.return_book()
    elif choice == "5":
        library.display_books()
    elif choice == "6":
        print("Library system closed.")
        break
    else:
        print("Invalid choice! Try again.")
