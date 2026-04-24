#Exercise 4 Area of a field in acres 
print("Field Area Calculator") 

length_ft = float(input("Enter field length (feet): ")) 
width_ft = float (input("Enter field width (feet): ")) 

area_sqft = length_ft * width_ft 

SQFT_PER_ACRE = 43560 

area_acres = area_sqft / SQFT_PER_ACRE 

print("\n--- Computation Details ---") 
print(f"Square Feet: {area_sqft:.2f}") 
print(f"Acres: {area_acres:.4f}") 