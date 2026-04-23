#Problem 13: Making Change

change = int(input("Enter change in cents as an integer: "))
toonies = change // 200
change = change % 200
loonies = change // 100
change = change % 100
quarters = change // 25
change = change % 25
dimes = change // 10
change = change % 10
nickels = change // 5
change = change % 5
pennies = change // 1
change = change % 1

print(f"\nChange breakdown")
print(f"Toonies: {int(toonies)}")
print(f"Loonies: {int(loonies)}")
print(f"Quarters: {int(quarters)}")
print(f"Dimes: {int(dimes)}")
print(f"Nickels: {int(nickels)}")
print(f"Pennies: {int(pennies)}")