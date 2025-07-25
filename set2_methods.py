a = {1, 2, 3}
b = {3, 4, 5}
c = {1, 2}

print("Disjoint:", a.isdisjoint(b))     # Check if sets have no elements in common
print("Is a subset of b?", a.issubset(b))  # Check if all elements of a are in b
print("Is a superset of c?", a.issuperset(c))  # Check if all elements of c are in a
print("Is b a subset of a?", b.issubset(a))  # Check    if all elements of b are in a
print("Is b a superset of c?", b.issuperset(c))  #  Check if all elements of c are in b
print("Is c a subset of a?", c.issubset(a))  # Check if all elements of c are in a       
print("Subset:", c.issubset(a))         
print("Superset:", a.issuperset(c))     

# Clear a set
print("Before clear:", a)
a.clear()
print("After clear:", a)                


del b
# Attempting to access b after deletion will raise an error

print("After delete b:", b)  # This will raise an error since b is deleted
