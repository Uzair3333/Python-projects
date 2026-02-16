# 🏛️ Project 2: Library Book Tracker
# 🎯 Purpose: Manage books — add, view, search, borrow, return, and remove
# 🧠 Concepts Used: Lists, Dictionaries, Loops, Conditionals, Input Handling

# 📚 Initial book collection
books = [
    {
        "title": "1984",
        "author": "George Orwell",
        "year": 1949,
        "available": True
    }
]

# --------------------------
# 🖥️ Display Main Menu
# --------------------------
print("-" * 40)
print("📖        LIBRARY BOOK TRACKER")
print("-" * 40)
print("1️⃣  Add New Book")
print("2️⃣  View All Books")
print("3️⃣  Search Book by Title")
print("4️⃣  Borrow a Book")
print("5️⃣  Return a Book")
print("6️⃣  Remove a Book")
print("7️⃣  Exit Program")
print("-" * 40)

# --------------------------
# 🚀 Main Program Loop
# --------------------------
while True:
    user_choice = input("👉 Choose one of the above options: ").strip()
    print("-" * 40)

    # ➕ Add a New Book
    if user_choice == "1":
        new_title = input("Enter Book Title: ").strip()
        new_author = input("Enter Author Name: ").strip()
        new_year = input("Enter Year of Publication: ").strip()
        new_book = {"title": new_title, "author": new_author, "year": new_year, "available": True}
        books.append(new_book)
        print(f"✅ Book '{new_title}' added successfully!")
        print("-" * 40)

    # 👀 View All Books
    elif user_choice == "2":
        if not books:
            print("📭 No books in the library yet!")
        else:
            for book in books:
                status = "✅ Available" if book["available"] else "❌ Borrowed"
                print(f"📘 '{book['title']}' by {book['author']} ({book['year']}) — {status}")
        print("-" * 40)

    # 🔎 Search Book by Title
    elif user_choice == "3":
        title_search = input("Enter the book title to search: ").casefold()
        found = False
        for book in books:
            if book["title"].casefold() == title_search:
                status = "✅ Available" if book["available"] else "❌ Borrowed"
                print(f"📖 Found: '{book['title']}' by {book['author']} ({book['year']}) — {status}")
                found = True
        if not found:
            print("⚠️  No book found with that title.")
        print("-" * 40)

    # 📕 Borrow a Book
    elif user_choice == "4":
        title_search = input("Enter the title of the book to borrow: ").casefold()
        found = False
        for book in books:
            if book["title"].casefold() == title_search:
                found = True
                if book["available"]:
                    book["available"] = False
                    print(f"🎉 You borrowed '{book['title']}'. Enjoy reading!")
                else:
                    print("⚠️  That book is already borrowed.")
        if not found:
            print("❌ Book not found in the library.")
        print("-" * 40)

    # 📗 Return a Book
    elif user_choice == "5":
        title_search = input("Enter the title of the book to return: ").casefold()
        found = False
        for book in books:
            if book["title"].casefold() == title_search:
                found = True
                if not book["available"]:
                    book["available"] = True
                    print(f"✅ '{book['title']}' has been returned successfully!")
                else:
                    print("⚠️  That book wasn’t borrowed.")
        if not found:
            print("❌ Book not found in the library.")
        print("-" * 40)

    # 🗑️ Remove a Book
    elif user_choice == "6":
        title_remove = input("Enter the title of the book to remove: ").casefold()
        found = False
        for book in books[:]:  # copy list to avoid iteration errors
            if book["title"].casefold() == title_remove:
                books.remove(book)
                print(f"🗑️  Book '{book['title']}' removed successfully.")
                found = True
        if not found:
            print("⚠️  Book not found in database.")
        print("-" * 40)

    # 🚪 Exit Program
    elif user_choice == "7":
        print("👋 Thank you for using Library Book Tracker!")
        break

    # ❌ Invalid Choice
    else:
        print("⚠️  Invalid choice. Please select a valid option.")
        print("-" * 40)
