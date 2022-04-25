

#    @@@ WELLCOME TO LIST PROGRAM @@@@@@


# List Append indexing ,slicing, iterarting.....

List =  [1,2,6,3,4]

for i in List:
    print(i)
List.append(12)
List[0]=121
print(List) 

List.pop()

l1 = [1,2,23,3,9]

l1 = [i for i in l1 if i>2]
print(l1)
print(List)

fruits = ["apple", "banana", "cbherry", "kiwi", "mango"]


l1 = [f for f in fruits if 'b' in f]

print(l1)