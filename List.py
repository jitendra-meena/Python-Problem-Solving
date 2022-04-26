

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

list = [1,2,[54,33],[12,33333]]
list1 =[]
for i in list:
    if type(i)=='list':
        for j in list:
            list1.append(j)
    else:
        print(type(i))
        list1.append(i)        
print(list1)


