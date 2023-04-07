"""

Vehicle_Questionnaire.py

Author: Joe Douglas

This program is designed to take in the user's inputs through a series of questions and then have them
go through classes to evaluate the data, and then output the data for the user to read.

"""

class Vehicle:
    """Parent class designed to take the user's input for vehicle"""

    def __init__(self, type):
        self.type = type


class Automobile(Vehicle):
    """Class designed to take the user's input for the description of the vehicle"""

    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


user_type = (input("Please enter the type of your vehicle: "))
user_year = (input("Please enter the year of your vehicle: "))
user_make = (input("Please enter the maker of your vehicle: "))
user_model = (input("Please enter the model of your vehicle: "))
user_doors = (input("Please enter the number of doors on your vehicle: "))
user_roof = (input("Please enter type of roof on your vehicle: "))

# A series of inputs designed to store the information on the vehicle before going through classes

vehicle_1 = Automobile(user_type, user_year, user_make, user_model, user_doors, user_roof)


print("\n Vehicle Specifications \n")

print(f"Vehicle type: {vehicle_1.type}")
print(f"Year: {vehicle_1.model}")
print(f"Make:  {vehicle_1.make}")
print(f"Model: {vehicle_1.model}")
print(f"Number of doors: {vehicle_1.doors}")
print(f"Type of roof: {vehicle_1.roof}")

# Printing results