'''
Hash tables in python
- Provides data lookup by key rather than by index
- Behaves likes a dictionary (Python) or associative array (PHP)
- Internally uses a flat array
- Static changing - Collisions are handled by creating a linked list where there are multiple matches
- Each index in the internal flat array is referred to as a bucket 
'''


# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value


# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # internal flat array (bucket) where we initialise each element to None
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# ''


# hash method takes key as an argument
def hash(key, max):
    # Initialise hash to 5381
    # 5381 is just a number in testing which results in fewer collisions
    # Why 33? No clue.
    # two impletations for djb2 using either /33 or <<5
    # ref:https://goodmath.scientopia.org/2013/10/20/basic-data-structures-hash-tables/
    hash = 5381
    # loop through each character in key
    for c in key:
        # take the original hash and left shift by 5 and add hash and add character
        hash = ((hash << 5) + hash) + ord(
            c)  # make the `c` into a unicode
    return hash % max  # mod hash into max


# '''
# Fill this in.


# If you are overwriting a value with a different key, print a warning.
# '''
# Insert method takes in hash_table, key and value
def hash_table_insert(hash_table, key, value):
    # 1. Find the index we're going to in the internal array
    # To do this we use our hash function
    index = hash(key, hash_table.capacity)
    # create a new pair using key and value
    new_pair = Pair(key, value)
    # 2. if there is already a pair 
    if hash_table.storage[index]:
        # 3. Print a warning
        print(
            'Warning: overwriting a value with a different key is not allowed')
    # 4. Create pair, add it
    hash_table.storage[index] = new_pair.value


# '''
# Fill this in.


# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    # 2. check if a value exists:
    if hash_table.storage[index]:
        # 3. Set it to None
        hash_table.storage[index] = None
    else:
        # 4. Print warning
        print('Warning: the value you try to remove doesnt exist')
        return None


# '''
# Fill this in.


# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # 1. Compute hash
    index = hash(key, hash_table.capacity)
    # 2. check if a value exists:
    if hash_table.storage[index]:
        # 3. Return the value
        return hash_table.storage[index]
    else:
        # 4. Print warning
        print('Warning: the value you try to retrieve doesnt exist')
        # 5. Return None
        return None


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")


Testing()
