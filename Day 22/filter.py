fruits = ['apple', 'banana', 'cherry', 'blueberry']

for fruit in fruits:
    if fruit.startswith('b'):
        print(f"Fruit starting with 'b': {fruit.title()}")
    elif fruit.startswith('a'):
        print(f"Fruit starting with 'a': {fruit.title()}")
    else:
        print(f"Other fruit: {fruit.title()}")