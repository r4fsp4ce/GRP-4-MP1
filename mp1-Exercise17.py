#Problem 17: Heat Capacity
C = 4.186 #spec. heat of water 
m = float(input("Enter mass of water (grams): "))
iTemp = float(input("Enter initial temperature (Celsius): "))
fTemp = float(input("Enter final temperature (Celsius): "))
delTemp = fTemp - iTemp #change in temperature
q = m * C * delTemp
print(f"Amount of energy needed to achieve temperature change is {q:.02f} J")

kWh = q / 3600000 #kWh from J
cost = kWh * 0.089 
print(f"Cost of heating water is ${cost:.04f}")