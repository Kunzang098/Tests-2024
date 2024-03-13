#Initialize empty lists and dictionary to store students information
students_list= []
students_dict= {}

#Add student information
name= input("Enter student's name:")
age = int(input("Enter student's age:"))
grade = int(input("Enter student's grade:"))
students_list.append(name)
students_dict[name] = {"age":age, "grade":grade}
print("Student's information added successfully")
print(students_dict.items())

#Search for students by name
search_name =input("Enter the name of the student to search or simply enter to escape:")
if search_name in students_list:
    info=students_dict[search_name]
    print(f"Name:{search_name}, Age:{info['age']}, Grade:{info['grade']}")
else:
    print("Student not found")

#Remove student
remove_name=input("Enter the name of the student to be removed or simply enter to skip:")
if remove_name in students_list:
    del students_dict[remove_name]
    students_list.remove(remove_name)
    print("Student removed successfully")
else:
    print("Student not found!")    

