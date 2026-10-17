# Sets & Companies setup from Day 7 Exercises
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

print("--- Initial it_companies set ---")
print(it_companies)
print()

# 1. Find the length of the set it_companies
print("1. Length of it_companies:")
print(len(it_companies))
print()

# 2. Add 'Twitter' to it_companies
it_companies.add('Twitter')
print("2. After adding 'Twitter':")
print(it_companies)
print()

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Tesla', 'Adobe'])
print("3. After inserting multiple IT companies:")
print(it_companies)
print()

# 4. Remove one of the companies from the set it_companies
it_companies.remove('Oracle')
print("4. After removing 'Oracle':")
print(it_companies)
print()

# 5. What is the difference between remove and discard?
print("5. Difference between remove() and discard():")
print("- remove(): Removes an item from the set. If the item does not exist, it raises a KeyError.")
print("- discard(): Removes an item from the set. If the item does not exist, it does NOT raise an error (the set remains unchanged).")