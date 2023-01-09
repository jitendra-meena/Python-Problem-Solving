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
string=input("Enter string:")
new = ""
for s in range(len(string)):
    if i%2==0:
        new = new+string[i]
 print(new)       

#Python Program to Remove the nth Index Character from a Non-Empty String

string  = input("Enter STRT-")
index = int(input("Enter Index-"))
print(string[:index]+string[index+1:])


# Python Program to Calculate the Length of a String Without using Library Functions


string = "Jitendra"
c = 0
for s in string:
    c = c+1
print(c)    

# Python Program to Count the Number of Words and Characters in a String

string = "Jitendra Meena Python Developer"
w = 1
c = 0

for s in string:
    c = c+1
    if(s==' '):
        w = w+1
print(w,c)        

# Python Program to Count Number of Lowercase Characters in a String

s = "Jitendra"

l = 0
for s in s:
    if(s == s.lower()): # islower()
        l=l+1
print(l) 

# Remove Odd Indexed Characters in a string

string = "Jitendra Meena"
final_str = ""
for st in range(len(string)):
    if st%2==0:
        final_str += string[st]
print(final_str)

# Remove the nth Index Character from a Non-Empty String


string = "Jitendra Meena"
n = int(input("enter numbers:-"))
print(string[:n]+string[n+1:])      

# Python Program to Determine How Many Times a Given Letter Occurs in a String Recursively

# With Count fucntion
ele = input("Enter a Search str:-")
string = input("Enter a String:-")
print(string.count(ele))


# Without Count 
c = 0
for i in range(len(string)):
    if string[i]==ele:
        c+=1
print(c)        
