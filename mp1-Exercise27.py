#Exercise 27 BMI Calculator
print("BMI Calculator")

height = float(input("Enter height (meters): "))
weight = float (input("Enter weight (kg): "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

print("\n--- BMI Result ---")
print(f"BMI Value: {bmi:.2f}")
print(f"Category : {category}")