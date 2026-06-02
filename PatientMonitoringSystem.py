class Patient:
    def __init__(self, name, temperatures):
        self.name = name
        self.temperatures = temperatures

    def highest_temperature(self):
        return max(self.temperatures)

    def lowest_temperature(self):
        return min(self.temperatures)

    def abnormal_readings(self):
        count = 0

        for temp in self.temperatures:
            if temp > 100:
                count += 1

        return count


patient = Patient(
    "Kumar",
    [98.4, 99.1, 101.2, 102.3, 98.9]
)

print("Highest Temperature:", patient.highest_temperature())
print("Lowest Temperature:", patient.lowest_temperature())
print("Abnormal Readings:", patient.abnormal_readings())
