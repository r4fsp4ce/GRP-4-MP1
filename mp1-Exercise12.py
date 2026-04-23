#Exercise 12: Distance Between 2 Points on Earth
import math

t1 = math.radians(float(input("Enter latitude of the first point (degrees): ")))
g1 = math.radians(float(input("Enter longitude of the first point (degrees): ")))
t2 = math.radians(float(input("Enter latitude of the second point (degrees): ")))
g2 = math.radians(float(input("Enter longitude of the second point (degrees): ")))

distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))
print(f"\nThe distance between the two points is {distance:.2f} km.")