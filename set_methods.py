set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7}

#difference: Returns elements in set_a that are not in set_b
# It does not modify set_a

diff_result = set_a.difference(set_b)
print("1. difference():", diff_result)      
print("   set_a after difference():", set_a)  

# DIFFERENCE_UPDATE: Removes items found in set_b from set_a
set_a_copy = set_a.copy()  # Copy to preserve original set_a
set_a_copy.difference_update(set_b)
print("2. difference_update():", set_a_copy)  
print("   set_a_copy after difference_update():", set_a_copy)  


# SYMMETRIC DIFFERENCE

# Returns elements in either set, but not both
sym_diff = set_a.symmetric_difference(set_b)
print("3. symmetric_difference():", sym_diff)  
print("   set_a after symmetric_difference():", set_a)  

# SYMMETRIC_DIFFERENCE_UPDATE: Updates set_a with symmetric difference
set_a_sym = set_a.copy()  
set_a_sym.symmetric_difference_update(set_b)
print("4. symmetric_difference_update():", set_a_sym)  
print("   set_a_sym after symmetric_difference_update():", set_a_sym)  
