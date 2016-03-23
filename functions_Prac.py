"""Various mini functions for calculations/conversions"""

def main():
    print("Rectangle Area: ", calculate_area_rectangle(4, 5))
    print("Fahrenheit Value: ", convert_Celsius_to_Fahrenheit(0))
    print("Your BMI is:", calculate_BMI(1.8, 70))


def calculate_area_rectangle(height, width):
    return height * width

def convert_Celsius_to_Fahrenheit(celsius):
    return celsius * 1.8 + 32

def calculate_BMI(height, weight):
    return "{:.2f}".format(weight/height**2)

main()