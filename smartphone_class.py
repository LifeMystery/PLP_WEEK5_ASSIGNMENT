# Class representing a Smartphone
class Smartphone:
    def __init__(self, brand, model, storage, battery_life):
        self.brand = brand  # Smartphone brand
        self.model = model  # Model of the smartphone
        self.storage = storage  # Storage capacity in GB
        self.battery_life = battery_life  # Battery life in hours

    def display_info(self):
        """Displays the smartphone's information."""
        print(f"Smartphone Info:\nBrand: {self.brand}\nModel: {self.model}\nStorage: {self.storage}GB\nBattery Life: {self.battery_life} hours")

    def make_call(self, number):
        """Simulate making a call."""
        print(f"Calling {number}...")

    def charge_battery(self):
        """Simulate charging the phone."""
        print("Charging phone... Battery is now full!")

# Creating an instance of the Smartphone class
my_phone = Smartphone("Apple", "iPhone 13", 128, 20)
my_phone.display_info()  # Display phone information
my_phone.make_call("123-456-7890")  # Simulate making a call
my_phone.charge_battery()  # Simulate charging the phone
