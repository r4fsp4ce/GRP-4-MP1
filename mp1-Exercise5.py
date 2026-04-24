#Exercise 5 Bottle Deposit Calculator 
print("Bottle Deposit Calculator") 

small_count = int(input("Enter Small containers (<=1L): ")) 
large_count = int(input("Enter Large containers (>1L): ")) 

SMALL_RATE = 0.10 
LARGE_RATE = 0.25 

small_total = small_count * SMALL_RATE 
large_total = large_count * LARGE_RATE 

total_refund = small_total + large_total 

print("\n--- Breakdown ---") 
print(f"Small Refund: ${small_total:.2f}") 
print(f"Large Refund: ${large_total:.2f}") 
print(f"Toral Refund: ${total_refund:.2f}") 