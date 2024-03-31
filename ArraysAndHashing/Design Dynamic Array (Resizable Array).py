#https://neetcode.io/problems/dynamicArray

class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [0]*capacity
        self.length = 0


    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i]=n


    def pushback(self, n: int) -> None:
        if self.capacity == self.length:
            self.resize()
        self.set(self.length, n)
        self.length += 1
        
    def popback(self) -> int:
        self.length -= 1
        return self.array[self.length]
 

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0]*self.capacity
        for i,num in enumerate(self.array):
            new_arr[i]=num
        self.array = new_arr

    def getSize(self) -> int:
        return self.length
    
    def getCapacity(self) -> int:
        return self.capacity

