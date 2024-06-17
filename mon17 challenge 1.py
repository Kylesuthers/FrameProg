def calculate_costs():
    price_trousers = 20.0
    price_shirt = 15.99
    price_shoes = 29.99
    tax_rate = 8/100
    discount_rate = 20/100

    total_cost = (price_trousers + price_shirt + price_shoes) * (1 - discount_rate) * (1 + tax_rate)
    print(f"Total cost of purchase: £{total_cost:.2f}")

    refund = (price_trousers * 3 + price_shoes * 2) * (1 - discount_rate) * (1 + tax_rate)
    shirts_bought = int(refund / (price_shirt * (1 - discount_rate) * (1 + tax_rate)))
    leftover = refund - shirts_bought * (price_shirt * (1 - discount_rate) * (1 + tax_rate))

    print(f"The customer can buy {shirts_bought} shirts with the returned money.")
    print(f"The customer will have £{leftover:.2f} left over.")

calculate_costs()