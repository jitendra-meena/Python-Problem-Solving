
"""
Python Basic Programs 2023 by Code with Jeet

"""

# Python Program to Reverse a Number


n = int(input("Enter a Numbers :-"))
r = 0
while(n>0):
    d = n%10
    r = r*10+d
    n = n//10
print(r) 

# Python Program to Find Sum of Digits of a Number

n = int(input("Enter a Numbers :-"))
r = 0
total = 0
while(n>0):
    d = n%10
    r = r*10+d
    n = n//10
    total +=d
print(total)


# Python Program to Count the Number of Digits in a Number


n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)
    
# Generator in Python 
'''
A generator function is a special type of function in Python that returns a generator object.
 A generator is an iterable object that generates values one at a time,
 instead of generating a list with all values at once.

'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci_generator()
for i in range(10):
    print(next(fib))
'''
Output:
Copy code
0
1
1
2
3
5
8
13
21
34
'''
'''
In this example, the fibonacci_generator function returns a generator that generates the Fibonacci sequence.
The generator is assigned to the variable fib, and we can iterate over it using the for loop or the next function. 
The function is executed each time we call next(fib), and it stops when it encounters the end of the function.
'''




