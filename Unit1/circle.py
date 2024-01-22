import math

# define variables
radius = float(input("Enter radius:"))
area = math.pi * radius ** 2
circumference = radius * 2 * math.pi

print("Area :", round(area, 3), "cm^2")
print("Circumference :", round(circumference, 3), "cm")
