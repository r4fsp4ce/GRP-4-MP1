# Exercise 31: Sum of the Digits in an Integer

num = int(input("Enter a four-digit integer: "))
thousands = num // 1000
hundreds = (num % 1000) // 100
tens = (num % 100) // 10
ones = num % 10

total = thousands + hundreds + tens + ones

print("Sum of the digits is:", total)
