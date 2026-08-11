# delcare an element stack and an index/minimum stack so each time we add an element we keep track of our smallest number
class MinStack:

    def __init__(self):
        self.stack = []
        self.indexStack = []
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.indexStack[-1] if self.indexStack else val) # take min of val and top item of indexStack (if non empty. if it is empty then just take min of val)
        self.indexStack.append(val) # add it to second array
        
    def pop(self) -> None:
        self.stack.pop()
        self.indexStack.pop()
        
    def top(self) -> int:
        return self.stack[-1] # return 'top'
        
    def getMin(self) -> int:
        return self.indexStack[-1] # return 'top' min stack
        
