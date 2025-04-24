def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    return x / y

def calculator():
    while True:
        num1 = input("Enter first number: ")
        try:
            num1 = float(num1)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        operation = input("Choose operation (+, -, *, /): ")
        
        num2 = input("Enter second number: ")
        try:
            num2 = float(num2)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            print("Invalid operation. Please choose +, -, *, or /.")
            continue
        
        print(f"{num1} {operation} {num2} = {result}")
        
        cont = input("Do you want to continue? (y/n): ").lower()
        if cont != 'y':
            break

if __name__ == "__main__":
    calculator()