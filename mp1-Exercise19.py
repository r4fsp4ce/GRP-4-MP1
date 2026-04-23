#Problem 19: Free Fall
import math

iV = 0
a = 9.8
d = float(input("Enter height in meters (m): "))
fV = math.sqrt(pow(iV, 2) + (2 * a * d))
print(f"The final velocity of the object given {d} m distance is {fV:.2f} m/s.")