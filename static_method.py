# Static Method = A method that belong to a class rather then any object from the class (instance)
#                 usually used for general utility functions

# Instance Method = Best for operations on instances of the class (Objects)
# Static Method = Best for utility functions that do not need access to class data

class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name} is {self.position}"
    

    @staticmethod
    def is_valid_position(position):
        valid_positions = ["Manager", "Receptionist", "Butler", "Cleaner"]
        return position in valid_positions


employee1 = Employee("Sahaj", "Manager")
employee2 = Employee("Ananya", "Receptionist")

print(f"Is butler a valid position: {Employee.is_valid_position("Butler")}")
print(employee1.get_info())
print(employee2.get_info())
print(f"Is Dancer a valid position: {Employee.is_valid_position("Dancer")}")