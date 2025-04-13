# Subclass representing a Superphone
class Superphone(Smartphone):
    def __init__(self, brand, model, storage, battery_life, camera_quality):
        super().__init__(brand, model, storage, battery_life)  # Initialize the parent class
        self.camera_quality = camera_quality  # Additional attribute for camera quality

    def display_info(self):
        """Override the display_info method to include camera quality."""
        super().display_info()  # Call the parent method
        print(f"Camera Quality: {self.camera_quality}MP")

    def take_photo(self):
        """Simulate taking a photo."""
        print(f"Taking a photo with {self.camera_quality}MP camera!")

# Creating an instance of the Superphone class
my_superphone = Superphone("Samsung", "Galaxy S21", 256, 24, 108)
my_superphone.display_info()  # Display phone info with camera quality
my_superphone.take_photo()  # Simulate taking a photo
