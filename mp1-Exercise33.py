#Exercise 33 "Day Old Bread"
print("Day-Old Bread Calculator")

bread = int(input("Enter number of day-old loaves: "))

reg_price = 3.49
dis_rate = 0.60

reg_total = bread * reg_price
dis_amount = reg_total * dis_rate 
final_total = reg_total - dis_amount

print("\n --- Pricing Details ---")
print(f"Regular Price Total   : ${reg_total:.2f}")
print(f"Discount (60%)        : -${dis_amount:.2f}")
print(f"Final Price           : ${final_total:.2f}")