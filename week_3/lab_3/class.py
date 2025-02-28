from math import sqrt

class Str:
    string = ''
    def get_string():
        global string
        string = input("write a string")
    
    def print_string():
        print(string)

class Shape:
    length = 0
    width = 0

    def area(self):
        print(self.length * self.width)
    

class Square(Shape):

    def __init__(self, length):
        self.length = length
        self.width = length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
#A point class is a class that creates a certain point with x, y coordinates and ability to move.
class Point:
    def __init__(self, x_init, y_init):
        self.x = x_init
        self.y = y_init
    
    def show(self):
        print(f"{self.x}, {self.y}")
    
    def move(self, x_move = 0, y_move= 0):
        self.x = x_move
        self.y = y_move

    def dist(a, b):
        return sqrt((a.x-b.x)**2+(a.y-b.y)**2)
    

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, d_amount):
        self.balance =+ d_amount

    def withdrawal(self, w_amount):
        if(w_amount <= self.balance):
            self.balance =- w_amount
        else:
            print("Not correct withdrawal")
    

        


