
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

    
