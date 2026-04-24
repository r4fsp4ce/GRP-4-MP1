# Exercise 16
import math
radius = float(input("Enter radius: "))

area = radius ** 2 * math.pi
volume = radius ** 3 * math.pi * (4 / 3)

print(f"The area of the circle is: {area:.2f}")
print(f"The volume of the circle is: {volume:.2f}")