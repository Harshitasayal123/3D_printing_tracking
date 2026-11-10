# print_utils.py
# functions for the 3D printing service tracker
import math

# material rates (Rs. per gram)
MATERIAL_RATES = {"PLA": 1.20, "PETG": 1.50, "ABS": 1.35, "TPU": 2.00}


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
