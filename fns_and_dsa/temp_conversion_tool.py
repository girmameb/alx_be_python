# Define Global Conversion Factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_OFFSET = 32
CELSIUS_TO_FAHRENHEIT_OFFSET = 32

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): Temperature in Fahrenheit.

    Returns:
    - float: Temperature in Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR, FAHRENHEIT_TO_CELSIUS_OFFSET
    # Convert Fahrenheit to Celsius using the formula: (F - 32) * 5/9
    celsius = (fahrenheit - FAHRENHEIT_TO_CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    - celsius (float): Temperature in Celsius.

    Returns:
    - float: Temperature in Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR, CELSIUS_TO_FAHRENHEIT_OFFSET
    # Convert Celsius to Fahrenheit using the formula: C * 9/5 + 32
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + CELSIUS_TO_FAHRENHEIT_OFFSET
    return fahrenheit

def main():
    """
    Main function to handle user interaction for temperature conversion.
    """
    print("Temperature Conversion Tool")
   # print("Choose the conversion type:")
   # print("F. Fahrenheit to Celsius")
   # print("C. Celsius to Fahrenheit")

    Temp1 = float(input("Enter the temperature to convert: "))
    choice = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
    if choice == 'F':
        try:
           # fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = convert_to_celsius(Temp1)
            print(f"{Temp1}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    
    elif choice == 'C':
        try:
            #celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = convert_to_fahrenheit(Temp1)
            print(f"{Temp1}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("Invalid temperature. Please enter a numeric value.")
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()

