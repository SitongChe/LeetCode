#https://leetcode.com/problems/time-based-key-value-store/
#time get O(logN), set O(N), space O(N)
class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value,timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        times = self.dict[key]
        left = 0
        right = len(times)-1
        while left+1<right:
            mid = left+(right-left)//2
            if times[mid][1]>timestamp:
                right = mid
            else:
                left = mid
        if times[right][1]<=timestamp:
            return self.dict[key][right][0]
        if times[left][1]<=timestamp:
            return self.dict[key][left][0]
        return ""

        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
