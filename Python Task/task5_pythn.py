class Student:
    def __init__(self, name, age, grades):
        #Initialize a student with name, age, and grades.
        self.name = name 
        self.age = age 
        self.grades = grades  

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Grades: {self.grades}")

    def calculate_average(self):
        #Calculate and return the average of the grades.
        if self.grades:  # Check if the grades list is not empty
            return sum(self.grades) / len(self.grades)
        else:
            return 0.0


student1 = Student("Henry Cavil", 22, [85.5, 90.0, 78.0])
student1.display_details()
print("Average Grade:", student1.calculate_average())
