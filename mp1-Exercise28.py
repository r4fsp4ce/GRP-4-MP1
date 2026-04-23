# Exercise 28: Wind Chill
Ta = float(input("Enter air temperature (Celsius): "))
V = float(input("Enter wind speed (km/h): "))

if Ta > 10 or V <= 4.8: 
    print("Input invalid. Temperature must be <= 10°C and wind speed must exceed 4.8 km/h.")
else:
    WCI = 13.12 + (0.6215 * Ta) - (11.37 * (V ** 0.16)) + (0.3965 * Ta * (V ** 0.16))
    print(f"\nWind Chill Index: {round(WCI)}")