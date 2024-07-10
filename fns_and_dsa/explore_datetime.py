from datetime import datetime, timedelta


def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    # Print the formatted current date and time
    print(f"Current Date and Time: {formatted_date}")


def calculate_future_date(days):
    """
    Calculates the future date given a number of days to add to the current date.

    Parameters:
    - days (int): The number of days to add to the current date.

    Returns:
    - future_date (datetime.date): The calculated future date.
    """
    # Get the current date and time
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    # Print the future date
    print(f"Future Date : {formatted_future_date}")


def main():
    """
    Main function to execute the two parts of the program.
    """
    # Part 1: Display the current date and time
    display_current_datetime()

    # Part 2: Calculate and display the future date
    while True:
        try:
            # Prompt the user to enter the number of days
            days = int(input("Enter the number of days to add to the current date: ").strip())
            if days < 0:
                # Handle the case where the user enters a negative number
                print("Please enter a non-negative integer for the number of days.")
            else:
                # Call the function to calculate the future date
                calculate_future_date(days)
                break  # Exit the loop once a valid number of days is entered
        except ValueError:
            # Handle the case where the user does not enter a valid integer
            print("Please enter a valid integer for the number of days.")


if __name__ == "__main__":
    main()

