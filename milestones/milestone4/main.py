# main.py
# Milestone 4 - Organize the Application Using Functions and Modules
import time
from print_utils import job_summary, totals, select_jobs

# sample jobs: each job is a dictionary
jobs = [
    {"job_id": 101, "customer": "Riya",  "model": "Phone Stand", "material": "PLA",  "grams": 85,  "minutes": 150},
    {"job_id": 102, "customer": "Arjun", "model": "Drone Frame", "material": "PETG", "grams": 210, "minutes": 320},
    {"job_id": 103, "customer": "Meera", "model": "Gear Set",    "material": "ABS",  "grams": 60,  "minutes": 45},
    {"job_id": 104, "customer": "Kabir", "model": "Phone Case",  "material": "TPU",  "grams": 40,  "minutes": 180},
    {"job_id": 105, "customer": "Sana",  "model": "Chess Piece", "material": "PLA",  "grams": 25,  "minutes": 60},
]

start = time.time()
line = "-" * 62

print("===== 3D Printing Service Job and Material Usage Tracker =====")
print("Summary Generated :", time.strftime("%d-%m-%Y %I:%M:%S %p"))
print(line)
for job in jobs:
    print(job_summary(job))
print(line)

# total filament and total charge (machine_rate passed as keyword)
total_filament, total_charge = totals(jobs, machine_rate=100)
print(f"Total Jobs     : {len(jobs)}")
print(f"Total Filament : {total_filament:.1f} g")
print(f"Total Charge   : Rs. {total_charge:.2f}")
print(line)

# function passed as argument: lambda selects jobs longer than 240 minutes
long_jobs = select_jobs(jobs, lambda job: job["minutes"] > 240)
print("Jobs longer than 240 minutes:")
for job in long_jobs:
    print(" ", job_summary(job))

print(line)
print(f"Time taken to generate summary: {time.time() - start:.4f} seconds")
