cart = []




items_name = input("What is the items name? ")
items_price = input("What is the items price? ")
items_quanity = input("What is the item quantity? ")
item = { "name": items_name, "price": items_price, "quantiy": items_quanity
    }
cart.append(item)    
print(cart)

answer = input("Do you want to add more items to the cart? Y/N ").lower()

if answer == "y":
    items_name2 = input("What is the items name? ")
    items_price2 = input("What is the items price? ")
    items_quanity2 = input("What is the item quantity? ") 
    item2 = {"name": items_name2, "price": items_price2, "quantiy": items_quanity2} 
    cart.append(item2)
    print(cart)
    
elif answer == "n":
    pass

answer2 = input("Do you want to delete anything from your cart? Y/N ").lower()

if answer2 == "y":
    input("Do you want to remove item1? Y/N ").lower()
    y = cart.remove(item)

else:
    pass

if answer2 == "y":
    input("Do you want to remove item2? Y/N ").lower()
    y = cart.remove(item2)

else:
    pass

input("Do you want to see whats in your shopping cart? Y/N? ").lower()

print(cart)





    