# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.
    Returns:
    - float: The temperature converted to Celsius.
    """
    FAHRENHEIT_TO_CELSIUS_OFFSET = 32
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius


def convert_to_fahrenheit(celsius):
    CELSIUS_TO_FAHRENHEIT_OFFSET = 32
    """
    Converts a temperature from Celsius to Fahrenheit.

    Parameters:
    - celsius (float): The temperature in Celsius.

    Returns:
    - float: The temperature converted to Fahrenheit.
    """
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit


def main():
    """
    Main function to handle user interaction and perform temperature conversions.
    """
    print("Temperature Conversion Tool")

    while True:
        try:
            # Prompt the user for the temperature value and the unit
            temp_input = input("Enter the temperature to convert: ")
            Unit_1 = input ("Is this temperature in Celsius or Fahrenheit? (C / F): ")
            if Unit_1 == 'C':
                # Extract the numeric value
                celsius_temp = float(temp_input)
                # Convert to Fahrenheit
                fahrenheit_temp = convert_to_fahrenheit(celsius_temp)
                print(f"{celsius_temp}°C is equal to {fahrenheit_temp:.2f}°F")
            elif Unit_1 == 'F':
                # Extract the numeric value
                fahrenheit_temp = float(temp_input)
                # Convert to Celsius
                celsius_temp = convert_to_celsius(fahrenheit_temp)
                print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C")
            else:
                raise ValueError("Invalid temperature unit. Please enter a temperature ending with 'C' or 'F'.")
        except ValueError:
            # Handle invalid temperature input
            print("Invalid temperature. Please enter a numeric value followed by 'C' or 'F'.")

        # Ask if the user wants to perform another conversion
        another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()
        if another_conversion != 'yes':
            break
    print("Goodbye!")

if __name__ == "__main__":
    main()

