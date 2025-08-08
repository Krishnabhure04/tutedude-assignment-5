# Task 1: Create a Dictionary of Student Marks

def get_student_marks():
    # Dictionary of student names and their marks
    student_marks = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "David": 88,
        "Eva": 95
    }

    # Get student name input
    student_name = input("Enter the student's name: ")

    # Check if student exists and display marks
    if student_name in student_marks:
        print(f"{student_name}'s marks: {student_marks[student_name]}")
    else:
        print(f"Student '{student_name}' not found in the records.")

if __name__ == "__main__":
    get_student_marks()
