# Exercise 8 Order Weight Calculator

widgets = int(input("Enter number of widgets: "))
gizmos = int(input("Enter number of gizmos: "))

Total_widget_weight = widgets * 75
Total_gizmo_weight = gizmos * 112

total_weight = (widgets * 75) + (gizmos * 112)

print("\n--- Weight Summary ---")
print(f"Widgets Weight: {Total_widget_weight} grams")
print(f"Gizmos Weight: {Total_gizmo_weight} grams")
print(f"Total Weight: {total_weight} grams")

