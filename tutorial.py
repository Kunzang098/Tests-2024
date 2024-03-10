# Initialize empty lists and dictionary
students_list = []
students_dict = {}

def add_student():
    name = input("Enter student's name: ")
    age = input("Enter student's age: ")
    grade = input("Enter student's grade: ")

    # Add to list
    students_list.append(name)
    # Add to dictionary
    students_dict[name] = {'age': age, 'grade': grade}

    print("Student added successfully!")

def view_students():
    print("\nStudent Details:")
    for name, info in students_dict.items():
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")

def search_student():
    name = input("Enter student's name to search: ")
    if name in students_dict:
        info = students_dict[name]
        print(f"Name: {name}, Age: {info['age']}, Grade: {info['grade']}")
    else:
        print("Student not found.")

def remove_student():
    name = input("Enter student's name to remove: ")
    if name in students_list:
        students_list.remove(name)
        del students_dict[name]
        print("Student removed successfully!")
    else:
        print("Student not found.")

def main():
    while True:
        print("\nStudent Information Management System")
        print("1. Add a Student")
        print("2. View all Students")
        print("3. Search for a Student")
        print("4. Remove a Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            remove_student()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()