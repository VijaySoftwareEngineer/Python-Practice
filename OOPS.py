# self: is reference of object

# OOPS in python 

# create class

# class Student:
#     def __init__(self, name):
#         self.name = name
#         print("Adding new student in database: ")

#     def Welcome(self):
#         print("Welcome student: ", self.name)

# s1 = Student("Vijay")
# s1.Welcome()


# Q on OOPS
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("hello")

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("Hi", self.name, "your avg score is: ", sum/3)
# object of class
# s1 = Student("Vijay", [99,98,97])
# s1.get_avg()

# # s1.name = "Ajay"
# # s1.get_avg()
# s1.hello()

# Abstraction: Hide unnecessary data and show essential data only.
# example
# class Car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def Start(self):
#         self.clutch = True
#         self.acc = True
#         print("Car started..")

# car1 = Car()
# car1.Start()

# Encapculation: ek object ke andar uss se related data bhi hai or function bhi hai usse encapculation khate hai.

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc

#     def Debit(self, amount):
#         self.balance -= amount
#         print("Rs", amount, "was debited")
#         print("Total balance = ", self.get_balance())

#     def Credit(self, amount):
#         self.balance += amount
#         print("Rs", amount, "was credited")
#         print("Total balance = ", self.get_balance())

#     def get_balance(self):
#         return self.balance

# acc1 = Account(5000, 12345)
# # print(acc1.balance)
# # print(acc1.account_no)
# acc1.Debit(500)
# acc1.Credit(1500)

# Inheritance: ek class dusari class ki kuch property or method ko inherit kar leati hai.

# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def Sound(self):
#         pass

# class Dog(Animal):
#         def Sound(self):
#             print("Dog Bark")

# class Cat(Animal):
#         def Sound(self):
#             print("Cat meaow")

# dog = Dog("canine")
# dog.Sound()

# cat = Cat("Feline")
# cat.Sound()


# Polymorphism:refers to the ability to use a single interface for multiple data types or classes. 
# It allows objects of different classes to be treated as objects of a common superclass.

# class Bird:
#     def sound(self):
#         print("Bird chirps")

# class Dog:
#     def sound(self):
#         print("Dog barks")

# def make_sound(animal):
#     animal.sound()

# bird = Bird()
# dog = Dog()

# make_sound(bird)
# make_sound(dog)

# Q1 OOPS
# Sol:
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print("The data of person name:", self.name)
#         print("The age of person:", self.age)

# s1 = Person("Vijay", 22)

# Q2 OOPS
# Solution:
# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def set_name(self, new_name):
#         self.name = new_name

#     def set_breed(self, new_breed):
#         self.breed = new_breed

#     def get_name(self):
#         return self.name
    
#     def get_breed(self):
#         return self.breed
    
# # object of dog class
# dog1 = Dog("Tommy", "Pitbull")

# print("initial values")
# print("Dog:", dog1.get_name(), "Breed:", dog1.get_breed())
# # Updated value
# dog1.set_name("Jack")
# print("Updated value of dog:")
# print("Dog:", dog1.get_name(), "Breed:", dog1.get_breed())

# Q3 OOPS
# Solution:
# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width

#     def cal_area(self):
#         return self.height * self.width
    
#     def cal_perimeter(self):
#         return 2 * (self.height + self.width)
    
# rect = Rectangle(5, 10)

# print("Area of rectangle:", rect.cal_area())
# print("Perimeter of rectangle", rect.cal_perimeter())

# Q4 OOPS
# Solution:
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def get_radius(self):
#         return self.radius
    
#     def set_radius(self, radius):
#         self.radius = radius
    
#     def cal_area(self):
#         return 3.14 * self.radius * self.radius
    
#     def cal_circumference(self):
#         return 2 * 3.14 * self.radius

# if __name__ == "__main__":
#     # Creating an instance of Circle with radius 5
#     circle = Circle(5)
#     print("Radius of circle:", circle.get_radius())

#     area = circle.cal_area()
#     print("Area of circle:", area)

#     circumference = circle.cal_circumference()
#     print("Circumference of circle:", circumference)

#     # Setting radius to new value
#     circle.set_radius(7.5)
#     print("\nUpdated radius:", circle.get_radius()) 

#     area = circle.cal_area()
#     circumference = circle.cal_circumference()
#     print("\nUpdated values:")
#     print("Area of circle:", area)
#     print("Circumference of circle:", circumference)


# Q5 OOPS
# Solution:



