
# ---

### 🧠 `calculator.py` (fully commented and ready to push)

# python
# calculator.py
# Multi-Function CLI Calculator
# Author: [Your Name]
# Description: A command-line calculator supporting multiple operations.

import math
import random
import time

# Main infinite loop to keep the program running
while True:

    # Display menu and get user choice
    def show_menu():
        print("\n--- Multi-Function Calculator ---\n")
        print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Power\n6. Square Root\n7. Factorial")
        print("8. Sine\n9. Cosine\n10. Tangent\n11. Random Number\n12. Exit\n")
        try:
            user_choice = int(input("Enter your choice: "))
            return user_choice
        except ValueError:
            print("\n❌ Invalid value. Choose one of the above options.\n")

    # Addition
    def add():
        try:
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The result of {num1} + {num2} is: {num1 + num2}"

    # Subtraction
    def subtract():
        try:
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The result of {num1} - {num2} is: {num1 - num2}"

    # Multiplication
    def multiply():
        try:
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The result of {num1} * {num2} is: {num1 * num2}"

    # Division with zero check
    def divide():
        try:
            num1 = int(input("\nEnter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            try:
                result = num1 / num2
            except ZeroDivisionError:
                print("\n❌ Cannot divide by zero.\n")
                return None
            else:
                return f"\n✅ The result of {num1} / {num2} is: {result}"

    # Exponentiation
    def power():
        try:
            num1 = int(input("\nEnter base number: "))
            num2 = int(input("Enter exponent: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The result of {num1} raised to the power of {num2} is: {math.pow(num1, num2)}"

    # Square root
    def square_root():
        try:
            num = int(input("\nEnter a number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The square root of {num} is: {math.sqrt(num)}"

    # Factorial
    def factorial():
        try:
            num = int(input("\nEnter a number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The factorial of {num} is: {math.factorial(num)}"

    # Sine
    def sin():
        try:
            num = int(input("\nEnter an angle in radians: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The sine of {num} is: {math.sin(num)}"

    # Cosine
    def cos():
        try:
            num = int(input("\nEnter an angle in radians: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The cosine of {num} is: {math.cos(num)}"

    # Tangent
    def tan():
        try:
            num = int(input("\nEnter an angle in radians: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The tangent of {num} is: {math.tan(num)}"

    # Random number generation
    def random_num_gen():
        try:
            start = int(input("\nEnter the starting number: "))
            end = int(input("Enter the ending number: "))
        except ValueError:
            print("\n❌ Invalid input. Enter a number.\n")
            return None
        else:
            return f"\n✅ The random number between {start} and {end} is: {random.randint(start, end)}"
    
    # Helper to Reduce Repetition
    def process_operation(operation_func):
        ans = operation_func()
        if ans:
            print("\nCalculating...")
            time.sleep(1.5)
            print(ans)


    # Main execution control
    choice = show_menu()

    if choice is None:
        continue
    elif choice == 1:
        process_operation(add)
    elif choice == 2:
        process_operation(subtract)
    elif choice == 3:
        process_operation(multiply)
    elif choice == 4:
        process_operation(divide)
    elif choice == 5:
        process_operation(power)
    elif choice == 6:
        process_operation(square_root)
    elif choice == 7:
        process_operation(factorial)
    elif choice == 8:
        process_operation(sin)
    elif choice == 9:
        process_operation(cos)
    elif choice == 10:
        process_operation(tan)
    elif choice == 11:
        process_operation(random_num_gen)
    elif choice == 12:
        print("\n👋 Good Bye!\n")
        break
    else:
        print("\n❌ Invalid input. Please select a valid option.\n")
        continue
