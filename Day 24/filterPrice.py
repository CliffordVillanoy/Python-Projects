# Only print items priced above 1.0
items = {'apple': 0.9, 'banana': 0.5, 'cherry': 2.5, 'mango': 1.8}

for item, price in items.items():
    if price > 1.0:
        print(f"{item.capitalize():<10} - Price: ${price:.2f}")
             