"""
Create a tuple and print the reverse of the created tuple
"""
t1=("temple","scary house",2.5,8,"kids")
print("main tuple: ")
print(t1)
def rev(t1):
    t2=t1[::-1]
    return t2
t2=rev(t1)
print("Reversed tuple: ")
print(t2)
"""
Create a tuple and convert tuple into list
"""
tup = [(1, 2), (3, 4), (5, 6)]
out = list(sum(tup, ()))
print(out)