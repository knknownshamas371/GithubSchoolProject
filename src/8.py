def get_random_code(length):
    import random
    
    # List of characters to choose from
    code_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    # Generate a random string of the specified length
    return ''.join(random.choice(code_chars) for i in range(length))
