# 🧩 Quiz Game (Pakistan Edition)
# ---------------------------------
# Concepts Used:
# ✅ Dictionaries for questions and answers
# ✅ Loops and input validation
# ✅ Score tracking
# ---------------------------------

print("🧩 Welcome to the Pakistan Quiz Game!")
print("-" * 40)

while True:
    questions = {
        1: "What is the national language of Pakistan?",
        2: "What is the traditional dress for men in Pakistan?",
        3: "What is the festival marking the end of Ramadan?",
        4: "What is the staple food of Pakistan?",
        5: "Which city is known as the cultural hub of Pakistan?"
    }

    choices = {
        1: "A) Urdu\nB) English\nC) Punjabi\nD) Sindhi",
        2: "A) Kurta and Shalwar\nB) Suit\nC) Jeans and T-shirt\nD) Suit and Tie",
        3: "A) Eid-ul-Fitr\nB) Eid-ul-Adha\nC) Diwali\nD) Holi",
        4: "A) Rice\nB) Bread (Roti)\nC) Biryani\nD) All of the above",
        5: "A) Lahore\nB) Karachi\nC) Islamabad\nD) Peshawar"
    }

    correct_choices = {1: "a", 2: "a", 3: "a", 4: "a", 5: "a"}
    score = 0

    for q_num, question in questions.items():
        print(f"\n{q_num}. {question}")
        print(choices[q_num])
        answer = input("👉 Enter your choice (A/B/C/D): ").strip().lower()

        if answer == correct_choices[q_num]:
            print("✅ Correct Answer!\n")
            score += 2
        elif answer in ["b", "c", "d"]:
            print(f"❌ Wrong Answer! Correct was: {correct_choices[q_num].upper()}\n")
        else:
            print("⚠️ Invalid choice.\n")

    print(f"🏁 Your total score: {score} / 10")

    if score == 10:
        print("🏆 Excellent! Full marks!")
    elif score >= 6:
        print("✅ Good job!")
    else:
        print("❌ Better luck next time!")

    play_again = input("🔁 Play again? (Yes/No): ").strip().lower()
    if play_again != "yes":
        print("👋 Goodbye! Thanks for playing!")
        break
