# Milestone 1 - Calculate the Cost of a Single 3D Print Job
# 3D Printing Service Job and Material Usage Tracker

print("===== 3D Printing Service - Single Job Cost Estimate =====")

# taking input and converting numbers to float / int
customer_name = input("Enter customer name: ")
model_name = input("Enter model name: ")
filament_grams = float(input("Enter filament weight (g): "))
cost_per_gram = float(input("Enter filament cost per gram (Rs.): "))
duration_minutes = int(input("Enter print duration (minutes): "))
machine_rate = float(input("Enter machine rate per hour (Rs.): "))

# checking the data types
print("\nData type of filament weight :", type(filament_grams))
print("Data type of duration        :", type(duration_minutes))

# cost calculation
material_cost = filament_grams * cost_per_gram
machine_cost = (duration_minutes / 60) * machine_rate
total_cost = material_cost + machine_cost

# // and % give the duration as hours and minutes
hours = duration_minutes // 60
minutes = duration_minutes % 60

# printing the result, title() shows the model name neatly
line = "-" * 44
print()
print(line)
print("        3D PRINT JOB COST ESTIMATE")
print(line)
print("Customer       :", customer_name.title())
print("Model          :", model_name.title())
print("Filament       :", filament_grams, "g")
print("Duration       :", hours, "h", minutes, "min")
print(line)
print(f"Material Cost  : Rs. {material_cost:.2f}")
print(f"Machine Cost   : Rs. {machine_cost:.2f}")
print(f"Total Cost     : Rs. {total_cost:.2f}")
print(line)
