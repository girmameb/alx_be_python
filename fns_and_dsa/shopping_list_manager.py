# shopping_list_manager.py

def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View list")
    print("4. Exit")

def add_item(shopping_list):
    """
    Prompts the user to enter an item name and adds it to the shopping list.
    
    Parameters:
    - shopping_list (list): The list where items will be added.
    """
    item = input("Enter the item name to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    """
    Prompts the user to enter an item name and removes it from the shopping list.
    If the item is not found, displays an error message.
    
    Parameters:
    - shopping_list (list): The list from which items will be removed.
    """
    item = input("Enter the item name to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    """
    Displays the current items in the shopping list.
    
    Parameters:
    - shopping_list (list): The list whose items will be displayed.
    """
    if shopping_list:
        print("\nCurrent shopping list:")
        for idx, item in enumerate(shopping_list, 1):
            print(f"{idx}. {item}")
    else:
        print("The shopping list is empty.")

def main():
    """
    Main function that drives the shopping list manager.
    """
    shopping_list = []

    while True:
        display_menu()
        choice = input("Choose an option (1, 2, 3, 4): ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()

