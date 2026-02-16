from main import Book, Library, Member

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
