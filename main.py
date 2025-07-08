from auth import login
from students import register_student
from students import list_students
def main():
    print("====School Management System====")
    if not login():
        return
    while True:
        print("\n Menu:\n 1.Register Student\n 2.List Students\n 3.Exit")
        choice=input()
        if choice=="1":
            register_student()
        elif choice=="2":
            list_students()
        elif choice=="3":
            print("Exiting the program")
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()