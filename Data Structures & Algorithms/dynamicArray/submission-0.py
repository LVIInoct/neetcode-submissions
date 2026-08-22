class DynamicArray:
    
    def __init__(self, capacity: int):
        self.length = 0
        self.capacity = capacity
        self.arr = [0] * self.capacity

    def get(self, i: int) -> int:
        return self.arr[i]
        
    # set n value to i index
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        
    # insert n at end of array and resize if needed
    def pushback(self, n: int) -> None:
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    # remove last element
    def popback(self) -> int:
        if self.length > 0: # if length > 0 decrease it by 1
            self.length -=1
        return self.arr[self.length]
    
    # resizing by doubling capacity and copying elements
    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        new_arr = [0] * self.capacity
        for i in range(self.length): # going through old array's length to copy
            new_arr[i] = self.arr[i] # iterating through new arr and self arr to pass elements
        self.arr = new_arr # updating

    def getSize(self) -> int:
        return self.length
        
    def getCapacity(self) -> int:
        return self.capacity
