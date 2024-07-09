# shopping_list_manager.py

def display_menu():
    """
    Displays the menu of options for the user.
    """
    print(f"\n{'Shopping List Manager':^30}")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")
    print("Please select an option (1-4): ")

def add_item(shopping_list):
    """
    Adds an item to the shopping list.
    """
    item = input("Enter the item name to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    """
    Removes an item from the shopping list.
    """
    item = input("Enter the item name to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' is not in the shopping list.")

def view_list(shopping_list):
    """
    Displays all items in the shopping list.
    """
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

def main():
    """
    Main function to run the shopping list manager.
    """
    shopping_list = []  # Start with an empty list
    
    while True:
        display_menu()
        
        try:
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue
        
        if choice == 1:
            add_item(shopping_list)
        elif choice == 2:
            remove_item(shopping_list)
        elif choice == 3:
            view_list(shopping_list)
        elif choice == 4:
            print("Exiting the shopping list manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

