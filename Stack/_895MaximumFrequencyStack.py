#https://leetcode.com/problems/maximum-frequency-stack/description/
#time O(1) space O(N*frequency)
class FreqStack:

    def __init__(self):
        self.stacksByCnt = defaultdict(list)
        self.count = Counter()
        self.maxCount = 0

    def push(self, val: int) -> None:
        self.count[val]+=1
        if self.count[val]>self.maxCount:
            self.maxCount = self.count[val]
        self.stacksByCnt[self.count[val]].append(val)

    def pop(self) -> int:
        ans = self.stacksByCnt[self.maxCount].pop()
        if not self.stacksByCnt[self.maxCount]:
            self.maxCount -= 1
        self.count[ans]-=1
        
        return ans
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
