opened_file = open("2022_sales.txt")
read_file = opened_file.read()
first_3_orders = read_file[:23]
print(first_3_orders)
split_orders = first_3_orders.split("\n")
print(split_orders)
opened_file.close()
