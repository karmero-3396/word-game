chlid_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of an adult's meal? "))
children = int(input("How many children are there? "))
adults = int(input("How many adults are there? "))
price = chlid_meal * children + adult_meal * adults
print()
print(f"Subtotal: ${price:.2f}")
print()
tax_rate = float(input("What is the sales tax rate? "))
subtotal = tax_rate * price / 100
print(f"Sales Tax: ${subtotal:.2f}")
total_price = price + subtotal
print(f"Total: ${total_price:.2f}")
print()
payment = float(input("What is the payment amount? "))
change = payment - total_price
print(f"Change: ${change:.2f}")
