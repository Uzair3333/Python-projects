# 🎓 Project: Student Grade Calculator
# 🧩 Concepts Used: Classes, Loops, Conditionals, Functions, Exception Handling, Encapsulation

class GradeCalculator:
    """A class to calculate total, average, and grade for a student's subjects."""

    def __init__(self):
        """Initialize the calculator by asking how many subjects the student has."""
        print("🎓 Welcome to the Student Grade Calculator 🎓")
        while True:
            try:
                self.num_of_subjects = int(input("\nEnter the number of subjects: "))
                if self.num_of_subjects <= 0:
                    print("⚠️ Please enter a positive number.")
                    continue
                break
            except ValueError:
                print("❌ Invalid input. Please enter a valid number.")
        self.marks_of_subjects = []

    def get_marks(self):
        """Collect marks for each subject from the user."""
        print("\n📘 Enter your marks (0–100):")
        for i in range(1, self.num_of_subjects + 1):
            while True:
                try:
                    mark = int(input(f"  ➤ Subject #{i}: "))
                    if 0 <= mark <= 100:
                        self.marks_of_subjects.append(mark)
                        break
                    else:
                        print("⚠️ Marks should be between 0 and 100.")
                except ValueError:
                    print("❌ Please enter a valid number.")
        print("\n✅ Marks recorded successfully!\n")

    def calculate_total(self):
        """Calculate total marks obtained."""
        self.total = sum(self.marks_of_subjects)
        return self.total

    def calculate_average(self):
        """Calculate and return average marks."""
        self.average = self.total / len(self.marks_of_subjects)
        return self.average

    def determine_grade(self):
        """Determine grade based on the average marks."""
        avg = self.average  # keep numeric for logic
        if 90 <= avg <= 100:
            self.grade = "A"
            self.remark = "🌟 Excellent Performance!"
        elif 80 <= avg < 90:
            self.grade = "B"
            self.remark = "💪 Very Good! Keep it up."
        elif 70 <= avg < 80:
            self.grade = "C"
            self.remark = "👍 Good Work!"
        elif 60 <= avg < 70:
            self.grade = "D"
            self.remark = "🙂 Needs a bit more effort."
        else:
            self.grade = "F"
            self.remark = "❌ Failed. Work harder next time!"
        return self.grade

    def display_summary(self):
        """Display a clean formatted summary of results."""
        print("\n📊 ---- RESULT SUMMARY ---- 📊")
        print(f"📚 Total Subjects : {self.num_of_subjects}")
        print(f"🧾 Marks Entered  : {self.marks_of_subjects}")
        print(f"🔢 Total Marks    : {self.total}")
        print(f"📈 Average Marks  : {self.average:.2f}%")
        print(f"🏅 Grade Awarded  : {self.grade}")
        print(f"💬 Remark         : {self.remark}")
        print("-----------------------------")
        print("🎉 Congratulations on completing your exam analysis!\n")

    def run(self):
        """Main driver function that runs all steps in sequence."""
        self.get_marks()
        self.calculate_total()
        self.calculate_average()
        self.determine_grade()
        self.display_summary()


# 🧠 Main Execution
if __name__ == "__main__":
    student = GradeCalculator()
    student.run()
