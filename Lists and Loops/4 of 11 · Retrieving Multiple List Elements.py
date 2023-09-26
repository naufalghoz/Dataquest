# Each list has the following elements: [name, price, currency, quantity, rating]

keyboard_product = ["Keyboard", 29.50, "USD", 6, 4.80]
mouse_product = ["Mouse", 13.99, "USD", 14, 2.45]
keyboard_inventory = [keyboard_product[0],keyboard_product[1],keyboard_product[3],keyboard_product[1]*keyboard_product[3]]
mouse_inventory = [mouse_product[0],mouse_product[1],mouse_product[3],mouse_product[1]*mouse_product[3]]

average_inventory_pricing = (keyboard_inventory[3]+mouse_inventory[3])/2
print(average_inventory_pricing)
