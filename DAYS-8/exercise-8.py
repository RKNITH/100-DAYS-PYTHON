#  LOVE CALCULATOR

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

# 2. Then check for the number of times the letters in the word LOVE occurs.   

# 3. Then combine these numbers to make a 2 digit number and print it out.


def calculate_love_score(name1, name2):
    # Combine both names into a single string
    combined_names = (name1 + name2).lower()

    # Calculate the number of times the letters in "TRUE" occur
    true_count = combined_names.count('t') + combined_names.count('r') + combined_names.count('u') + combined_names.count('e')

    # Calculate the number of times the letters in "LOVE" occur
    love_count = combined_names.count('l') + combined_names.count('o') + combined_names.count('v') + combined_names.count('e')

    # Create a two-digit number based on these counts
    love_score = int(str(true_count) + str(love_count))

    print(f"Love Score = {love_score}")
    return love_score

# Example usage:
calculate_love_score("Kanye West", "Kim Kardashian")  # Output: 42

