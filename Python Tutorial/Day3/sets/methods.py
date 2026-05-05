# methods of set

s={1,2,3,4,5,4}

# s.add() -> adds a value
s.add(100)
print(s)

# s.remove(val) -> removes a val
s.remove(2)
print(s) 

# s.clear()-> empties the set
# s.clear()
# print(s)

# s.pop() -> removes a random val
s.pop()
print(s)

# s.union(set2) -> returns new union
set1 = {1,2,3,4,5}
set2 = {2,3,4,5,6}

union1 = set1.union(set2)
print(union1)

# s.intersection(set2)

intersect = set1.intersection(set2)
print(intersect)