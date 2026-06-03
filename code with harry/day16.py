#match case statements
from unittest import case


x = int(input("enter the number:"))
match x:
    case 0:
        print("the value of x is zero")
    case 1:
        print("the value of x is one")
    case _ if x!=90:
        print("the value of x is not 90")
    case _ if x!=100:
        print("the value of x is not 100")
    case _:
        print("the value of x is something else")
# from unittest import case
x = int(input("Enter the number: "))
if x == 0:
    print("The value of x is zero")
elif x == 1:
    print("The value of x is one")
elif x != 90 and x != 100:  # Dono conditions ko aap aise combine kar sakte hain
    print("The value of x is neither 90 nor 100")
else:
    print("The value of x is something else")
