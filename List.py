

#    @@@ WELLCOME TO LIST PROGRAM @@@@@@


# List Append indexing ,slicing, iterarting.....

from enum import unique


List =  [1,2,6,3,4]

for i in List:
    print(i)
List.append(12)
List[0]=121
print(List) 

List.pop()

l1 = [1,2,23,3,9]

l1 = [i for i in l1 if i>2]

fruits = ["apple", "banana", "cbherry", "kiwi", "mango"]


l6 = [f for f in fruits if 'b' in f]  # List Comperiehence
l1.sort() # Sort List 
print(l1)

list = [9,2,33,11,22,33,2]

list.sort(reverse=True) # SOrt Decending Orders

list.reverse()
list.extend(l1)  # Extends Elements From One List to Another one
print(list)


# Remove Duplicate Elements From List:

list = [1,2,3,2,3,1,2,4,22,121]
unique_list = []
for i in list:
    if i not in unique_list:
        unique_list.append(i)
print(list)
print(unique_list)



# Program To Sort List Elements Without using Sort functions

list_data = [122,11,3434,21,656,8,3223,2]
l =len(list_data)

for i in range(l-1):
    for j in range(l-i-1):
        if list_data[j]>list_data[j+1]:
            list_data[j],list_data[j+1] = list_data[j+1],list_data[j]
print(list_data,"Sort List Data")            


# Program to search elements in list 

list_data = [122,11,3434,21,656,8,3223,2]

s = 11

for i in list_data:
    if s in list_data:
        print("Yes Elements Presents---")
    else:
        print("Not Present Elements")



# Program To Find Largest Numbers in List

list = [122,11,3434,21,656,8,3223,2]
max =list[0]
min=list[0]
for i in list:
    if i>max:
        max = i
    elif i<min:
        min = i    
print(max,min)    

# List Comperihence Program 
# Python code to flat a nested list with
# multiple levels of nesting allowed.

# input list
l = [1, 2, [3, 4, [5, 6]], 7, 8, [9, [10]]]

# output list
output = []

def reemovNestings(l):
	for i in l:
		if type(i) == list:
			reemovNestings(i)
		else:
			output.append(i)

# Driver code 
print ('The original list: ', l)
reemovNestings(l)
print ('The list after removing nesting: ', output)

 
   
l1 = [1,2,4]
#124
x = "".join(map(str,l1))
print(x)


data,data2 = [12,6],[9,7]
#[12,6,9,7]
data[-1:]=data2

print(data)



def vedik(a,b):
    if (a < 10 or a > 99):
        print("Invalid Input!")
    else:
        f,l = a // 10,a % 10
        s = f+l
        c = [f,s,l]
        f = ''.join(str(c) for c in c)
        print(f)


A = int(input("Enter A--"))
B = int(input("Enter B--"))
vedik(A,B)

def mul(a,b):
    c =a*b
    print(c)

A = int(input("Enter A--"))
B = int(input("Enter B--"))
mul(A,B)



# Program to show Element count String
st = "MeenaJitu"
l = len(st)
c = 1
new = ''
for i in range(l-1):
    if st[i]==st[i+1]:
        c =c+1
    else:    
        new = new +st[i]+str(c)
print(st)
print(new)

#Python program to implement matrix addition

X = [[8,5,1],
[9 ,3,2],
[4 ,6,3]]
Y = [[8,5,3],
[9,5,7],
[9,4,1]]
result = [[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(X)):
    for j in range(len(Y)):
        result[i][j]=X[i][j]+Y[i][j]
for k in result:
    print(k)



#Python program to find second largest number in a list

list1 = [10, 20, 4, 45, 99]

list2 = list(set(list2))

list2.sort()
print("Second largest element is:", list2[-2])


# Python Program to Return the Length of the Longest Word from the List of Words

max = len(a[0])
temp = a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)


# Check if a pair exists with given sum in given List
def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        for i in range(0,l):
            for j in range(i+1,l):
                if(nums[i]+nums[j]==target):
                    return [i,j]

nums = [1,3,4]
target = 5
twoSum(nums,target)

	
		

