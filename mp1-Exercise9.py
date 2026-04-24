# mp1-Exercise9

deposit_amount = float(input("Enter deposit amount: "))
rate = 0.04

#Calculating the amount per year
year1 = deposit_amount * (1 + rate)
year2 = year1 * (1 + rate)
year3 = year2 * (1 + rate)

#Displaying the amount
print(f"Year 1: {year1:.2f}")
print(f"Year 2: {year2:.2f}")
print(f"Year 3: {year3:.2f}")