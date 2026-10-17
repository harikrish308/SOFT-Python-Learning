# Sets setup from Day 7 Exercises - Level 2
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print("--- Initial Sets ---")
print("Set A:", A)
print("Set B:", B)
print()

# 1. Join A and B (Union)
# You can use the union() method or the pipe operator (|)
join_ab = A.union(B)
print("1. Join A and B (Union):")
print(join_ab)
print()

# 2. Find A intersection B
# You can use the intersection() method or the ampersand operator (&)
intersection_ab = A.intersection(B)
print("2. A intersection B:")
print(intersection_ab)
print()

# 3. Is A subset of B?
# Use the issubset() method
is_subset = A.issubset(B)
print("3. Is A a subset of B?:")
print(is_subset)
print()

# 4. Are A and B disjoint sets?
# Use the isdisjoint() method
are_disjoint = A.isdisjoint(B)
print("4. Are A and B disjoint sets?:")
print(are_disjoint)
print()

# 5. Join A with B and B with A
# Joining A with B is the same as joining B with A (Union is commutative)
join_a_with_b = A.union(B)
join_b_with_a = B.union(A)
print("5. Join A with B and B with A:")
print("A joined with B:", join_a_with_b)
print("B joined with A:", join_b_with_a)
print()

# 6. What is the symmetric difference between A and B?
# Use the symmetric_difference() method or the caret operator (^)
sym_diff = A.symmetric_difference(B)
print("6. Symmetric difference between A and B:")
print(sym_diff)
print()

# 7. Delete the sets completely
# Use the del keyword to delete variables from memory
del A
del B
print("7. Sets A and B have been deleted completely using 'del'.")
# Trying to print A or B after this line would raise a NameError because they no longer exist.