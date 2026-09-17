U_I = input("Enter the price of the item: ")

try:
    price = float(U_I)
    if price < 0:
        print("Invalid input! Please enter a valid decimal number.")
    else:
        print(f"The price entered is {price}")
except:
    print("Invalid input! Please enter a valid decimal number.")
