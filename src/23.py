def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

def multiply_numbers(x, y):
    return x * y

def divide_numbers(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

# Example usage
result_addition = add_numbers(3, 4)
result_subtraction = subtract_numbers(10, 5)
result_multiplication = multiply_numbers(2, 7)
result_division = divide_numbers(8, 0)

print("Addition:", result_addition)
print("Subtraction:", result_subtraction)
print("Multiplication:", result_multiplication)
print("Division:", result_division)
