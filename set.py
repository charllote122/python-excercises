set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)              
print("Intersection:", set1 & set2) # common elements      
print("Difference:", set1 - set2) # se present in set1 but not in set2
print("Difference (set2 - set1):", set2 - set1) # elements in set2 but not in set1       
print("Symmetric Difference:", set1 ^ set2)   # elements that are in either set1 or set2 but not in both
print("Is set1 a subset of set2?", set1.issubset(set2))  # check if all elements of set1 are in set2
print("Is set1 a superset of set2?", set1.issuperset(set2))  