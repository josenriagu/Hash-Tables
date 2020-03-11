# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def append(self, key, value):
        # if key exists, simply overwrite value
        if self.key == key:
            self.value = value
        # otherwise if no next
        elif not self.next:
            # set next to a new instance of LinkedPair using passed in arguments
            self.next = LinkedPair(key, value)
        # otherwise, append to next
        else:
            self.next.append(key, value)

    def retrieve(self, key):
        # if key exist, return it's value
        if self.key == key:
            return self.value
        # otherwise if no next, end of the LP has been reached, return none
        elif not self.next:
            return None
        # otherwise, call the retrieve method on the next
        else:
            return self.next.retrieve(key)


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        # base case: if storage is filled (no None), resize
        if not None in self.storage:
            self.resize()
        # hash key using the _hash_mod algo
        hashed_key = self._hash_mod(key)
        # if hash already exists (hash collision), append to the linkedList
        if self.storage[hashed_key]:
            self.storage[hashed_key].append(key, value)
        # else form a new linkedList
        else:
            self.storage[hashed_key] = LinkedPair(key, value)

    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        # hash key using the _hash_mod algo
        hashed_key = self._hash_mod(key)
        # if key is not found in storage, print error message and return
        if not self.storage[hashed_key]:
            print("Not Found: A hash for that key has probably gone to Mars!")
            return
        # set storage at hashed_key to current
        current = self.storage[hashed_key]
        # set prev_node to None
        prev_node = None
        # if current key matches passed in key and there is no next
        if current.key == key and not current.next:
            # set storage at hashed_key to None
            self.storage[hashed_key] = None
        # else if current key matches passed in key and there is next
        elif current.key == key:
            # set storage at hashed_key to its next
            self.storage[hashed_key] = self.storage[hashed_key].next
        # otherwise
        else:
            # while current exists
            while current:
                # if current key matches passed in key and there is next
                if current.key == key:
                    # set prev_node next to current next
                    prev_node.next = current.next
                    return
                # set prev_node next to current
                prev_node = current
                # move current to its next
                current = current.next

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        # hash key using the _hash_mod algo
        hashed_key = self._hash_mod(key)
        # if storage at hashed key exists
        if self.storage[hashed_key]:
            # call the retrieve method of the LinkedPair class
            return self.storage[hashed_key].retrieve(key)
        # otherwise return None
        else:
            return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        # double the storage capacity
        self.capacity *= 2
        # store old storage
        old_storage = self.storage
        # change new storage to Nones in expanded capacity
        self.storage = [None] * self.capacity

        # loop through and copy existing items in old_storage
        for node in old_storage:
            # if node exists
            if node:
                # set node to current
                current = node
                # while current is not None
                while current:
                    # call the insert method on the storage
                    self.insert(current.key, current.value)
                    # move current to its next
                    current = current.next


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
