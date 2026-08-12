# goal is to keep track of how many days pass until a bigger or the same temperature shows up later on in the stack since it's decreasing order, and in the output set how many days (indexes) it took to find one
# I. declare pairs II. while stack is not empty and temperature is bigger than the top of our stack as the first value in that pair
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = [] # pair: [temp, index]
        
        for i, t in enumerate(temperatures): # i and t are our temperature and index
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop() # pairs
                output[stackInd] = (i - stackInd) # current temperature - index of temperature we just popped = number of days
            stack.append([t, i])
        return output