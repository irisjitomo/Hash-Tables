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
        hash = 5381
        for i in key:
            hash = (( hash << 5 ) + hash) + ord(x)
        
        return hash


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
        index = self._hash_mod(key)
        current = self.storage[index]
        # check for Linked List
        if self.storage[index] is not None:
        # if yes, check to see if it is key
        # if key, update it
            newPair = LinkedPair(key, value)
            newPair.next = self.storage[index]
            self.storage[index] = newPair
        else:
            self.storage[index] = LinkedPair(key, value)

        return

        # if self.storage[index] is not None:
        #     print(f'WARNING: COLLISION HAS OCCURED at {index}')
            
        # else:
        #     self.storage[index] = (key, value)
        
        # return



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        prev = None

        if current.key == key:
            self.storage[index] = current.next
        if current.key != key:
            while current.next is not None:
                prev = current
                current = current.next
                if current.key == key:
                    prev.next = current.next
                    return None
            print(f'the key {key} was not found!')
        
        # return


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        if current is not None:
            while current:
                if current.key is key:
                    return current.value
                elif current.next is not None:
                    # we have to look at the .next  in the index where collision is
                    # print(f'WARNING: COLLISION HAS OCCURED at {index}')
                    current = current.next
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
        for item in old_storage:
            current = item
            while current:
                self.insert(current.key, current.value)
                current = current.next



if __name__ == "__main__":
    # ht1 = HashTable(2)

    # ht1.insert("key1", 'hello')
    # ht1.insert("unicorn", 'goodbye')
    # ht1.remove('key1')

    # print(ht1.storage)
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
