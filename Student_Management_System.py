import json

try:
    with open("students.json", "r") as file:
        students = json.load(file)
except FileNotFoundError:
    students = {}

def add_new_student():
    try:
        roll_no =int(input("\nEnter roll number: "))
        if roll_no in students:
            raise ValueError("\nError: Roll number already exists!")
    except ValueError as ve:
        print("\nError: Roll number must have only numbers!")
        return

    name = input("\nEnter name: ")

    if not name.isalpha():
        print("\nError: Name must have only alphabets")
        return 

    age = input("\nEnter age: ")
    
    if not age.isdigit() or int(age) <= 0:
        print("\nError: Age must be a positive number!")
        return

    student_class = input("\nEnter class: ")
    subjects = {}

    num_subjects = input("\nEnter number of subjects: ")
    if not num_subjects.isdigit() or int(num_subjects) <= 0:
        print("\nError: Number of subjects should be at least 1!")
        return

    for i in range(int(num_subjects)):
        subject = input(f"\nSubject {i+1} name: ")
        marks = input(f"\nSubject {i+1} marks: ")
        if not marks.isdigit() or int(marks) < 0 or int(marks) > 100:
            print("\nError: Marks should be between 0 and 100!")
            return
        subjects[subject] = int(marks)

    students[roll_no] = {"name": name, "age": int(age), "class": student_class, "subjects": subjects}
    print("\nStudent added successfully!")

def view_all_students():
    if students:
        for roll_no, info in students.items():
            print(f"\nRoll No: {roll_no}, Name: {info['name']}, Age: {info['age']}, Class: {info['class']}, Subjects: {info['subjects']}")
    else:
        print("\nNo students found!")

def search_student():
    roll_no = input("\nEnter roll number to search: ")
    if roll_no in students:
        print(students[roll_no])
    else:
        print(f"\nStudent of Roll No.{roll_no} not found!")

def update_student_information():
    roll_no = input("\nEnter roll number to update: ")
    if roll_no in students:
        name = input("\nEnter new name: ")
        age = input("\nEnter new age: ")
        student_class = input("\nEnter new class: ")

        if name.isalpha():
            students[roll_no]["name"] = name
        if age.isdigit() and int(age) > 0:
            students[roll_no]["age"] = int(age)
        elif age:
            print("Error: Age must be a positive number!")
            return

        if student_class:
            students[roll_no]["class"] = student_class

        print("\nStudent updated successfully!")
    else:
        print(f"\nStudent of Roll No.{roll_no} not found!")

def delete_student_information():
    roll_no = input("\nEnter roll number to delete: ")
    if roll_no in students:
        del students[roll_no]
        print("\nStudent deleted successfully!")
    else:
        print(f"\nStudent of Roll No.{roll_no} not found!")

def save_data():
    with open("students.json", "w") as file:
        json.dump(students, file, indent = 4)
    print("\nData saved successfully!")

while True:
    choices={
        1: "Add Student",
        2: "View All Students",
        3: "Search Student by Roll Number",
        4: "Update Student",
        5: "Delete Student",
        6: "Exit"
        }

    print("\n   *** Welcome to Student Management System ***    \n")
    for key, value in choices.items():
        print((f"{key}. {value}"))
    
    choice = input("\nEnter your choice: ")
    
    if choice == "1":
        add_new_student()
    elif choice == "2":
        print("\n   *** Students List ***   ")
        view_all_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student_information()
    elif choice == "5":
        delete_student_information()
    elif choice == "6":
        save_data() 
        break
    else:
        print("\nInvalid choice, please enter a number between 1 and 6!")