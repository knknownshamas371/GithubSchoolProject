def get_random_string(length):
    import random
    import string
    letters = string.ascii_lowercase
    result = ''.join(random.choice(letters) for i in range(length))
    return result
