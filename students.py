import json
import re

STUDENT_FILE="data/students.json"
COURSES= ["BCA","MCA","B.TECH","M.TECH"]

def load_students():
    with open(STUDENT_FILE,"r") as f:
        return json.load(f)

def save_students(students):
    with open(STUDENT_FILE,"w") as f:
        json.dump(students,f,indent=4)

def register_student():
    while True:
        name=input("Enter Student name:")
        if len(name)>=2 and re.match(r"^[A-Za-z ]+$", name):
            break
        else:
            print("The name should have atleaast 2 leters and only alphabets")
    print("NAME:", name)
    while True:
        regno=input("Register no:")
        if re.match(r"^REG-\d{4}-\d{4}$",regno, re.IGNORECASE):
            break
        else:
            print("Invalid register number")
    print("Regno:",regno)
    while True:
        age_input=input("Age:")
        if age_input.isdigit():
            age=int(age_input)
            if age>=18 and age<=25:
                break
            else:
                print("Age must be in between 18 and 25")
        else:
            print("Invalid input for age:")
    print("Age:",age)
    while True:
        email=input("Email:")
        if re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email):
            break
        else:
            print("Invalid email")
        
    print("Email:",email)

    while True:
        phoneno=input("Enter the phone number")
        if phoneno.isdigit() and len(phoneno)==10:
            break
        else:
            print("Invalid phone number")
    print("Phone no:",phoneno)
    
    print("Available Courses:", ", ".join(COURSES))
    while True:
        course = input("Enter course: ").strip().upper()
        if course in COURSES:
            break
        else:
            print("Invalid course. Please choose from the available list.")


    student={
        "Name": name,
        "Regno":regno,
        "Age": age,
        "Email": email,
        "Phoneno":phoneno,
        "Courses":course
    }
    students=load_students()
    students.append(student)
    save_students(students)
    print("Student saved successfully")

def list_students():
    students = load_students()
    if not students:
        print("No students registered yet.")
        return

    print("\n--- Registered Students ---")
    for idx, student in enumerate(students, start=1):
        print(f"\nStudent {idx}:")
        print(f"  Name     : {student['Name']}")
        print(f"  Reg No   : {student['Regno']}")
        print(f"  Age      : {student['Age']}")
        print(f"  Email    : {student['Email']}")
        print(f"  Phone    : {student['Phoneno']}")
        print(f"  Course   : {student['Courses']}")
