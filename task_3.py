import math


def get_sum_of_digits(number: int):
    """ Return sum of the digits in given number """
    summa = 0
    for i in str(number):  # Looping through converted to a string number
        summa += int(i)  # Summarized each number converted to int
    return summa


# Get factorial 100
factorial_100 = math.factorial(100)

# Get sum of the digits in variable factorial_100
get_sum_of_digits(factorial_100)
