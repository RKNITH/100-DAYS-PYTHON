# """Docstrings
# Docstrings are a type of comment used to describe
# what a function, class, or module does. They are defined 
# using triple quotes (""" or ''') and can be accessed
# programmatically through the __doc__ attribute. 
# Docstrings are essential for documentation purposes.
#  """

def add(a, b):
    """
    Add two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# Accessing the docstring
print(add.__doc__)






# This is a multi-line comment
# using hash symbols.
# It describes the following code block.

def multiply(a, b):
    return a * b

# Alternatively, you can use triple quotes,
# but this is more commonly used for docstrings.
"""
This is a multi-line comment using triple quotes.
It's not the conventional way for comments, but it works.
"""

# Usage of the multiply function
result = multiply(3, 5)
print(result)
