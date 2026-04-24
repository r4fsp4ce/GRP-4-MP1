#Exercise 6 Order Weight Calculator 
print("Order Weight Calculator") 

widgets = int(input("Enter number of widgets: ")) 
gizmos = int(input("Enter number of gizmos): ")) 

WIDGET_WEIGHT = 75 
GIZMO_WEIGHT = 112 

total_widget_weight = widgets * WIDGET_WEIGHT 
total_gizmo_weight = gizmos * GIZMO_WEIGHT 

overall_weight = total_widget_weight + total_gizmo_weight 

print("\n--- Weight Summary ---") 
print(f"Widgets Weight: {total_widget_weight}") 
print(f"Gizmos Weight: {total_gizmo_weight}") 
print(f"Total Weight: {overall_weight}") 