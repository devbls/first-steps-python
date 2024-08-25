# Defining values for different products
hamburger = 10.50
fries = 4.00
soda = 3.00

hamburger_quantity = int(input("Type the desired hamburger quantity: "))
fries_quantity = int(input("Type the desired fries quantity: "))
soda_quantity = int(input("Type the desired soda quantity: "))

total_price = (hamburger * hamburger_quantity) + (fries * fries_quantity) + (soda * soda_quantity)

print("The total value is: $", total_price)