# Exercise 30

pressure = float(input("Enter pressure in kilopascals (kPa): "))

psi = pressure * 0.1450377377
mmhg = pressure * 7.500615613
atm = pressure * 0.0098692327

print(f"Pressure in PSI: {psi:.2f}")
print(f"Pressure in mmHg: {mmhg:.2f}")
print(f"Pressure in atm: {atm:.2f}")