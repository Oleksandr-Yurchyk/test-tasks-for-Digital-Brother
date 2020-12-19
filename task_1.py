import math


def find_number_of_correct_brackets(n: int):
    """ Return Catalan number if n >= 2 """
    if n >= 2:
        # Calculating Catalan number and return its integer value
        catalan_number = math.factorial(2 * n) // (math.factorial(n) * math.factorial(n + 1))
        return int(catalan_number)
    return 1 if n == 1 else 0


# Get the number from keyboard
inputted_number = int(input())

# Get the number of correct brackets
print(find_number_of_correct_brackets(inputted_number))
