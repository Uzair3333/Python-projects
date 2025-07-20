import csv
from datetime import datetime


# ---------------------------
# 📚 Book Class
# ---------------------------
class Book:
    fieldnames = ['title', 'author', 'ISBN', 'available']

    def __init__(self, title, author, ISBN, available=True):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.__available = available

    def append_book(self):
        with open('books.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Book.fieldnames)
            writer.writerow({
                'title': self.title,
                'author': self.author,
                'ISBN': self.ISBN,
                'available': str(self.__available)
            })
        print(f"📘 Book '{self.title}' by '{self.author}' has been added successfully!")

    @staticmethod
    def load_books():
        with open('books.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)

    @staticmethod
    def is_valid_isbn(isbn):
        if len(isbn) != 13 or not isbn.isdigit():
            return False
        total = 0
        for i in range(13):
            digit = int(isbn[i])
            total += digit if i % 2 == 0 else digit * 3
        return total % 10 == 0

    def __repr__(self):
        status = "✅ Available" if self.__available else "❌ Unavailable"
        return f"\n📕 Title: '{self.title}'\n✍️  Author: '{self.author}'\n🔢 ISBN: '{self.ISBN}'\n📦 Status: '{status}'\n"


# ---------------------------
# 👤 Member Class
# ---------------------------
class Member:
    fieldnames = ['name', 'ID', 'contact']

    def __init__(self, name, ID, contact):
        self.name = name
        self.ID = ID
        self.contact = contact

    def append_member(self):
        with open('members.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Member.fieldnames)
            writer.writerow({
                'name': self.name,
                'ID': self.ID,
                'contact': self.contact
            })
        print(f"🙋 Member '{self.name}' registered successfully!")

    @staticmethod
    def load_members():
        with open('members.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def __repr__(self):
        return f"\n🧑 Name: '{self.name}'\n🆔 ID: '{self.ID}'\n📞 Contact: '{self.contact}'\n"


# ---------------------------
# 🏛️ Library Class
# ---------------------------
class Library:
    transaction_fields = ['member_id', 'book_isbn', 'action', 'date']

    @staticmethod
    def borrow_book(member_id, isbn):
        books = Book.load_books()
        updated_books = []
        found = False
        book_available = False

        for book in books:
            if book['ISBN'] == isbn:
                found = True
                if book['available'] == 'True':
                    book['available'] = 'False'
                    book_available = True
            updated_books.append(book)

        if not found:
            print("❌ Book not found in the catalog.")
            return
        elif not book_available:
            print("⚠️ Book is currently unavailable for borrowing.")
            return

        with open('books.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Book.fieldnames)
            writer.writeheader()
            writer.writerows(updated_books)

        with open('transactions.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Library.transaction_fields)
            writer.writerow({
                'member_id': member_id,
                'book_isbn': isbn,
                'action': 'borrow',
                'date': datetime.now().strftime("%Y-%m-%d")
            })

        print(f"📚 Book with ISBN '{isbn}' has been successfully borrowed by Member ID '{member_id}'!")

    @staticmethod
    def return_book(member_id, isbn):
        books = Book.load_books()
        updated_books = []

        for book in books:
            if book['ISBN'] == isbn:
                book['available'] = 'True'
            updated_books.append(book)

        with open('books.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Book.fieldnames)
            writer.writeheader()
            writer.writerows(updated_books)

        with open('transactions.csv', 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=Library.transaction_fields)
            writer.writerow({
                'member_id': member_id,
                'book_isbn': isbn,
                'action': 'return',
                'date': datetime.now().strftime("%Y-%m-%d")
            })

        print(f"✅ Book with ISBN '{isbn}' successfully returned by Member ID '{member_id}'.")

    @staticmethod
    def view_transactions():
        try:
            with open('transactions.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                print("\n📜 Transaction History:")
                for row in reader:
                    print(f"🔁' {row['date']}' | Member: '{row['member_id']}' | Book: '{row['book_isbn']}' | Action: '{row['action']}'")
        except FileNotFoundError:
            print("❌ No transactions found yet.")

# ----------------------
# 1. Add Books to Library
# ----------------------
print("\n🔧 Adding Books...")
book1 = Book("The Pragmatic Programmer", "Andy Hunt", "9780135957059", True)
book2 = Book("Clean Code", "Robert C. Martin", "9780132350884", True)
book1.append_book()
book2.append_book()

# ----------------------
# 2. Register Members
# ----------------------
print("\n📝 Registering Members...")
member1 = Member("Alice", "M001", "alice@example.com")
member2 = Member("Bob", "M002", "bob@example.com")
member1.append_member()
member2.append_member()

# ----------------------
# 3. Borrow Book
# ----------------------
print("\n📖 Borrowing a Book...")
Library.borrow_book(member_id="M001", isbn="9780135957059")  # Alice borrows

# ----------------------
# 4. Return Book
# ----------------------
print("\n📦 Returning a Book...")
Library.return_book(member_id="M001", isbn="9780135957059")

# ----------------------
# 5. View Transaction History
# ----------------------
print("\n📜 Transaction Log:")
Library.view_transactions()
