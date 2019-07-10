

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        # max length of hash table
        self.capacity = capacity
        # underlying data sructure
        self.storage = [None] * capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)

    return hash % max


# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
     # create a new pair using key and value
    linkedPair = LinkedPair(key, value)

    # get the index via the hash function
    index = hash(linkedPair.key, hash_table.capacity)

     # check if the current storage already contain a Linked List or Pair
    if hash_table.storage[index]:
        # loop through the linked pairs until we get to a current key or the end pair
        current_pair = hash_table.storage[index]
        while current_pair.next:
            if current_pair.key == key:
                current_pair.value = value
                return None
            # set new next pair as current_pair
            current_pair = current_pair.next
        # check if the last pair in the list matches the key
        if current_pair.key == key:
            current_pair.value = value
        # add the linked pair as the next item
        else:
            current_pair.next = linkedPair
    else:
        hash_table.storage[index] = linkedPair

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    pass


# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    # create a new pair using key and value
    linkedPair = LinkedPair(key, value)
    # set the index 
    index = hash_table.storage[ linkedPair]
    # check if there's anything at the index
    if not index:
        return None
    else:
        # loop through the pairs until we find the key
        current_pair = hash_table.storage[linkedPair]
        while current_pair.next:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next
        # check if it's the last pair in the list
        if current_pair.key == key:
            return current_pair.value
        # return none if the key is not found
        else:
            return None


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
   # double the capacity
    newCapacity = hash_table.capacity * 2
    # initialize new list for storage
    newStorage = [None] * newCapacity
    # copy over the elements
    for i in range(len(hash_table.storage)):
        newStorage[i] = hash_table.storage[i] 
    # set new storage and capacity
    hash_table.storage = newStorage
    hash_table.capacity = newCapacity
    # return updated hash table
    return hash_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
