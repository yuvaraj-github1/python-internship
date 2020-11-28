"""
1.	Write a program to create a list of n integer values
"""
def list(r1,r2):
    if(r1==r2):
        return r1
    else:
        res=[]#create empty list
        while(r1<=r2):
            res.append(r1)
            r1=r1+1
        return res
r1=int(input("Enter the value of range1: "))
r2=int(input("Enter the value of range2: "))
list=list(r1,r2)
print(list)
#•	Add an item in to the list (using function)
def append(n):
    list.append(n)
n=int(input("entet the number to add: "))
append(n)
print(list)
#•	Delete (using function)
def delete(x):
    if x in list:
        list.remove(x)
    else:
        print("item not in list!!")
x=int(input("Enter the item to be deleted: "))
delete(x)
print(list)
#•	Store the largest number from the list to a variable
a=max(list)
print("maximum number in list:",+a)
#•	Store the Smallest number from the list to a variable
b=min(list)
print ("minimun number in list:",+b)


