#Dictionary
d1={"sam":"chay","deepika":"ranveer"}
print(d1)
"""
1)	Write a Python script to merge two Python dictionaries
"""
d2={"nagarjuna":"amala","single":"salman"}
print(d2)
d=d1.copy()
d.update(d2)
print(d)
"""
2)	Write a Python program to remove a key from a dictionary
"""
del d["single"]
print(d)
"""
3)	Write a Python program to map two lists into a dictionary
"""
list1=("banana","apple","orange")
list2=("banana juice","apple juice","orange juice")
d3=dict(zip(list1,list2))
print(d3)
"""
4)	Write a Python program to find the length of a set
"""
set={"web series","movies","daily serials","entertainment programs"}
print(len(set))
"""
5)	Write a Python program to remove the intersection of a 2nd set from the 1st set
"""
#using difference_update()
s1={"dog","cat","cow","bull","cock"}
s2={"cat","bull","fox","goat"}
s1.difference_update(s2)
print(s1)
#using operator
s11={"yuvaraj","ramesh","sandhya","sai"}
s22={"sandhya","saila","shobha"}
print(s11-s22)