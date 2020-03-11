class DynamicArray:
    # my_array = [4] # make an empty array of size 4, NOT a 1 size array with a 4
    def __init__(self, capacity):
        self.capacity = capacity
        self.count = 0
        self.storage = [None] * self.capacity

    def __len__(self):
        return self.count

    def insert(self, index, value):
        # make sure we have open space
        if self.count >= self.capacity:
            # Todo: make array dynamically resize
            self.double_size() # def double_size()

        # make sure index is in range
        if index > self.count:
            print('Error: Index out of range')
            return

        # shift everything over to right
        # start with the last one, move it to right
        for i in range(self.count, index, -1):
            self.storage[i] = self.storage[i - 1]

        # insert value
        self.storage[index] = value
        self.count += 1

    def append(self, value):
        self.insert(self.count, value)

    def double_size(self):
        self.capacity *= 2
        new_storage = [None] * self.capacity
        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage


my_arr = DynamicArray(4)
my_arr.insert(0, 1)
my_arr.insert(0, 2)
my_arr.insert(1, 3)
my_arr.insert(3, 4)
my_arr.insert(0, 5)
my_arr.append(20)
print(my_arr.storage)