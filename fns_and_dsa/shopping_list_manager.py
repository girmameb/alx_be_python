def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")


def main():
    """
    Main function to handle user interaction and manage the shopping list.
    """
    shopping_list = []  # Initialize an empty shopping list

    while True:
        display_menu()  # Display the menu options

        # Prompt the user for their choice
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            # Add an item to the shopping list
            item = input("Enter the item to add: ").strip()
            shopping_list.append(item)
            print(f"Added '{item}' to the shopping list.")

        elif choice == '2':
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"Removed '{item}' from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")

        elif choice == '3':
            # View the current shopping list
            if shopping_list:
                print("Current Shopping List:")
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
            else:
                print("The shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()

