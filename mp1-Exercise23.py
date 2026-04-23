#Problem 23: Area of a Regular Polygon 
import math

s = int(input("Enter length of the polygon: "))
n = int(input("Enter number of sides: "))
area = (n * pow(s, 2)) / (4 * math.tan(math.pi/n))
print(f"The area of the regular polygon is {area:.02f} square units.")