# import random
# def ask_guess():
#     guess = input("what is your guess for the code")
#
# def generate_three_code():

# class Circle():
#
#     def __init__ (self,breed,name):
#         self.breed=breed
#         self.name= name
# x=Circle("local","jill")
# print(x.breed)
# print(x.name)

class Circle():

    pi = 3.142

    def __init__(self,radius=1):
        self.radius=radius

    def area(self):
        return Circle.pi * (self.radius ** 2)

    def circumfrence(self):
        return 2 * Circle.pi * self.radius

    def set_radius(self,new_radius):
        self.radius = new_radius

x = Circle(7)
x.set_radius(200)
print(x.area())
