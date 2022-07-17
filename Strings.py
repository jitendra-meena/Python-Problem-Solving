# Program to reverse word of String 



str = "geeks quiz practice code"

str_list = str.split()

print(str_list)

for str in range(len(str_list)):
    print(str)


# Program to count Upper case and lower Case 

string= 'PythonMeena'
u_c = 0
l_c =0

for i in string:
    if i.isupper():
        u_c = u_c+1
    else:
        l_c = l_c+1

print(u_c,l_c)


# Reverse String in Python......


string = "Python Developer"

revv = string[::-1]

rev = ''.join(reversed(string))

print(rev,'/n',revv)

str =""

for i in string:
    str = i+str
print(str)    


#Python Program to Remove Odd Indexed Characters in a string
string=raw_input("Enter string:")
new = ""
for s in range(len(string)):
    if i%2==0:
        new = new+string[i]
 print(new)       
