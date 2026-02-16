# 🧾 User Input Validation Toolkit
# -----------------------------------------
# ✅ Validates: Username, Email, and Age
# 🎯 Concepts: Strings, Conditionals, Error Handling, Input Validation
# 🧠 Author: Uzair
# -----------------------------------------

# ---------------------------
# 🧑 Username Validation
# ---------------------------
def validate_user_name():
    print("\n=== 🧑 USERNAME VALIDATION ===")
    user_name = input("Enter username: ").strip()

    # Check for non-empty username
    if len(user_name) < 1:
        print("❌ Invalid — username cannot be empty.")
        return

    # Check that username contains only letters and spaces
    if all(char.isalpha() or char.isspace() for char in user_name):
        print("✅ Valid Username!")
    else:
        print("❌ Invalid — username should contain only alphabets and spaces.")


# ---------------------------
# 📧 Email Validation
# ---------------------------
def validate_email():
    print("\n=== 📧 EMAIL VALIDATION ===")
    email = input("Enter Email: ").strip()

    # 1️⃣ Must have exactly one '@'
    if email.count('@') != 1:
        print("❌ Invalid — email must contain exactly one '@'.")
        return

    # Split into username and domain parts
    user_name, domain = email.split('@', 1)

    # 2️⃣ Basic username/domain presence check
    if not user_name or not domain:
        print("❌ Invalid — email missing username or domain part.")
        return

    # 3️⃣ Domain must have at least one '.' and not at start or end
    if "." not in domain or domain.startswith('.') or domain.endswith('.'):
        print("❌ Invalid — domain part is malformed (e.g. gmail.com).")
        return

    # 4️⃣ Should not start or end with '@' or '.'
    if email.startswith(('@', '.')) or email.endswith(('@', '.')):
        print("❌ Invalid — email cannot start or end with '@' or '.'.")
        return

    print("✅ Valid Email Address!")


# ---------------------------
# 🎂 Age Validation
# ---------------------------
def validate_age():
    print("\n=== 🎂 AGE VALIDATION ===")
    age_input = input("Enter your age: ").strip()

    try:
        age = int(age_input)
    except ValueError:
        print("❌ Invalid — please enter a numeric value.")
        return

    # Check realistic age range
    if age < 0 or age > 120:
        print("⚠️ Invalid — please enter a realistic age (0–120).")
    else:
        print("✅ Valid Age!")


# ---------------------------
# 🚀 Main Program Execution
# ---------------------------
def main():
    print("=" * 40)
    print("🧮 USER INPUT VALIDATION TOOL")
    print("=" * 40)

    validate_user_name()
    validate_email()
    validate_age()

    print("\n🎉 Validation Complete — Thanks for using the tool!")
    print("=" * 40)


# ---------------------------
# ▶️ Entry Point
# ---------------------------
if __name__ == "__main__":
    main()
