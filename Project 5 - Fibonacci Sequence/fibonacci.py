# -*- coding: utf-8 -*-

# Fibonacci Sequence

def Fibonacci_Sequence(n):
    if type(n) not in (int):
        raise TypeError('Please input a non-negative number')
    elif n <= 0:
        raise TypeError('Please input a non-negative number')
    elif n == 1:
        print("This Fibonacci sequence has {} element.".format(length), ":")
        print(x)
    else:
        x = 0
        y = 1
        iteration = 0
        print("This Fibonacci sequence has {} element.".format(length), ":")
        while iteration < n:
            print(x, end=', ')
            z = x + y
            x = y
            y = z
            iteration += 1
            

# Testing the Fibonacci Sequence
Fibonacci_Sequence(5)
Fibonacci_Sequence(-1)
Fibonacci_Sequence('number')

# The length of our Fibonacci sequence
length = 10

# The first two values
x = 0
y = 1
iteration = 0

# Condition to check if the length has a valid input
if length <= 0:
   print("Please provide a number greater than zero")
elif length == 1:
   print("This Fibonacci sequence has {} element".format(length), ":")
   print(x)
else:
   print("This Fibonacci sequence has {} elements".format(length), ":")
   while iteration < length:
       print(x, end=', ')
       z = x + y
       # Modify values
       x = y
       y = z
       iteration += 1