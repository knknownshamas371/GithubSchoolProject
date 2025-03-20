def multiply_numbers(x, y):
    return x * y

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        raise ValueError("Cannot divide by zero")

# Example usage
num1 = multiply_numbers(5, 3)
print(num1)  # Output: 15
