# Prompt user for task details
task = input("Enter your task : ")
priority = input ("priority (high, medium, low): ")
time_bound = input ("Is it time-bound? (yes or no): ").lower()

# Process the task based on priority
match priority:
    case 'high':
        reminder = f"Task: '{task}' is high priority task."
    case 'medium':
        reminder = f"Task: '{task}' is medium priority task."
    case 'low':
        reminder = f"Task: '{task}' is low priority task."
    case _:
        reminder = f"Task: '{task}' is an unrecognized priority task."

# Modify reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " This task is time-bound and requires immediate attention today!"

# Print the customized reminder
print(reminder)

