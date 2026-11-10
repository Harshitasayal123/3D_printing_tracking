# Milestone 3 - Refactor the Same Application Using OOP
# 3D Printing Service Job and Material Usage Tracker

class PrintJob:
    machine_rate = 100          # class variable: Rs. per hour
    material_rates = {"PLA": 1.20, "PETG": 1.50, "ABS": 1.35, "TPU": 2.00}

    # constructor
    def __init__(self, job_id, customer_name, model_name, material,
                 filament_grams, duration_minutes):
        self.job_id = job_id
        self.customer_name = customer_name
        self.model_name = model_name
        self.material = material
        self.filament_grams = filament_grams
        self.duration_minutes = duration_minutes

    def material_cost(self):
        return self.filament_grams * PrintJob.material_rates[self.material]

    def machine_cost(self):
        return (self.duration_minutes / 60) * PrintJob.machine_rate

    def total_cost(self):
        return self.material_cost() + self.machine_cost()

    def display_summary(self):
        line = "-" * 40
        print(line)
        print("Job ID        :", self.job_id)
        print("Customer      :", self.customer_name)
        print("Model         :", self.model_name)
        print("Material      :", self.material)
        print("Filament      :", self.filament_grams, "g")
        print("Duration      :", self.duration_minutes, "min")
        print(f"Material Cost : Rs. {self.material_cost():.2f}")
        print(f"Machine Cost  : Rs. {self.machine_cost():.2f}")
        print(f"Total Cost    : Rs. {self.total_cost():.2f}")
        print(line)

    # short summary used by print()
    def __str__(self):
        return (f"Job {self.job_id}: {self.model_name} ({self.material}, "
                f"{self.filament_grams} g, {self.duration_minutes} min)")


print("===== 3D Printing Job Manager (OOP Version) =====\n")

# creating two objects
job1 = PrintJob(101, "Riya", "Phone Stand", "PLA", 85, 150)
job2 = PrintJob(102, "Arjun", "Drone Frame", "PETG", 210, 320)

print(job1)
job1.display_summary()
print()
print(job2)
job2.display_summary()

# isinstance() verifies the type of an object
print("\nisinstance(job1, PrintJob) :", isinstance(job1, PrintJob))
