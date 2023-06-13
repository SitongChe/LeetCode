#https://leetcode.com/problems/find-median-from-data-stream/
#time addNum O(logN) space O(N)
class MedianFinder:

    def __init__(self):
        self.small = [] #maxHeap
        self.large = [] #minHeap
        
    def addNum(self, num: int) -> None:
        if self.large and self.large[0]<num:
            heapq.heappush(self.large,num)
        else:
            heapq.heappush(self.small,-num)
        
        if len(self.large)>len(self.small)+1:
            cur = heapq.heappop(self.large)
            heapq.heappush(self.small,-cur)
        elif len(self.small)>len(self.large)+1:
            cur = heapq.heappop(self.small)
            heapq.heappush(self.large,-cur)
        
        

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        elif len(self.small)<len(self.large):
            return self.large[0]
        else:
            return (self.large[0]-self.small[0])/2
