#Exercise 15 Distance Converter
print("Distance Converter")

feet = float(input("Enter distance in feet: "))

inches = feet * 12
yards = feet / 3
miles = feet / 5280

print("\n--- Converted Values ---")
print(f"Inches : {inches:.2f}")
print(f"Yards : {yards:.2f}")
print(f"Miles : {miles:.6f}")

print("\n(Note: 1 mile = 5280 feet)")