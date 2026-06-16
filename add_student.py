'''
Project: Student Management System
Problem Statement

Create a Student Management System using Python and Object-Oriented Programming (OOP).

The system should allow the user to:

Add a new student.
View all students.
Search for a student using Student ID.
Update a student's marks.
Delete a student record.
Display the student with the highest marks.
Exit the application.
Student Details

Each student should have:

Student ID
Student Name
Age
Marks
'''
# Student Management System using OOP

class Student:

    def __init__(self, student_id, name, age, marks):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("\nStudent ID :", self.student_id)
        print("Name       :", self.name)
        print("Age        :", self.age)
        print("Marks      :", self.marks)


class StudentManagementSystem:

    def __init__(self):
        self.students = []
        

   # Add Multiple Students
    def add_student(self):

        n = int(input("How many students do you want to add? : "))

        for i in range(n):

            print(f"\nEnter Details of Student {i+1}")

            while True:
                student_id = int(input("Enter Student ID : "))

            # Check duplicate ID
                is_duplicate = False

                for student in self.students:
                    if student.student_id == student_id:
                        is_duplicate = True
                        break

                if is_duplicate:
                    print("Student ID already exists! Enter a different ID.")
                else:
                    break

            name = input("Enter Student Name : ")
            age = int(input("Enter Age : "))
            marks = float(input("Enter Marks : "))

            student = Student(student_id, name, age, marks)

            self.students.append(student)

        print(f"\n{n} Students Added Successfully!")

    # View Students
    def view_students(self):

        if len(self.students) == 0:
            print("No Students Found!")

        else:
            print("\n----- Student Details -----")

            for student in self.students:
                student.display()

    # Search Student
    def search_student(self):

        student_id = int(input("Enter Student ID to Search : "))

        for student in self.students:

            if student.student_id == student_id:

                print("\nStudent Found!")
                student.display()
                return

        print("Student Not Found!")

    # Update Marks
    def update_marks(self):

        student_id = int(input("Enter Student ID : "))

        for student in self.students:

            if student.student_id == student_id:

                new_marks = float(input("Enter New Marks : "))
                student.marks = new_marks

                print("Marks Updated Successfully!")
                return

        print("Student Not Found!")

    # Delete Student
    def delete_student(self):

        student_id = int(input("Enter Student ID : "))

        for student in self.students:

            if student.student_id == student_id:

                self.students.remove(student)

                print("Student Deleted Successfully!")
                return

        print("Student Not Found!")

    # Display Topper
    def display_topper(self):

        if len(self.students) == 0:
            print("No Students Available!")

        else:

            topper = self.students[0]

            for student in self.students:

                if student.marks > topper.marks:
                    topper = student

            print("\n----- Topper Details -----")
            topper.display()


# Main Program

sms = StudentManagementSystem()

while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Marks")
    print("5. Delete Student")
    print("6. Display Topper")
    print("7. Exit")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        sms.add_student()

    elif choice == 2:
        sms.view_students()

    elif choice == 3:
        sms.search_student()

    elif choice == 4:
        sms.update_marks()

    elif choice == 5:
        sms.delete_student()

    elif choice == 6:
        sms.display_topper()

    elif choice == 7:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")