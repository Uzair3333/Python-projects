# 🎯 Project: Student Performance Analyzer (Functional Programming Edition)
# ---------------------------------------------------------------
# Concepts Used:
# ✅ map() → add grades to students
# ✅ filter() → filter out passed students
# ✅ reduce() → calculate average marks
# ✅ sorted() → rank students by marks
# ---------------------------------------------------------------

from functools import reduce

# 🎓 List of Students (sample dataset)
students = [
    {"name": "Aziz", "marks": 78},
    {"name": "Habib", "marks": 56},
    {"name": "Alice", "marks": 91},
    {"name": "Bob", "marks": 42},
    {"name": "Devil", "marks": 65}
]

# 🧩 Step 1: Determine Grade
def determine_grade(marks):
    """Return grade based on marks."""
    if marks >= 80:
        return "A"
    elif 60 <= marks <= 79:
        return "B"
    else:
        return "C"

# 🧩 Step 2: Add Grades to Each Student using map()
students_with_grades = list(
    map(lambda s: {**s, "grade": determine_grade(s['marks'])}, students)
)

# 🧩 Step 3: Filter Passed Students (marks >= 50)
def has_passed(marks):
    """Return True if student has passed."""
    return marks >= 50

passed_students = list(
    filter(lambda s: has_passed(s['marks']), students_with_grades)
)

# 🧩 Step 4: Calculate Average Marks using reduce()
marks = [s['marks'] for s in students]
average_marks = reduce(lambda x, y: x + y, marks) / len(marks)

# 🧩 Step 5: Sort Students by Marks (Descending)
sorted_students = sorted(students_with_grades, key=lambda s: s['marks'], reverse=True)


# ---------------------------------------------------------------
# 🖨️ Display Output Nicely
# ---------------------------------------------------------------

print("\n🎓 Student Performance Report")
print("-" * 40)
for s in sorted_students:
    status = "✅ Passed" if int(s['marks']) >= 50 else "❌ Failed"
    print(f"{s['name']:<10} | Marks: {s['marks']:<3} | Grade: {s['grade']} | {status}")

print("-" * 40)
print(f"📊 Class Average Marks: {average_marks:.2f}")
print(f"🏆 Top Performer: {sorted_students[0]['name']} ({sorted_students[0]['marks']} marks)")
print(f"📘 Total Passed Students: {len(passed_students)}/{len(students)}")
print("-" * 40)
