#if else statement 
num = int(input("enter the value:"))
if num < 0:
    print("the number is negative")
elif num == 0:
    print("the number is zero")
elif num == 999:    
    print("the number is special")
else:
    print("the number is positive")
    print("i am happy now")  
#nested if else statement
num = int(input("enter the value:"))
if (num < 0):
    print("the number is negative")
elif (num > 0):
    if (num <= 10):
        print("the number is between 1 and 10")
    elif (num > 10 and num <= 100):
        print("the number is between 11 and 100")        
else:
    print("the number is positive")