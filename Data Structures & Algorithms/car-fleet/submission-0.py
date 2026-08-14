# as the cars' positions intercept, the one who was behind the slower car turns into a fleet
# we pop as cars that fleet to x speed 
# overall takes O(log n) as we need to sort in reverse order (end to beginning)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)] # list comprehension. array of pairs for each car and iterate through position and speed lists at the same time
        carfleets = []
        for p, s in sorted(pair)[::-1]: # reverse sorted order
            carfleets.append((target - p) / s) # calculating distance
            if len(carfleets) >= 2 and carfleets[-1] <= carfleets[-2]: # if the time of current car is lesser than the next one that means they collide
                carfleets.pop()
        return len(carfleets)