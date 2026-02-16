# ✊ Rock, Paper, Scissors Game
# ---------------------------------
# Concepts Used:
# ✅ random.choice() for computer selection
# ✅ Conditional logic for winner detection
# ✅ Loops for replay functionality
# ---------------------------------

import random

print("🎮 Welcome to Rock, Paper, Scissors!")
print("-" * 40)

while True:
    print("\n1️⃣  Rock\n2️⃣  Paper\n3️⃣  Scissor")
    user_input = input("👉 Enter your choice (1-3): ")

    if user_input not in ["1", "2", "3"]:
        print("❌ Invalid choice. Please enter 1–3.")
        continue

    choices = { "1": "Rock", "2": "Paper", "3": "Scissor" }
    user_choice = choices[user_input]
    computer_choice = choices[str(random.randint(1, 3))]

    print(f"\n🧍 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 It's a Tie!")
    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):
        print("🏆 You Win!")
    else:
        print("😢 You Lose!")

    play_again = input("\n🔁 Play again? (Yes/No): ").strip().lower()
    if play_again != "yes":
        print("👋 Goodbye! Thanks for playing!")
        break
