class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old.")

class Student(Person):
    def __init__(self, name, age, gender, student_id):
        super().__init__(name, age, gender)
        self.student_id = student_id
    
    def study(self):
        print(f"{self.name} is studying.")

class Teacher(Person):
    def __init__(self, name, age, gender, subject):
        super().__init__(name, age, gender)
        self.subject = subject
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")

# Creating objects
student1 = Student("Alice", 18, "Female", "S12345")
teacher1 = Teacher("Mr. Smith", 35, "Male", "Math")

# Using methods
student1.introduce()
student1.study()

teacher1.introduce()
teacher1.teach()
