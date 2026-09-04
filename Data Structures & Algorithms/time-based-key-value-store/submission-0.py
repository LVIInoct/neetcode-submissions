class TimeMap:

    def __init__(self):
        self.store = {} # key = string , value [list of [value, time]]
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [] # make the key a list
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        got = ""
        values = self.store.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            # [1] = timestamp, [0] = value
            if values[m][1] <= timestamp:
                got = values[m][0]
                l = m + 1
            else:
                r = m - 1

        return got