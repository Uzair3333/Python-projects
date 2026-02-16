# This is for practicing OOP again in Python
# There goes the practice projects one by one

# 🏦 Project #1: Bank Account Management System
# ---------------------------------------------------
# We’ve got a bank vault 🔐, a deposit counter 💰, 
# an ATM machine 🏧 for withdrawals,
# a "Balance Inquiry Machine™" 🖥️ for nosy customers 😅,
# and now… TRANSACTION HISTORY 📜 (like your stalker friend).
# ---------------------------------------------------

# 🚨 Custom Exceptions = Special Error Messages (with personality 😎)
class InsufficientFundsError(Exception):
    def __init__(self, message="💀 Bro, you're broke! Insufficient funds. Sell your kidney maybe? (just kidding 😂)"):
        super().__init__(message)

class InvalidDepositError(Exception):  # ✅ Fixed spelling
    def __init__(self, message="😡 Error: Bro, you can’t deposit zero or negative money… this isn’t a withdrawal machine! 🚫"):
        super().__init__(message)

class InvalidWithdrawError(Exception):
    def __init__(self, message="😡 Error: Nice try hacker, but you can’t withdraw zero or negative money 🚫"):
        super().__init__(message)


# 🏦 Main BankAccount Class
class BankAccount:

    def __init__(self, account_number, account_holder_name, balance=0):
        # Like your "New Account Form" 📋
        self.account_number = account_number  
        self.account_holder_name = account_holder_name  
        self.balance = balance
        self.history = []  # stores all deposits/withdrawals (your personal FBI agent 🕵️)

    # Makes account details readable instead of ugly <object at 0x7ff...>
    def __str__(self):
        return f"Account Number: {self.account_number} | Account Holder's Name: {self.account_holder_name} | Balance: ${self.balance}"

    # 💰 Deposit Method
    def deposit(self, amount):
        if amount <= 0:
            raise InvalidDepositError()
        else:
            self.balance += amount
            self.history.append({
                "Type": "Deposit",
                "Amount": f"${amount}",
                "Balance After": f"{self.balance}"
            })
            print(f"🎉 Deposit Successful! ${amount} has been added to your account.")
            print(f"💵 Current Balance: ${self.balance}\n")
            print("👉 Tip: Don’t spend it all on pizza 🍕 or gaming skins 🎮\n")

    # 🏧 Withdraw Method
    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidWithdrawError()
        elif amount > self.balance:
            raise InsufficientFundsError()
        else:
            self.balance -= amount
            self.history.append({
                "Type": "Withdraw",
                "Amount": f"${amount}",
                "Balance After": f"{self.balance}"
            })
            print(f"🎉 Withdrawal Successful! You withdrew ${amount}.")
            print(f"💵 Remaining Balance: ${self.balance}\n")
            print("👉 Pro Tip: Don’t withdraw everything… keep some for Netflix subscription 🍿\n")
        
    # 👀 Balance Check Method
    def check_balance(self):
        print("📊 Balance Inquiry:")
        print(f"👉 Current Balance: ${self.balance} 💵 (Don’t flex too hard, Elon Musk 🤣)\n")

    # 📜 Show History (formatted)
    def show_history(self):
        print("\n📜 Transaction History:")
        if not self.history:
            print("🤷 No transactions yet. Start flexing your money 💸\n")
        else:
            for entry in self.history:
                print(f"👉 {entry['Type']}: {entry['Amount']} | Balance After: ${entry['Balance After']}")
        print()  # empty line for spacing


# 🎉 Step 2: Create an account
my_acc = BankAccount("15602", "SwatStormer", 5000)

# 🖨️ Step 3: Print the account details
print("📝 Account Details:")
print(my_acc)
print("-" * 50)

# 🚀 Step 4: Test deposit, withdraw, and balance check (with try/except)
try:
    my_acc.deposit(100)
    my_acc.deposit(-50)   # ❌ test invalid deposit
except Exception as e:
    print(e, "\n")

try:
    my_acc.withdraw(200)   # ✅ valid withdraw
    my_acc.withdraw(10000) # ❌ more than balance
    my_acc.withdraw(-50)   # ❌ invalid withdraw
except Exception as e:
    print(e, "\n")

# Balance Inquiry
my_acc.check_balance()

# Show Transaction History
my_acc.show_history()