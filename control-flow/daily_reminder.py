# Prompt user for task details
task = input("Enter your task: ")

# Prompt for priority
priority = input("Priority (high/medium/low): ")

# Prompt for time-bound status
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task based on priority
match priority:
    case 'high':
        reminder = f"Task: '{task}' has high priority task."
    case 'medium':
        reminder = f"Task: '{task}' has medium priority task."
    case 'low':
        reminder = f"Task: '{task}' has low priority task."
    case _:
        reminder = f"Task: '{task}' has an unrecognized priority task."

# Modify reminder if the task is time-bound
if time_bound == 'yes':
    reminder += " This task is time-bound and requires immediate attention today!"

# Print the customized reminder
print(reminder)
