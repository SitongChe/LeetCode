#https://leetcode.com/problems/eliminate-maximum-number-of-monsters/description/
#time O(nlogn) space O(n)
class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [d/s for d,s in zip(dist,speed)]
        n = len(dist)
        time.sort()
        ans = 0
        for i in range(n):
            if i<time[i]:
                ans+=1
            else:
                return ans
        return ans
