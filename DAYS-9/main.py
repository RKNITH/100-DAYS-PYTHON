#  PYTHON DICTIONARY:

# A dictionary in Python is a collection of key-value pairs. Each key is unique, and the values can be of any data type. Dictionaries are unordered and mutable, meaning you can change, add, or remove elements after the dictionary is created.

# Key Characteristics:
# Unordered: The items do not have a defined order.
# Mutable: The items can be changed or updated.
# Indexed by Keys: Each item is accessed using its key.
# Unique Keys: No duplicate keys are allowed.

# Creating a dictionary with key-value pairs
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science"
}

# Accessing value using key
print(student["name"])  # Output: John Doe

# Using the get() method (returns None if key is not found)
print(student.get("age"))  # Output: 20



# Adding a new key-value pair
student["grade"] = "A"
print(student)  # Output: {'name': 'John Doe', 'age': 20, 'major': 'Computer Science', 'grade': 'A'}

# Updating an existing value
student["age"] = 21
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'major': 'Computer Science', 'grade': 'A'}


# Removing an item using pop()
student.pop("major")
print(student)  # Output: {'name': 'John Doe', 'age': 21, 'grade': 'A'}

# Removing the last inserted item using popitem()
student.popitem()
print(student)  # Output: {'name': 'John Doe', 'age': 21}

# Removing an item using del keyword
del student["age"]
print(student)  # Output: {'name': 'John Doe'}

# Removing all items using clear()
student.clear()
print(student)  # Output: {}



student = {"name": "John", "age": 20, "major": "Computer Science"}

# Loop through keys
for key in student:
    print(key)  # Output: name, age, major

# Loop through values
for value in student.values():
    print(value)  # Output: John, 20, Computer Science

# Loop through key-value pairs
for key, value in student.items():
    print(f"{key}: {value}")  
    # Output:
    # name: John
    # age: 20
    # major: Computer Science

