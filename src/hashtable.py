# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

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
        index = self._hash_mod(key) # variable index holds the hashed key 
        hash_table = self.storage # hash_table variable

        # deal with collision IF there are matching indexes

        if hash_table[index] is not None: # checks if there is something in that index
            new_pair = LinkedPair(key, value) # new pair variable
            new_pair.next = hash_table[index] # needed for linked lists in case of collision
            hash_table[index] = new_pair # insert the new_pair (key, value) in that index
        else:
            hash_table[index] = LinkedPair(key, value) # insert the new_pair (key, value) in that index

        return


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        
        if current.key == key: # checks if the key in that index is the target key
            self.storage[index] = current.next # this removes that (key, value)
        if current.key != key: # this is for collisions
            while current.next is not None:
                next = current.next # sets the `next` variable
                if next.key == key: # checks for the key for `next`
                    current.next = next.next # removes that key
            print("key not found") # print error for when no key exists in hash_table


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        if current is not None: # if we have something in that index
            while current: # while loop to traverse to check
                if current.key is key: # if the key matches that index's key
                    return current.value # return that value
                elif current.next is not None: # if there is a next
                    current = current.next # move on to the next one by setting current to current.next
        else:
            return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity
        current = None
        for i in old_storage:
            current = i
            while current:
                self.insert(current.key, current.value)
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
