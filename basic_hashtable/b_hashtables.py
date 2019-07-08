

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
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(strings):
    hash = 5381
    for x in strings:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    # 1. Compute hash
    index = hash(key) % hash_table.capacity
    # 2. if overwriting a value with a different key:
    if hash_table.storage[index]:
        # 3. Print a warning
        print('Warning: overwriting a value with a different key is not allowed')
    # 4. Create pair, add it
    hash_table.storage[index] = Pair(key, value)


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    # 1. Compute hash
    index = hash(key) % hash_table.capacity
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
    index = hash(key) % hash_table.capacity
    # 2. check if a value exists:
    if hash_table.storage[index]:
        # 3. Get the value
        hash_table.storage[index].value
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
