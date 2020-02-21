# -*- coding: utf-8 -*-

# Fibonacci Sequence

def Fibonacci_Sequence(n):
    # Raise a type error if the value is not an integer
    if type(n) != int:
        raise TypeError('Please input a real non-negative integer.')
    # Raise a type error if the value is less than or equal to 0
    elif n < 0:
        raise TypeError('Please input a non-negative integer greater than 0.')
    # Return 0 or 1 if the number placed in the function is 0 or 1 respectively
    elif n <= 1:
        print(f"This Fibonacci sequence has {n} element:")
        print(n)
    # Return the fibonacci sequence with the number specified
    else:
        x = 0
        y = 1
        iteration = 0
        print(f"This Fibonacci sequence has {n} elements:")
        while iteration < n:
            print(y, end=', ')
            z = x + y
            x = y
            y = z
            iteration += 1

#------------------------------------------------------------------
# Testing the Fibonacci Sequence:

# Fibonacci_Sequence(10)
# Fibonacci_Sequence(-1)
# Fibonacci_Sequence('number')
# Fibonacci_Sequence(5j-2)
# Fibonacci_Sequence(2.5)
