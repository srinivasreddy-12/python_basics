s = {1,2,3,3,46,7,8,9}
print(s)

#adding a value to set
s.add(100)
print(s)

#removing a value from set
s.remove(3)
print(s)

#removing a random value
s.pop()
print(s)

#making a set to emty set
s.clear()
print(s)

set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

#union (all)
print(set1.union(set2))

#intersection
print(set1.intersection(set2))