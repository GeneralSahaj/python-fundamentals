# objects = A "bundle" of related attributes (variables) and methods (function)
#           a phone, a car, book
#            you need a "class" to create many objects

# Class : (blueprints) used to design the structure and layout of an object

# Note : A method is an function that belongs within an object

from player import Player

player1 = Player("knight", 100)
player2 = Player("goblin", 50)

player1.attack(player2)
player2.attack(player1)