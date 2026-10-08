# 1. Creating tuples
fruits = ("apple", "banana", "cherry")
single_item_tuple = ("orange",)  # Note the trailing comma for single items

# 2. Accessing elements (indexed starting at 0)
print("First fruit:", fruits[0])  # Output: apple
print("Last fruit:", fruits[-1])  # Output: cherry

# 3. Tuple Unpacking
a, b, c = fruits
print(f"Unpacked: a={a}, b={b}, c={c}")

# 4. Immutability (This will raise a TypeError if uncommented)
# fruits[0] = "mango"  # Error! Tuples cannot be modified after creation

# 5. Common operations
print("Length of tuple:", len(fruits))
print("Is 'banana' in fruits?", "banana" in fruits)

# 6. Returning multiple values from a function using tuples
def get_dimensions():
    width = 1920
    height = 1080
    return width, height  # Implicitly returns a tuple (width, height)


w, h = get_dimensions()
print(f"Dimensions: {w}x{h}")