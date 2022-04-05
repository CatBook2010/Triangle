# (The Triangle class) Design a class named Triangle that extends the GeometricObject class. The Triangle class contains:

# Three float data fields named side1, side2, and side3 are used to denote the three sides of the triangle.

# A constructor creates a triangle with the specified side1, side2, and side3 with default values 1.0.

# The accessor methods for all three data fields

# A method named getArea() returns the area of this triangle.

# A method named getPerimeter() returns the perimeter of this triangle.

# A method named __str__() returns a string description for the triangle.


# The __str__() method is implemented as follows:
# return "Triangle: side1 = " + str(self.__side1) + 
#     " side2 = " +
#     str(self.__side2) + " side3 = " + str(self.__side3)


# The __str__() method is implemented as follows:


# return "Triangle: side1 = " + str(self.__side1) + 
#     " side2 = " +
#     str(self.__side2) + " side3 = " + str(self.__side3)

# Sample input:
# 2.5 
# 3.1  
# 2.8 
# red  
# 1

# Sample output:
# Enter side1: 2.5 
# Enter side2: 3.1  
# Enter side3: 2.8 
# Enter color: red  
# Enter 1/0 for filled (1: true, 0: false): 1
# The area is 3.3159613990515604
# The perimeter is 8.399999999999999
# Color is red  
# Filled is True

from geometric_object import GeometricObject

class Triangle(GeometricObject):
    def __init__(self, color, filled, side1 = 1.0, side2 = 1.0, side3 = 1.0):
        super().__init__()
        self.__side1 = side1
        self.__side2 = side2
        self.__side3 = side3

    def get_side1_len(self):
        return self.__side1

    def set_side1_len(self, side_len):
        self.__side1 = side_len

    def get_side2_len(self):
        return self.__side2

    def set_side2_len(self, side_len):
        self.__side2 = side_len

    def get_side3_len(self):
        return self.__side3

    def set_side3_len(self, side_len):
        self.__side3 = side_len

    def getPerimeter(self):
        return self.get_side1_len() + self.get_side2_len() + self.get_side3_len()

    def getArea(self):
        half_perimetr = self.getPerimeter() / 2
        return (half_perimetr * (half_perimetr - self.get_side1_len()) * (half_perimetr - self.get_side2_len()) * (half_perimetr - self.get_side3_len())) ** 0.5

    def __str__(self):
        return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)