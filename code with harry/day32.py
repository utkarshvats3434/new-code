s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
print(s1.union(s2)) #union of two sets
print(s1.update(s2)) #union of two sets
print(s1.intersection(s2)) #intersection of two sets
print(s1.difference(s2)) #difference of two sets
print(s1.difference_update(s2)) #difference of two sets
print(s1.symmetric_difference(s2)) #symmetric difference of two sets    
cities1= {"Delhi", "Mumbai", "Bangalore", "Chennai"}
cities2 = {"Uttarakhand", "Kolkata"}
print(cities1.issuperset(cities2))
cities3 = {"Delhi", "Bangkok", "Bihar Sharif"}
print(cities1.issuperset(cities3))
print(cities3.issubset(cities1))