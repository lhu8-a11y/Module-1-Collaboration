# Vehicle superclass
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Automobile subclass inheriting from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Main app
def main():
    print("===Vehicle Information Input System===\n")

    # Set vehicle type to "Car" as required
    vehicle_type = "car"

    # Get user input
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Create Automobile object
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Output the data in easy-to-read format
    print("\n===Vehicle Information===")
    print(f"Vehicle Type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of Doors: {car.doors}")
    print(f"Type of Roof: {car.roof}")

if __name__ == "__main__":
    main()