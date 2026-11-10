# main.py
# 3D Printing Service Job and Material Usage Tracker - Final Version
import time
from print_utils import (material_cost, machine_cost, classify_duration,
                         validate_job, save_record, read_records, next_job_id)

print("===== 3D Printing Service Job and Material Usage Tracker =====")

while True:
    print("\n1. Add Print Job")
    print("2. View Saved Jobs")
    print("3. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        customer = input("Enter customer name: ").strip().title()
        model = input("Enter model name: ").strip().title()
        material = input("Enter material (PLA/PETG/ABS/TPU): ").strip().upper()

        # handle wrong or impossible numeric values
        try:
            grams = float(input("Enter filament weight (g): "))
            minutes = int(input("Enter print duration (minutes): "))
            rate_text = input("Enter machine rate per hour (Enter for 100): ").strip()
            machine_rate = float(rate_text) if rate_text != "" else 100.0
            validate_job(material, grams, minutes, machine_rate)
        except ValueError as error:
            print("Invalid input!", error)
            print("Job not saved. Please enter valid numbers.")
            continue

        # cost calculation using the module functions
        mat = material_cost(material, grams)
        mac = machine_cost(minutes, machine_rate=machine_rate)
        total = mat + mac
        job_id = next_job_id()
        stamp = time.strftime("%d-%m-%Y %I:%M %p")

        record = (f"{job_id} | {customer} | {model} | {material} | {grams} g | "
                  f"{minutes} min | Rs. {total:.2f} | {stamp}")
        save_record(record)

        print("\n" + "-" * 50)
        print(f"Job ID        : {job_id}")
        print(f"Model         : {model} ({classify_duration(minutes)})")
        print(f"Material Cost : Rs. {mat:.2f}")
        print(f"Machine Cost  : Rs. {mac:.2f}")
        print(f"Total Charge  : Rs. {total:.2f}")
        print("-" * 50)
        print("Job saved to print_logs/print_jobs.txt")

    elif choice == "2":
        result = read_records()
        if result is not None:
            count, total_grams, total_charge = result
            print("Valid Jobs      :", count)
            print(f"Total Filament  : {total_grams:.1f} g")
            print(f"Total Charge    : Rs. {total_charge:.2f}")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
