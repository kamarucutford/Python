# LIST

import random

# # Created a list of 5 random numbers
random_numbers = [random.randint(1, 100) for _ in range(5)]
print("Original List:", random_numbers)

# # Inserted 3 new values into the list
random_numbers.append(10)
random_numbers.append(20)
random_numbers.append(30)
#
print("Updated List:", random_numbers)

# # Using a for loop to print each element in the list
print("List elements:")
for num in random_numbers:
    print(num)

# DICTIONARY

# # Created a dictionary
person = {
    'name': 'Krishna',
    'age': 25,
    'address': 'Kerala'
}

print("Dictionary:", person)

# # Added a new key-value pair to the dictionary
person['phone'] = '8569541278'

print("Updated Dictionary:", person)

SET
Created a set
my_set = {1, 2, 3, 4, 5}

print("Original Set:", my_set)

# Added the value 6 to the set
my_set.add(6)

print("Updated Set:", my_set)

# Removed the value 3 from the set
my_set.remove(3)

print("Set after removal:", my_set)

# TUPLE

# Created a tuple
my_tuple = (1, 2, 3, 4)

print("Tuple:", my_tuple)

# Printing the length of the tuple
print("Length of the tuple:", len(my_tuple))
