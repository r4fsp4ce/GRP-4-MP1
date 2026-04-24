#Exercise 14: Height Units

feet = int(input("Enter height (feet): "))
inches = int(input("Enter remeaining inches: "))

total_inches = (feet * 12) + inches

centimeters = total_inches * 2.54

print("Your height in centimers is:", centimeters)