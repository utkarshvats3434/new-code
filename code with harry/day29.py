#docstrings in python 
#
#pep 8 python code ko kaise likhte hai python enhancement proposal 
def square(n):
    '''this function returns the square of a number'''
    print(n**2)
square(int(input("enter a number: ")))
print(square.__doc__)

