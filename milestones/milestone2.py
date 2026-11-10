# Milestone 2 - Manage Multiple Print Jobs Using Collections and Decisions
# 3D Printing Service Job and Material Usage Tracker

# material rates (Rs. per gram) stored in a dictionary
materials = {"PLA": 1.20, "PETG": 1.50, "ABS": 1.35, "TPU": 2.00}

MACHINE_RATE = 100      # Rs. per hour
jobs = []               # list that stores all accepted jobs

print("===== 3D Printing Job Manager =====")
print("\n------ MATERIAL RATES ------")
for name in materials:
    print(f"{name:<5} - Rs. {materials[name]:.2f}/g")
print("Type DONE as the model name when all jobs are entered.\n")

# keep accepting jobs until the user types DONE
while True:
    model = input("Enter model name: ").strip()
    if model.upper() == "DONE":
        break

    material = input("Enter material (PLA/PETG/ABS/TPU): ").strip().upper()
    weight = float(input("Enter filament weight (g): "))
    duration = int(input("Enter print duration (minutes): "))

    # reject an unknown material
    if material not in materials:
        print("Rejected! Unknown material:", material)
        continue

    # reject non-positive weight or duration
    if weight <= 0:
        print("Rejected! Filament weight must be above 0.")
        continue
    if duration <= 0:
        print("Rejected! Duration must be above 0.")
        continue

    # classify the duration
    if duration <= 60:
        category = "Quick"
    elif duration <= 240:
        category = "Standard"
    else:
        category = "Long"

    # charge = material cost + machine cost (Rs. 100 per hour)
    charge = weight * materials[material] + (duration / 60) * MACHINE_RATE

    # store the accepted job
    jobs.append({"model": model.title(), "material": material,
                 "weight": weight, "duration": duration,
                 "category": category, "charge": charge})
    print("Job accepted:", model.title(), "-", category)

# final summary
line = "-" * 62
if len(jobs) == 0:
    print("\nNo valid jobs were entered.")
else:
    total_weight = 0
    total_charge = 0
    used_materials = set()          # a set keeps only unique materials
    for job in jobs:
        total_weight = total_weight + job["weight"]
        total_charge = total_charge + job["charge"]
        used_materials.add(job["material"])

    print()
    print(line)
    print("               PRINT JOBS SUMMARY")
    print(line)
    for job in jobs:
        print(f"{job['model']:<15} {job['material']:<5} {job['weight']:>6.1f} g "
              f"{job['duration']:>4} min  {job['category']:<8} Rs. {job['charge']:>7.2f}")
    print(line)
    print("Total Jobs         :", len(jobs))
    print("Unique Materials   :", len(used_materials), sorted(used_materials))
    print(f"Total Filament     : {total_weight:.1f} g")
    print(f"Total Charge       : Rs. {total_charge:.2f} (at Rs. {MACHINE_RATE}/hour)")
    print(line)
