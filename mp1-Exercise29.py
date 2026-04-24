#Exercise 29 Temperature Converter

print("Temperature Converter")

cel = float(input("Enter Temperature in Celsius: "))

fah = (cel * 9/5) + 32
kel = cel + 273.15

print("\n--- Converted Results ---")
print(f"Celsius    : {cel:.2f}")
print(f"Fahrenheit : {fah:.2f}")
print(f"Kelvin     : {kel:.2f}")

print("\n Conversion Complete!")