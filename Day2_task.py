"""
1)Create three variables (a,b,c) to same value of any integer & do the following
a)	Divide a by 10
b)	Multiply b by 50
c)	Add c value by 60
"""
a=b=c=int(input())
print(a/10)
print(b*50)
print(c+60)


"""Create a String variable of 5 characters  and replace the 3rd character with G"""
string=str(input())
print(string.replace(string[2],"G"))


"""
Create two values (a,b) of int,float data type & convert the vise versa,
Hint : convert a from int to float datatype & b from float to int datatype 
"""
a=int(input())
print(float(a))
b=float(input())
print(int(b))