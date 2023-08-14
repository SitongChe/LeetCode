#https://leetcode.com/problems/max-points-on-a-line/description/
#time O(n^2) space O(n)
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def rate(x,y):
            if x[0]==y[0]:
                return inf
            return (y[1]-x[1])/(y[0]-x[0])
        n = len(points)
        ans = 1
        for i in range(n):
            count = defaultdict(int)
            for j in range(i+1,n):
                slope = rate(points[i],points[j])
                count[slope]+=1
            ans = max(ans,max(count.values())+1 if count else 0)
        return ans

