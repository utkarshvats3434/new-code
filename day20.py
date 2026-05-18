def calculateGmean(a , b):
    mean = (a * b)/(a + b)
    print(mean)

def isGreater(a , b):
    if(a > b):
        print("a is greater than b")
    else:
        print("b is greater than a")

def isLesser(a , b):
    pass

a = int(input("enter a a1: "))
b = int(input("enter b1: "))
isGreater(a , b)
calculateGmean(a , b)
# gmean1 = (a * b)/(a + b)
# print(gmean1)

c = int(input("enter a a2: "))
d = int(input("enter b2: "))
isGreater(c , d)
calculateGmean(c , d)
# gmean2 = (c * d)/(c + d)
# print(gmean2)