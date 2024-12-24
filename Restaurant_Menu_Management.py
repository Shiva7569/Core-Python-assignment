items = []

def add_item(items, item):
    items.append(item)

def delete_item():
    itemsToRemove = input("Enter The Name Of The Item You Want To Delete = ")
    if itemsToRemove in items:
        items.remove(itemsToRemove)
        print(f"{itemsToRemove} has been removed from the menu.")
    else:
        print(f"{itemsToRemove} not found in the menu.")

def check_item():
    checkItem = input("Enter the item name to check if it's in the menu or Not = ")
    if checkItem in items:
        print("Avaialbility :",checkItem,"is available")
    else:
        print(f"{checkItem} is not available in the menu.")

def view_items(items):
    print(items)

def operations_on_items():
    while True:
        print("1. Add item")
        print("2. Remove item")
        print("3. View items and check an item")
        print("4. Exit")
        choice = int(input("Enter the choice : "))
        match choice:
            case 1:
                item = input("Enter the item to be added: ")
                add_item(items, item)
            case 2:
                delete_item()
            case 3:
                view_items(items)
                check_item()
            case 4:
                print("Exiting...")
                break 
            case _:
                print("Invalid input, try again.")
operations_on_items()
