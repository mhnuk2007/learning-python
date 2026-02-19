# main.py
# Import your custom module and package

import math_tools  # custom module
from shapes import circle_area, circle_circumference, rect_area, rect_perimeter  # package imports

# Using functions from the module
print("Module Examples:")
print("Add 5 + 3:", math_tools.add(5, 3))
print("Divide 10 / 2:", math_tools.divide(10, 2))

# Using functions from the package
print("\nPackage Examples:")
print("Circle area (radius 3):", circle_area(3))
print("Circle circumference (radius 3):", circle_circumference(3))
print("Rectangle area (5x7):", rect_area(5, 7))
print("Rectangle perimeter (5x7):", rect_perimeter(5, 7))