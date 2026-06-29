# class variable = shared among all instance of a class
#                  defined outside the construture
#                  allow you to share data among all objects created from the class

class Student:

    class_year = 2026                # Class Variable
    num_student = 0                  # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_student += 1

student1 = Student("Raghav", 22)
student2 = Student("Jhanvi", 22)
student3 = Student("Sahaj", 29)
student4 = Student("Ananya", 28)

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)