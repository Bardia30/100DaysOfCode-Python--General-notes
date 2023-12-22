# class Point:
    
#     default_color = 'red' #class level attribute (less used)
    
#     #constructor function
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     #decorator for class method
#     @classmethod 
#     def zero(cls):
#         return cls(0,0) #exactly like Point(0,0)

#     def draw(self):
#         print(f"draw ({self.x}, {self.y})")

#     def __str__(self):
#         return f"({self.x}, {self.y})"
    
#     def __eq__(self, other):
#         #returns true if another objects x and y values are equal to another object
#         return self.x == other.x and self.y == self.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y
    
#     #to add to objects together
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)


# point = Point(1, 2)
# # print(type(point))
# #print(point.x)

# point.z = 30
# # print(isinstance(point, Point))
# #instance level attribute
# #x, y, z are attributes of the instance point (1,2,3)

# # point.draw()
# # print(isinstance(point, int))

# # print(point.z)

# # print(point.default_color)
# # print(Point.default_color)

# #instance methods. Need an object to call them 
# #class level. defined in class level (factory method, creates new method)


# origin = Point.zero()

# # origin.draw()

# # print(origin)


# point = Point(1,2)
# other = Point(3, 4)
# combined = point + other
# combined.draw()


class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1
        
    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)
    
    def __iter__(self):
        return iter(self.tags)

cloud = TagCloud()
cloud.add('Python')
cloud.add('python')
cloud.add('python')

# print(cloud['python'])
# print(cloud.tags)


class Product:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than 0")
        self.__price = value

    price = property(get_price, set_price)

product = Product(10)


#better way
class Product_better:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than 0")
        self.__price = value



#inheritence

# class Animal:
#     def __init__(self):
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         #method overriding (extending the super class)
#         super().__init__() 
#         self.weight = 25


#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#        print("swim")


# mammal = Mammal()
# print(mammal.weight)


# class Animal:
#     def eat(self):
#         print("eat")

# class Bird(Animal):
#     def fly(self):
#         print("fly")

# #chicken can't fly, so this is not logically right. Inheritance abuse
# #note: avoid multi-level inheritance
# class Chicken(Bird):
#     #to make python not do anything 
#     pass 

#good example of inheritance

#To make a class abstract base class (Not to be made for object instanciation)
# from abc import ABC, abstractmethod


# #custom exception
# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False
    
    
#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already opened")
#         self.opened = True
#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already closed")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass

# class FileStream(Stream):
#     def read(self):
#         print("reading data from a file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Reading data from a network")





#POLYMORPHISM
# from abc import ABC, abstractmethod


# class UIControl(ABC):
#     @abstractmethod
#     def draw(self):
#         pass


# class TextBox:
#     def draw(self):
#         print("text box")

# class DropDownList:
#     def draw(self):
#         print("Dropdown list")


# def draw(controls):
#     for control in controls:
#         control.draw()

# ddl = DropDownList()
# # print(isinstance(ddl, UIControl))
# textbox = TextBox()

# draw([ddl, textbox])
# #why polymorphism? because draw method has taken many shapes


# extending types
# class Text(str):
#     def duplicate(self):
#         return self + self
    
# class TrackableList(list):
#     #extending the existing append method
#     #it just does the print in addition to what .append() does
#     def append(self, object):
#         print("append called")
#         super().append(object)

# text = Text("Python")

# print(text.duplicate())




