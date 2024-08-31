#  RANDOM MODULE

import random
a =random.randint(1, 100)
print(a)

b= random.uniform(1, 100)
print(b)

c =random.random()
print(c)


# LIST IN PYTHON: A DATASTRUCTURE IN PYTHON: []

# list_operations.py

# Initialize the list
my_list = []

# Append elements
my_list.append(2)
print("After append(2):", my_list)

my_list.append(3)
print("After append(3):", my_list)

# Extend the list with another iterable
my_list.extend([4, 5])
print("After extend([4, 5]):", my_list)

# Insert element at a specified position
my_list.insert(1, 1)
print("After insert(1, 1):", my_list)

# Remove the first occurrence of a specified value
my_list.remove(1)
print("After remove(1):", my_list)

# Pop an element by index
removed_element = my_list.pop(2)
print("After pop(2):", my_list)
print("Removed element:", removed_element)

# Pop the last element
last_element = my_list.pop()
print("After pop():", my_list)
print("Last element removed:", last_element)

# Clear all elements from the list
my_list.clear()
print("After clear():", my_list)

# Initialize list again for further operations
my_list = [2, 3, 4, 3, 5]

# Find the index of the first occurrence of a specified value
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)

# Count occurrences of a specified value
count_of_3 = my_list.count(3)
print("Count of 3:", count_of_3)

# Sort the list in ascending order
my_list.sort()
print("After sort():", my_list)

# Sort the list in descending order
my_list.sort(reverse=True)
print("After sort(reverse=True):", my_list)

# Reverse the list
my_list.reverse()
print("After reverse():", my_list)

# Copy the list
new_list = my_list.copy()
print("Copy of the list:", new_list)

# Get the length of the list
length_of_list = len(my_list)
print("Length of the list:", length_of_list)

# Get the maximum value in the list
max_value = max(my_list)
print("Maximum value:", max_value)

# Get the minimum value in the list
min_value = min(my_list)
print("Minimum value:", min_value)

# Get the sum of all elements in the list
total = sum(my_list)
print("Sum of elements:", total)

# Slice the list to create a sublist
sublist = my_list[1:4]
print("Sliced list [1:4]:", sublist)

# Join elements of a list of strings into a single string
string_list = ['Hello', 'World']
joined_string = ' '.join(string_list)
print("Joined string:", joined_string)

