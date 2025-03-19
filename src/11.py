import random 
def get_random_python_code(length=10):
    # Define a list of characters to use in the code
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    # Use random.choices() to generate a string of random characters from the list
    code = ''.join(random.choices(chars, k=length))
    return code 