from datetime import datetime, timedelta
def display_current_datetime():
    """
    Displays the current date and time in the format YYYY-MM-DD HH:MM:SS.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(days):
    """
    Calculates the future date given a number of days to add to the current date.

    Parameters:
    - days (int): The number of days to add to the current date.

    Returns:
    - future_date (datetime.date): The calculated future date.
    """
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    #print(f"Future Date after {days} days: {formatted_future_date}")
    print(f"Future Date: {formatted_future_date}")
