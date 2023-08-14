#https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#time O(n) space O(N)
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        

    def addNum(self, value: int) -> None:
        start,end = value,value
        left = []
        right = []
        for curStart,curEnd in self.intervals:
            if curStart>end+1:
                right.append([curStart,curEnd])
            elif curEnd<start-1:
                left.append([curStart,curEnd])
            else:
                start = min(curStart,start)
                end = max(curEnd,end)
        self.intervals = left+[[start,end]]+right

        

    def getIntervals(self) -> List[List[int]]:
        return self.intervals
        


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
