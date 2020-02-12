class DynamicArray:
    def __init__(self, capacity=8):
        self.count = 0
        self.capacity = capacity
        self.storage = [None] * self.capacity

    def insert(self, value, index):
        if self.count = self.capacity:
            # TODO : increase size
            print('Error: Array is full')
            return
        if index >= self.count:
            # Todo :  better error handling
            print('Error: Index out of bounds')
            return

        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]
        
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        if self.count = self.capacity:
            # TODO : increase size
            print('Error: Array is full')
            return

        self.storage[self.count - 1] = value
        self.count += 1

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]
        
        self.storage = new_storage # reassigning pointer to new array which is new_storage