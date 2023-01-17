
print("Welcome to the Shop!")
stock = {"apple": 35, "banana": 18, "orange": 26}
print("Currently in stock:")
for item, price in stock.items():
    print(f"{item} ({price}p)")

basket = []

choice = input("Pick an item, or press Enter to checkout: ")


while choice != "":
    
    if choice in stock:
        
        basket.append(choice)
       
        print("Item added.")
    else:
        
        print("No such item. Try again.")
    choice = input("Pick an item, or press Enter to checkout: ")


if len(basket) == 0:
    print("You have not purchased any items.")
    exit()


total = 0
for item in basket:
    total += stock[item]


print("Thank you. You have purchased", end=" ")
for item in basket:
    print(item, end=" - ")
print(f"at a cost of {total}p.")
