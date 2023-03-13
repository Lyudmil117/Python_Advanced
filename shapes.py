from abc import ABC, abstractmethod
from math import pi

class  Shape:
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        return pi * self.__radius ** 2

    def calculate_perimeter(self):
        return pi * self.__radius * 2

class Rectangle(Shape):
    def __init__(self, width, length):
        self.__width = width
        self.__length = length

    def calculate_area(self):
        return self.__length * self.__width

    def calculate_perimeter(self):
        return 2 * (self.__width + self.__length)

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())