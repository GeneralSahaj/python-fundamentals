# multiple inheritance = inherit from more then one parent class
#                         C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent
#                          C(B) <- B(A) <- A

class Animal():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


# Inherits from Animal
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


# Inherits from Animal
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


# Multilevel Inheritance: Rabbit -> Prey -> Animal
class Rabbit(Prey):
    pass


# Multilevel Inheritance: Hawk -> Predator -> Animal
class Hawk(Predator):
    pass


# Multiple Inheritance: Fish -> Prey + Predator
class Fish(Prey, Predator):
    pass


# Animal.__init__() is inherited and used automatically
rabbit = Rabbit("Bunny")
hawk = Hawk("Hawks")
fish = Fish("Fishy")


# Python finds flee() in Prey and executes it
fish.flee()