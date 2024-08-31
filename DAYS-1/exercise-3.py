# We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. Write 3 lines of code to switch the contents of the variables. You are not allowed to type the words "milk" or "juice". You are only allowed to use variables to solve this exercise.


glass1 = "milk"
glass2 = "juice"

# method-1

a = glass1
glass1 =glass2
glass2=a

print(glass1)
print(glass2)

# method 2:
# Swap using tuple packing/unpacking
glass1, glass2 = glass2, glass1

print("glass1 =", glass1)  # Output: glass1 = juice
print("glass2 =", glass2)  # Output: glass2 = milk



#  METHODS 3:


# Swap without using a temporary variable
glass1 = glass1 + glass2
glass2 = glass1[:len(glass1)-len(glass2)]
glass1 = glass1[len(glass2):]

print("glass1 =", glass1)  # Output: glass1 = juice
print("glass2 =", glass2)  # Output: glass2 = milk