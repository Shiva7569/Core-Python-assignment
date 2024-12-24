Cart = {}
total = 0

def add_Cart():
    newCart = input("Enter the Cart Name You Want to Add = ")
    newCartPrice = int(input(f"Enter cost of {newCart} = "))
    Cart[newCart] = newCartPrice

def calculate_total_price():
    global total 
    total = sum(value for value in Cart.values() if value >= 0)
    if len(Cart) >= 5:
        discount = total * 0.10
        discounted_total = total - discount
        print(f"Total Cost Of Shopping is = {total}")
        print(f"Discount Applied (10%) = {discount}")
        print(f"Total Cost After Discount = {discounted_total}")
    else:
        print(f"Total Cost Of Shopping is = {total}")
    print("_______________________")

def ViewOptions():
    while True:
        try:
            print("================================")
            print("1.To Add Items Into Cart.")
            print("2.Exit")
            operation = int(input("Enter the operation : "))
            match operation:
                case 1:
                    add_Cart()
                    calculate_total_price()  
                case 2:
                    exit() 
                case _:
                    print("Invalid input, try again.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
ViewOptions()
