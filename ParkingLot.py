class ParkingLot:
    def __init__(self, vehicles):
        self.vehicles = vehicles

    def is_parked(self, vehicle):
        return vehicle in self.vehicles

    def duplicate_vehicles(self):
        duplicates = []

        for vehicle in self.vehicles:
            if self.vehicles.count(vehicle) > 1 and vehicle not in duplicates:
                duplicates.append(vehicle)

        return duplicates

    def unique_vehicle_count(self):
        return len(set(self.vehicles))


parking = ParkingLot([101, 105, 110, 101, 115, 105])

print("Duplicate Vehicles:", parking.duplicate_vehicles())
print("Unique Vehicles:", parking.unique_vehicle_count())
