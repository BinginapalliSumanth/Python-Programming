from package import mathfunctions
from package import areafunctions 
print("Addition:", mathfunctions.add(10, 5)) 
print("Subtraction:", mathfunctions.subtract(10, 5))
print("Multiplication:", mathfunctions.multiply(10, 5))
print("Division:", mathfunctions.divide(10, 5))
print("Circle Area (radius=7):", areafunctions.circle_area(7))
print("Rectangle Area (5x10):", areafunctions.rectangle_area(5, 10))
print("Triangle Area (base=6, height=8):", areafunctions.triangle_area(6, 8))
