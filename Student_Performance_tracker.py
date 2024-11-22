#  Student tracker performance
class Student:

    def __init__(self, name):
        self.name = name
        self.scores = []  # List to store the student's scores

    def add_scores(self, scores):
        self.scores = scores  # Add or update scores for the student

    def calculate_average(self):
        """Calculate and return the average score."""
        return sum(self.scores) / len(self.scores) if self.scores else 0

    def is_passing(self):
        """Check if the student has passed all subjects (score >= 40)."""
        return all(score >= 40 for score in self.scores)


class PerformanceTracker:
    def __init__(self):
        self.students = {}  # Dictionary to store all Student objects

    def add_student(self, name, scores):
        """Add a new student or update scores if the student exists."""
        if name in self.students:
            print(f"Student {name} already exists. Updating scores.")
        else:
            print(f"Adding new student {name}.")
        student = Student(name)
        student.add_scores(scores)
        self.students[name] = student

    def get_student_result(self, name):
        """Retrieve and format the result of a specific student."""
        if name in self.students:
            student = self.students[name]
            average = student.calculate_average()
            status = "Pass" if student.is_passing() else "Fail"
            return f"Name: {name}, Average: {average:.2f}, Status: {status}"
        else:
            return f"Student {name} not found."

    def display_all_students(self):
        """Display performance of all students."""
        if not self.students:
            print("No students have been added yet.")
        else:
            print("\nAll Students' Performance:")
            print("-" * 40)
            for student in self.students.values():
                print(self.get_student_result(student.name))
            print("-" * 40)


def main():
    tracker = PerformanceTracker()

    # Add students to the tracker
    print("Add Students (Enter 'done' as name to finish):")
    while True:
        name = input("Enter the student's name: ").strip()
        if name.lower() == "done":
            break
        try:
            scores = [
                int(input("Enter Math score: ")),
                int(input("Enter Science score: ")),
                int(input("Enter English score: ")),
                int(input("Enter Urdu score: ")),
                int(input("Enter Computer score: "))
            ]
            tracker.add_student(name, scores)
        except ValueError:
            print("Invalid input. Please enter numeric scores.")

    # Query a student's result
    while True:
        query = input("\nEnter a student's name to see their result (or 'exit' to stop): ").strip()
        if query.lower() == "exit":
            break
        print(tracker.get_student_result(query))

    # Display all student results
    tracker.display_all_students()


if __name__ == "__main__":
    main()
