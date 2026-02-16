# 🔐 Login & Registration System
# ---------------------------------
# Concepts Used:
# ✅ Dictionaries for user data
# ✅ Conditionals & loops
# ✅ Basic validation and input handling
# ---------------------------------

users = {
    "kamran": "54321",
    "abdullah": "34654"
}

print("🔐 Welcome to the Login & Registration System")
print("-" * 45)

while True:
    print("\n1️⃣  Register")
    print("2️⃣  Login")
    print("3️⃣  Exit")
    print("-" * 30)

    try:
        choice = int(input("👉 Enter your choice (1-3): "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    if choice == 1:
        username = input("Enter a new username: ").strip().lower()
        password = input("Enter a new password: ").strip()
        if username in users:
            print("⚠️ Username already exists. Try another one.")
        else:
            users[username] = password
            print("✅ Registration successful!")

    elif choice == 2:
        username = input("Enter username: ").strip().lower()
        password = input("Enter password: ").strip()
        if username in users and users[username] == password:
            print("🎉 Login successful! Welcome back!")
        else:
            print("❌ Invalid username or password.")

    elif choice == 3:
        print("👋 Goodbye! Have a great day!")
        break

    else:
        print("❌ Invalid input. Choose a number between 1–3.")
