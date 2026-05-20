from tkinter.font import names


marks= [1, 2, 3, 4, 5]
# print(marks)
# print(type(marks))
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[len(marks)-1]) 

if 67 in marks:
    print("67 is present in the list")
else:
    print("67 is not present in the list")
# print(marks[0:3])
# print(marks[1:4])
# print(marks[0:3])
print(marks[0:3:2]) #jump index 


#list comprehension
lst = [i for i in range(7)]
print(lst)