# class method = Allow operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself.

# Instance Method = Best for operations on instances of the class (Objects)
# Static Method = Best for utility functions that do not need access to class data
# Class Method = Best for class-level data or require access to the class itself

class Student:

    count = 0
    total_class_score = 0

    def __init__(self, name, score):
        self.name = name
        self.score = score
        Student.count += 1
        Student.total_class_score += score


    #Instance Method
    def get_info(self):
        return f"{self.name} scored {self.score}"
    
    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"
    
    @classmethod
    def get_class_average_score(cls):
        if cls.count == 0:
            return 0 
        else:
            return f"Your class average is {cls.total_class_score / cls.count}"
        
student1 = Student("Iski lee", 75)
student2 = Student("Uski lee", 85)
student3 = Student("Sabki lee", 95)

print(Student.get_count())
print(Student.get_class_average_score())
