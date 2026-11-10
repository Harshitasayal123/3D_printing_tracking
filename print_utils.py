# print_utils.py
# functions for the 3D printing service tracker (final version)
import math
import os

# material rates (Rs. per gram)
MATERIAL_RATES = {"PLA": 1.20, "PETG": 1.50, "ABS": 1.35, "TPU": 2.00}

# folder and file used to store the completed jobs
FOLDER = "print_logs"
FILE_PATH = os.path.join(FOLDER, "print_jobs.txt")


def material_cost(material, filament_grams):
    return filament_grams * MATERIAL_RATES[material]


# default/keyword parameter: machine_rate = 100
# math.ceil() rounds the print time UP to full chargeable hours
def machine_cost(duration_minutes, machine_rate=100):
    chargeable_hours = math.ceil(duration_minutes / 60)
    return chargeable_hours * machine_rate


# Quick (<=60), Standard (61-240), Long (>240)
def classify_duration(duration_minutes):
    if duration_minutes <= 60:
        return "Quick"
    elif duration_minutes <= 240:
        return "Standard"
    else:
        return "Long"


# job is a dictionary: job_id, customer, model, material, grams, minutes
def job_summary(job, machine_rate=100):
    mat = material_cost(job["material"], job["grams"])
    mac = machine_cost(job["minutes"], machine_rate=machine_rate)
    return (f"#{job['job_id']:<4}{job['model']:<14}{job['material']:<5}"
            f"{job['grams']:>6.1f} g {job['minutes']:>4} min "
            f"{classify_duration(job['minutes']):<9}Rs. {mat + mac:>7.2f}")


# jobs is a list of job dictionaries -> returns (total filament, total charge)
def totals(jobs, machine_rate=100):
    total_filament = 0
    total_charge = 0
    for job in jobs:
        total_filament = total_filament + job["grams"]
        total_charge = (total_charge + material_cost(job["material"], job["grams"])
                        + machine_cost(job["minutes"], machine_rate=machine_rate))
    return total_filament, total_charge


# a function that accepts another function (condition) as an argument
def select_jobs(jobs, condition):
    selected = []
    for job in jobs:
        if condition(job):
            selected.append(job)
    return selected


# raises ValueError for unknown material or impossible values
def validate_job(material, grams, minutes, machine_rate):
    if material not in MATERIAL_RATES:
        raise ValueError("Unknown material: " + material)
    if grams <= 0:
        raise ValueError("Filament weight must be above 0")
    if minutes <= 0:
        raise ValueError("Duration must be above 0")
    if machine_rate <= 0:
        raise ValueError("Machine rate must be above 0")


# creates print_logs folder if absent, then appends one record (mode "a")
def save_record(record):
    os.makedirs(FOLDER, exist_ok=True)
    with open(FILE_PATH, "a") as file:
        file.write(record + "\n")


# next job id = 101 + number of lines already saved
def next_job_id():
    try:
        with open(FILE_PATH, "r") as file:
            return 101 + len(file.readlines())
    except FileNotFoundError:
        return 101


# reads and displays all saved records, then shows the file size in bytes
# returns (valid records, total filament, total charge) or None if no file
def read_records():
    try:
        with open(FILE_PATH, "r") as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: print_logs/print_jobs.txt not found. Add a job first.")
        return None

    print("\n========== SAVED PRINT JOBS ==========")
    count = 0
    total_grams = 0
    total_charge = 0
    for number, line in enumerate(lines, start=1):
        text = line.strip()
        if text == "":
            continue
        parts = text.split(" | ")
        # a malformed record is skipped instead of crashing the program
        try:
            grams = float(parts[4].replace(" g", ""))
            charge = float(parts[6].replace("Rs. ", ""))
        except (ValueError, IndexError):
            print(f"[Skipped] Line {number}: malformed record -> {text}")
            continue
        print(text)
        count = count + 1
        total_grams = total_grams + grams
        total_charge = total_charge + charge

    print("-" * 50)
    print("File Size :", os.path.getsize(FILE_PATH), "bytes")
    return count, total_grams, total_charge
