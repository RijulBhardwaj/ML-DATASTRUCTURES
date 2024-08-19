print("Hello World")
# Lists
print("### Lists ###")
my_list = [1, 2, 3, 4, 5]
print("Original List:", my_list)
my_list.append(6)
print("After append:", my_list)
my_list.extend([7, 8])
print("After extend:", my_list)
my_list.insert(0, 0)
print("After insert:", my_list)
my_list.remove(8)
print("After remove:", my_list)
popped = my_list.pop()
print("After pop:", my_list, "- Popped element:", popped)
index = my_list.index(4)
print("Index of 4:", index)
count = my_list.count(2)
print("Count of 2:", count)
my_list.sort()
print("After sort:", my_list)
my_list.reverse()
print("After reverse:", my_list)
print("Slicing [1:4]:", my_list[1:4])

# Tuples
print("\n### Tuples ###")
my_tuple = (1, 2, 3, 4, 5)
print("Original Tuple:", my_tuple)
index = my_tuple.index(3)
print("Index of 3:", index)
count = my_tuple.count(2)
print("Count of 2:", count)

# Sets
print("\n### Sets ###")
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)
my_set.add(6)
print("After add:", my_set)
my_set.update([7, 8])
print("After update:", my_set)
my_set.remove(8)
print("After remove:", my_set)
popped = my_set.pop()
print("After pop:", my_set, "- Popped element:", popped)
my_set.discard(2)
print("After discard:", my_set)
print("Union with {4, 5, 6}:", my_set.union({4, 5, 6}))
print("Intersection with {4, 5, 6}:", my_set.intersection({4, 5, 6}))
print("Difference with {4, 5, 6}:", my_set.difference({4, 5, 6}))
print("Symmetric difference with {4, 5, 6}:", my_set.symmetric_difference({4, 5, 6}))

# Dictionaries
print("\n### Dictionaries ###")

import pandas as pd
import seaborn as sns
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("Original Dictionary:", my_dict)
my_dict['d'] = 4
print("After adding key 'd':", my_dict)
value = my_dict.pop('b')
print("After pop 'b':", my_dict, "- Popped value:", value)
keys = my_dict.keys()
print("Keys:", keys)
values = my_dict.values()
print("Values:", values)
items = my_dict.items()
print("Items:", items)
value = my_dict.get('a')
print("Get value for key 'a':", value)
my_dict.update({'e': 5, 'f': 6})
print("After update:", my_dict)
default_value = my_dict.setdefault('g', 7)
print("After setdefault for 'g':", my_dict, "- Default value:", default_value)
print("Check if 'h' in dictionary:", 'h' in my_dict)
print("Check if 'a' in dictionary:", 'a' in my_dict)

# Strings
print("\n### Strings ###")
my_string = "Hello, World!"
print("Original String:", my_string)
print("Lowercase:", my_string.lower())
print("Uppercase:", my_string.upper())
print("Title case:", my_string.title())
print("Split:", my_string.split(", "))
print("Join:", " ".join(['Hello', 'World']))
print("Replace:", my_string.replace("World", "there"))
print("Find 'World':", my_string.find("World"))
print("Count 'l':", my_string.count('l'))
print("Check if starts with 'Hello':", my_string.startswith("Hello"))
print("Check if ends with '!':", my_string.endswith("!"))

# Ranges
print("\n### Ranges ###")
my_range = range(1, 10, 2)
print("Original Range:", list(my_range))
print("Check if 3 in range:", 3 in my_range)
print("Check if 4 in range:", 4 in my_range)

# Bytes
print("\n### Bytes ###")
my_bytes = b"Hello, World!"
print("Original Bytes:", my_bytes)
print("Decode:", my_bytes.decode('utf-8'))
my_bytes_from_hex = bytes.fromhex('48656c6c6f2c20576f726c6421')
print("Bytes from hex:", my_bytes_from_hex)
print("Hex representation:", my_bytes.hex())

# Bytearrays
print("\n### Bytearrays ###")
my_bytearray = bytearray(b"Hello, World!")
print("Original Bytearray:", my_bytearray)
my_bytearray[0] = ord('h')
print("After modifying first element:", my_bytearray)
my_bytearray.extend(b"!!!")
print("After extend:", my_bytearray)
print("Decode:", my_bytearray.decode('utf-8'))

# Frozensets
print("\n### Frozensets ###")
my_frozenset = frozenset([1, 2, 3, 4, 5])
print("Original Frozenset:", my_frozenset)
print("Check if 3 in frozenset:", 3 in my_frozenset)
print("Union with frozenset({4, 5, 6}):", my_frozenset.union(frozenset({4, 5, 6})))
print("Intersection with frozenset({4, 5, 6}):", my_frozenset.intersection(frozenset({4, 5, 6})))
print("Difference with frozenset({4, 5, 6}):", my_frozenset.difference(frozenset({4, 5, 6})))
print("Symmetric difference with frozenset({4, 5, 6}):", my_frozenset.symmetric_difference(frozenset({4, 5, 6})))
