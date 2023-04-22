# Python | Sort Python Dictionaries by Key or Value
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15, 'yash': 2, 'suraj': 32}
l = [u for u in d]
l.sort()
c = {i:d[i] for i in l}
print(c)  


# Python program to find the sum of all items in a dictionary

d = {'Jeet': 10, 'rajnish': 9, 'meena': 15, 'yash': 2, 'kp': 32}

print(sum(d.values()))
