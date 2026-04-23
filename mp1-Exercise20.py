#Problem 20: Ideal Gas Law

R = float(8.314) #ideal gas constant in J/molK 
P = float(input("Enter pressure (Pascals): "))
V = float(input("Enter volume (Liters): "))
unitT = input("Enter the unit of temperature [Celsius (C) | Fahrenheit (F)]: ").upper()
T = float(input("Enter temperature: "))

if unitT == 'C':
    T += 273.15    
elif unitT == 'F':
    T = (T - 32) * (5/9) + 273.15
else: 
    print("\nInvalid unit.")
    exit()

n = float((P * V)/(R * T)) 
print(f"\nAmount of substance in moles is {n:.04f}")