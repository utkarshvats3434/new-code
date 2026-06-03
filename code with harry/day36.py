# #exception handling is the process of handling errors that may occur during the execution of a program. It allows you to gracefully handle errors and prevent your program from crashing.
# a = input("Enter a number: ")
# print(f"Multiplication table of {a} is : ")
# try:
#  for i in range(1, 11):
#         print(f"{int(a)} x {i} = {int(a)*i}")
# except: #as same as except Exception as e: but it is more specific to handle only ValueError
#     print("Apne kuch galti kii hai code likhne mein ")

# print("Some lines of code after the error")    
# print("end of the program")    
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("invalid integer")
except IndexError:
    print("index error")
except Exception as e:
    print(f"An error occurred: {e}")    