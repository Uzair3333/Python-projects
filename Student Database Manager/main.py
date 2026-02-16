# 🎓 Student Database Manager
# -----------------------------------------------------
# A simple CLI-based student management system.
# Features:
# ✅ Add new students
# ✅ View all records
# ✅ Find top scorer(s)
# ✅ Search students by subject
# ✅ Remove a student record
# ✅ Exit program gracefully
# -----------------------------------------------------
# Author: Uzair (GitHub: @Uzair3333)
# -----------------------------------------------------

import time

# 🧾 Initial sample student records
students = [
    {"name": "Uzair", "age": 18, "subject": "CS", "score": 90},
    {"name": "Abdullah", "age": 23, "subject": "Physics", "score": 95}
]

# 🚀 Main Program Loop
while True:
    print("\n🎓 STUDENT DATABASE MANAGER")
    print("-" * 40)
    print("1️⃣  Add New Student")
    print("2️⃣  View All Students")
    print("3️⃣  Find Top Scorer")
    print("4️⃣  Search by Subject")
    print("5️⃣  Remove a Student")
    print("6️⃣  Exit Program")
    print("-" * 40)

    user_choice = input("👉 Enter your choice: ").strip()

    # 1️⃣ Add new student
    if user_choice == "1":
        print("\n🆕 Add New Student Record")
        name = input("Enter name: ").strip()
        try:
            age = int(input("Enter age: "))
            subject = input("Enter subject: ").strip()
            score = int(input("Enter score (0-100): "))
        except ValueError:
            print("❌ Invalid input. Please enter numbers where required.")
            continue

        new_student = {"name": name, "age": age, "subject": subject, "score": score}
        students.append(new_student)
        print(f"✅ {name} added successfully!")

    # 2️⃣ View all students
    elif user_choice == "2":
        print("\n📋 Student Records:")
        print("-" * 40)
        if not students:
            print("⚠️ No records found.")
        else:
            for student in students:
                print(f"👤 {student['name']:<10} | Age: {student['age']:<2} | "
                      f"Subject: {student['subject']:<10} | Score: {student['score']}")
        print("-" * 40)

    # 3️⃣ Find top scorer
    elif user_choice == "3":
        if not students:
            print("⚠️ No student records available.")
        else:
            top_score = max(student["score"] for student in students)
            print("\n🏆 Top Scorer(s):")
            for student in students:
                if student["score"] == top_score:
                    print(f"⭐ {student['name']} — {top_score} points")

    # 4️⃣ Search by subject
    elif user_choice == "4":
        subject_input = input("Enter subject to search: ").strip().casefold()
        found_students = [s for s in students if s["subject"].casefold() == subject_input]
        print("\n🔍 Search Results:")
        if found_students:
            for student in found_students:
                print(f"📘 {student['name']} studies {student['subject']}")
        else:
            print("❌ No student found with that subject.")

    # 5️⃣ Remove a student
    elif user_choice == "5":
        student_to_remove = input("Enter the name of the student to remove: ").strip().casefold()
        for student in students:
            if student["name"].casefold() == student_to_remove:
                students.remove(student)
                print(f"🗑️ {student['name']} removed successfully.")
                break
        else:
            print("❌ Student not found.")

    # 6️⃣ Exit
    elif user_choice == "6":
        print("\n👋 Exiting Student Database Manager...")
        time.sleep(1)
        print("✅ All changes saved successfully (in memory).")
        print("Good Bye!\n")
        break

    # Invalid choice
    else:
        print("⚠️ Invalid choice. Please select a valid option from the menu.")
