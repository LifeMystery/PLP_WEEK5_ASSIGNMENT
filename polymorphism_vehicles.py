# Base class for vehicles
class Vehicle:
    def move(self):
        """Base move method to be overridden by subclasses."""
        raise NotImplementedError("Subclass must implement abstract method")

# Car class inheriting from Vehicle
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class inheriting from Vehicle
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class inheriting from Vehicle
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Function to demonstrate polymorphism
def vehicle_move(vehicle):
    vehicle.move()

# Create instances of the vehicles
car = Car()
plane = Plane()
boat = Boat()

# Demonstrate polymorphism
vehicle_move(car)    # Outputs: Driving 🚗
vehicle_move(plane)  # Outputs: Flying ✈️
vehicle_move(boat)   # Outputs: Sailing ⛵
