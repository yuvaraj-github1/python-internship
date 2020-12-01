"""
•	Write a program to loop through a list of numbers and add +2 to every value to elements in list
"""
mylist=[0,5,6,7,6,8,2]
mylist=list(map(lambda x:x+2,mylist))#return list by adding 2
print("mylist =",mylist)
for i in mylist:#loop that prints values by adding 2
    print(i+2)

"""
•	Write a program to get the below pattern
54321
4321
321
21
1
"""
num=int(input("enter the number"))
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print(j,end='')
    print()

"""
•	Python Program to Print the Fibonacci sequence
"""

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1

"""
•	Explain Armstrong number and
write a code with a function

"""
num = int(input('Enter a number: '))
num_original =num2=num
sum1 = 0
cnt=0

while(num>0):
	cnt=cnt+1
	num=num//10

while num2>0:
   rem = num2% 10
   sum1 += rem ** cnt
   num2//= 10


if(num_original==sum1):
    print('Armstrong!!')
else:
    print('Not Armstrong!')

"""

1•	Write a program to print the multiplication table of 9
"""
num = int(input("Show the multiplication table of? "))
# using for loop to iterate multiplication 10 times
for i in range(1,11):
   print(num,'x',i,'=',num*i)

"""
•	Check if a program is negative or positive
"""
num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

"""
•	Write a program to convert the number of days to ages
"""
days= int(input("enter the number of days:"))
years= days / 365
print("Number of years is: ");
print(years);

"""
•	Solve Trigonometry problem using math
 function write a program to solve us-ing math function

"""
import math

a = math.pi / 6

# returning the value of sine of pi/6
print("The value of sine of pi/6 is : ", end="")
print(math.sin(a))

# returning the value of cosine of pi/6
print("The value of cosine of pi/6 is : ", end="")
print(math.cos(a))

b = 3
c = 4

# returning the value of tangent of pi/6
print("The value of tangent of pi/6 is : ", end="")
print(math.tan(a))

# returning the value of hypotenuse of 3 and 4
print("The value of hypotenuse of 3 and 4 is : ", end="")
print(math.hypot(b, c))

"""
•	Create a calculator only on a code level by
 using if condition (Basic arithmetic calculation)
"""
print("Calculator")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")

# input choice
ch=int(input("Enter Choice(1-4): "))

if ch==1:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a+b
    print("Sum = ",c)
elif ch==2:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a-b
    print("Difference = ",c)
elif  ch==3:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a*b
    print("Product = ",c)
elif ch==4:
    a=int(input("Enter A:"))
    b=int(input("Enter B:"))
    c=a/b
    print("Quotient = ",c)
else:
    print("Invalid Choice")