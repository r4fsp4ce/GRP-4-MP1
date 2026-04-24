# Exercise 18
import math

radius = float(input("Enter radius of cylinder: "))
height = float(input("Enter height of cylinder: "))

area = radius ** 2 * math.pi
volume = area * height

print(f"The volume of the cylinder: {volume:.1f}")
