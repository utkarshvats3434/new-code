#f strings in python
letter = "my name is {} and i am from {}"
country = "india"
name = "utkarsh"
print(letter.format(country,name))
print(f"my name is {{name}} and i am from {country}")
price = 49.99
txt = "the price of the item is {}"
#print(txt.format(price))
print(f"the price of the item is {price:.2f}")
# print(txt)