#https://leetcode.com/problems/two-city-scheduling/description/
#time O(nlogn) space O(n)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff =[[abs(a-b),a,b] for a,b in costs]
        diff.sort(reverse=True)
        countA = 0
        countB = 0
        ans = 0
        for i in range(n):
            d,a,b = diff[i]
            if a>b:
                if countB<n//2:
                    countB+=1
                    ans+=b
                else:
                    countA+=1
                    ans+=a
            else:
                if countA<n//2:
                    countA+=1
                    ans+=a
                else:
                    countB+=1
                    ans+=b
        return ans


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        diff =[[b-a,a,b] for a,b in costs]
        diff.sort()
        ans = 0
        for i in range(n):
            d,a,b = diff[i]
            if i<n//2:
                ans+=b
            else:
                ans+=a
        return ans
