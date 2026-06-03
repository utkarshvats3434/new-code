#dictionaries 
# a dictionary is a collection of key value pairs
# the keys are unique and the values can be of any data type
# dictionaries are mutable and unordered
d = {'name': 'John', 'age': 30, 'city': 'New York'}
print(d)
print(d['name'])
print(d.get('age'))
d['age'] = 31
print(d)
d['country'] = 'USA'
print(d)
del d['city']
print(d)
print(d.keys())
print(d.values())
print(d.items())    