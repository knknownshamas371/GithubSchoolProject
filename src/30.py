class ExampleClass:
    def __init__(self):
        self.data = {}

    def add_data(self, key, value):
        if key in self.data:
            raise ValueError("Key already exists")
        self.data[key] = value

    def get_data(self, key):
        return self.data.get(key)

    def delete_data(self, key):
        if key not in self.data:
            raise KeyError(f"Data with key {key} does not exist")

# Example usage
example_class = ExampleClass()
example_class.add_data("user", "John")
print(example_class.get_data("user"))  # Output: John

try:
    example_class.delete_data("user")
except ValueError as e:
    print(e)

try:
    example_class.delete_data("nonexistent_key")
except KeyError as e:
    print(e)
