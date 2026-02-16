# 🎯 Number Guessing Game
# -------------------------------
# Concepts Used:
# ✅ random.randint() for random number generation
# ✅ while loop for continuous guessing
# ✅ conditionals for hints and validation
# -------------------------------

import random

print("🎮 Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10...")
print("-" * 40)

# Generate random number between 1–10
num = random.randint(1, 10)
attempts = 0

while True:
    try:
        guessing_num = int(input("👉 Enter your guess: "))
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    attempts += 1

    if guessing_num == num:
        print("🎉 Correct! You guessed the right number!")
        break
    elif guessing_num > num:
        print("⬆️ Too high! Try again.")
    else:
        print("⬇️ Too low! Try again.")

print("-" * 40)
print(f"🏁 You took {attempts} attempts to guess the number.")
print("Thanks for playing! 👋")
