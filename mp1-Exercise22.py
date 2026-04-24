# Exercise 22
import math

side1 = float(input("enter s1: "))
side2 = float(input("enter s2: "))
side3 = float(input("enter s3: "))

s = (side1 + side2 + side3)/2
area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print(f"The area of the triangle is: {area:.2f}")