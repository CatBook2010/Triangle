from triangle import Triangle

correct_sides = False
while not correct_sides:
    side_1 = float(input("Enter side1: "))
    side_2 = float(input("Enter side2: "))
    side_3 = float(input("Enter side3: "))

    correct_sides = side_1 + side_2 > side_3 and side_2 + side_3 > side_1 and side_1 + side_3 > side_2

    if not correct_sides:
        print("Please, enter correct sides.")

color = input("Enter color: ")
filled = bool(int(input("Enter 1/0 for filled (1: true, 0: false): ")))

new_triangle = Triangle(color, filled, side_1, side_2, side_3)

print(f"The perimeter is {new_triangle.getPerimeter()}")
print(f"Color is {color}") 
print(f"Filled is {filled}")