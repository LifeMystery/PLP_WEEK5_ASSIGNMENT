# PLP_WEEK5_ASSIGNMENT

# Python OOP and Inheritance Challenge

This repository contains examples of object-oriented programming (OOP) concepts in Python, including classes, inheritance, polymorphism, and method overriding.

## Files

### 1. `smartphone_class.py`

This script defines a `Smartphone` class with the following features:
- **Attributes**: Brand, model, storage, and battery life.
- **Methods**:
  - `display_info()`: Displays the smartphone’s details.
  - `make_call(number)`: Simulates making a call.
  - `charge_battery()`: Simulates charging the smartphone.

### 2. `superphone_inheritance.py`

This script demonstrates **inheritance** in Python. It extends the `Smartphone` class to create a `Superphone` class, which adds:
- **New attribute**: Camera quality.
- **Overridden method**: `display_info()` method is overridden to include camera quality in the information output.
- **New method**: `take_photo()` to simulate taking a photo.

### 3. `polymorphism_vehicles.py`

This script demonstrates **polymorphism** in Python, where multiple classes define the same method (`move()`), but each class implements it differently:
- **Vehicle** class (base class) defines a general `move()` method.
- **Car**, **Plane**, and **Boat** classes (subclasses) implement the `move()` method in their own way.
- A function `vehicle_move()` is used to demonstrate polymorphism by calling the `move()` method on different vehicle objects.

## How to Run the Code

1. Clone or download this repository.
2. Open the terminal and navigate to the directory where the scripts are stored.
3. Run any of the Python scripts by using the following command:

```bash
python <script_name>.py
#For example, to run the smartphone_class.py script: python smartphone_class.py
