# Dictionary to store student data
students = {
    "S101": {"name": "Sung Ji-Woon", "age": 20, "grades": [85.5, 90.0, 78.0]},
    "S102": {"name": "Taylor Swift", "age": 22, "grades": [92.5, 88.0, 95.0]},
    "S103": {"name": "Paresh Rawal", "age": 19, "grades": [76.0, 82.5, 88.0]},
    "S104": {"name": "Shahrukh Khan", "age": 21, "grades": [89.5, 91.0, 87.5]},
    "S105": {"name": "Dwayne Johnson", "age": 23, "grades": [78.0, 80.5, 85.5]}
}



def create_student(student_id, name, age, grades):
    # Add a new student.
    if student_id in students:
        print("Student ID already exists!")
    else:
        students[student_id] = {"name": name, "age": age, "grades": grades}
        print("Student added successfully.")

def read_student(student_id):
    # Read student data.
    if student_id in students:
        student = students[student_id]
        print(f"ID: {student_id}, Name: {student['name']}, Age: {student['age']}, Grades: {student['grades']}")
    else:
        print("Student not found.")

def update_student(student_id, name=None, age=None, grades=None):
    # Update student data.
    if student_id in students:
        if name:
            students[student_id]["name"] = name
        if age:
            students[student_id]["age"] = age
        if grades:
            students[student_id]["grades"] = grades
        print("Student updated successfully.")
    else:
        print("Student not found.")

def delete_student(student_id):
    # Delete a student.
    if student_id in students:
        del students[student_id]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

# Menu for CRUD operations
while True:
    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. View All Students")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        student_id = input("Enter student ID: ")
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        grades = list(map(float, input("Enter grades (separated by spaces): ").split()))
        create_student(student_id, name, age, grades)
    elif choice == "2":
        student_id = input("Enter student ID: ")
        read_student(student_id)
    elif choice == "3":
        student_id = input("Enter student ID: ")
        name = input("Enter new name (or press Enter to skip): ")
        age = input("Enter new age (or press Enter to skip): ")
        grades = input("Enter new grades (separated by spaces, or press Enter to skip): ")
        age = int(age) if age else None
        grades = list(map(float, grades.split())) if grades else None
        update_student(student_id, name, age, grades)
    elif choice == "4":
        student_id = input("Enter student ID: ")
        delete_student(student_id)
    elif choice == "5":
        if students:
            for student_id, info in students.items():
                print(f"ID: {student_id}, Name: {info['name']}, Age: {info['age']}, Grades: {info['grades']}")
        else:
            print("No students found.")
    elif choice == "6":
        print("Exiting program.")
        break
    else:
        print("Invalid choice. Please try again.")
