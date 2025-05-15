# Print only even numbers from 1 to 10 and their square
for i in range(1, 11):
    if i % 2 == 0:
        print(f"Even number: {i}, Square: {i ** 2}")
    else:
        print(f"Odd number: {i}")   