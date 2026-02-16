# 🏦 Simple ATM Machine
# --------------------------------------------
# Concepts Used:
# ✅ Menu-driven CLI interface
# ✅ Input handling and balance management
# ✅ Loops, conditionals, and error checking
# --------------------------------------------

def main():
    balance = 0.0

    print("🏦 Welcome to the Python ATM")
    print("-" * 40)
    print("1️⃣  Check Balance")
    print("2️⃣  Deposit Money")
    print("3️⃣  Withdraw Money")
    print("4️⃣  Exit")
    print("-" * 40)

    while True:
        try:
            option = int(input("💡 Choose an option (1–4): "))
        except ValueError:
            print("❌ Invalid input. Enter a number between 1–4.")
            continue

        if option == 1:
            print(f"💰 Current Balance: ${balance:.2f}")
        elif option == 2:
            try:
                amount = float(input("Enter amount to deposit: $"))
                balance += amount
                print(f"✅ Deposited ${amount:.2f} successfully!")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif option == 3:
            try:
                amount = float(input("Enter amount to withdraw: $"))
                if amount <= balance:
                    balance -= amount
                    print(f"💸 Withdrawn ${amount:.2f} successfully!")
                else:
                    print("⚠️ Insufficient balance!")
            except ValueError:
                print("❌ Please enter a valid number.")
        elif option == 4:
            print("👋 Thank you for using Python ATM. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select between 1–4.")

        print("-" * 40)

if __name__ == "__main__":
    main()
