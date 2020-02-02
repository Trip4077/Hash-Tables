class DynamicArray:
    def __init__(self, size):
        self.count = 0
        self.size = size
        
        self.storage = [None] * size

    def append(self, value):
        if self.count == self.size:
            self.resize()

        self.storage[self.count] = value
        self.count += 1

    def insert(self, value, idx):
        if self.count == self.size:
            self.resize()   

        for i in range( self.count, idx, -1 ):
            self.storage[i] = self.storage[i - 1]

        self.storage[idx] = value
        self.count += 1

    def resize(self):
        self.size *= 2
        newArr = [None] * self.size

        for i in range(self.size // 2):
            newArr[i] = self.storage[i]

        self.storage = newArr


DA = DynamicArray(4)

DA.append(4)
DA.append(2)
DA.append(4)
DA.append(7)
DA.append(9)

DA.insert(1, 2)
DA.insert(10, 0)
DA.insert(100, 5)
DA.insert(1000, 8)

print(DA.storage)