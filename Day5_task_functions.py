"""
1)Create a function getting two integer inputs from user. & print the following:

Addition of two numbers is +value
Subtraction of two numbers is +value
Division of two numbers is +value
Multiplication of two numbers is +value


"""
def user(a,b):
    print("Addition of two numbers is ",a+b)
    print("Subtraction of two numbers is ",a-b)
    print("Division of two numbers is ",a/b)
    print("Multiplication of two numbers is ",a*b)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
user(a,b)

