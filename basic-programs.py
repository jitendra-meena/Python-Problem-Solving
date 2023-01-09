
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
    
