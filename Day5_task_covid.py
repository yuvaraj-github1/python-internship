"""
Create a function covid( ) & it should accept patient name,
and body temperature,
by default the body temperature should be 98 degree
"""
def covid(pname, temp):
    if(temp==98):
        print("you don't have any symtoms of covid,stay safe")
    else:
        print("you have covid symtoms,go to quarintine for 14 day")
pname=str(input("Enter the patient name:"))
temp=int(input("enter the recorded temp: "))
covid(pname, temp)