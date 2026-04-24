# Exercise 32

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

middle = (num1 + num2 + num3) - max(num1, num2, num3) - min(num1, num2, num3)

print(f"The smallest number is: {min(num1, num2, num3)}")
print(f"The middle number is: {middle}")
print(f"The largest number is: {max(num1, num2, num3)}")