#Task 1: Identify the Greatest Write a Python program that asks the user to enter three numbers. Your code should then identify and print out the largest number among the three.

def maximum(a, b, c):

    if (a > b) and (a > c): 
        largest = a 

    elif (b > a) and (b > c): 
        largest = b 
    else: 
        largest = c 

    return largest

a = 4
b = 8
c = 15 
print(maximum(a, b, c))

#Task 2: Identify the Smallest Improve upon your code from Task 1 to also determine the smallest number among the three and print it out.

def maximum(a, b, c):

    if (a < b) and (a < c): 
        smallest = a 

    elif (b < a) and (b < c): 
        smallest = b 
    else: 
        smallest = c 

    return smallest

a = 4
b = 8
c = 15 
print(maximum(a, b, c))