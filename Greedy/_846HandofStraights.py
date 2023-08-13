#https://leetcode.com/problems/hand-of-straights/description/
#time O(n + k * log(k)) where n is the number of cards in the hand. where k is the number of unique cards. space O(n)
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n%groupSize:
            return False
        count = Counter(hand)
        minHeap = [i for i in count.keys()]
        heapq.heapify(minHeap)
        while minHeap:
            cur = minHeap[0]
            for i in range(cur,cur+groupSize):
                if i not in count:
                    return False
                count[i]-=1
                if count[i]==0:
                    if i!=minHeap[0]:
                        return False
                    heapq.heappop(minHeap)
        return True
        
