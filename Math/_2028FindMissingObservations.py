#https://leetcode.com/problems/find-missing-observations/description/
#time O(n) space O(n)
class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        total = (m+n)*mean
        diff = total-sum(rolls)
        if diff<n or diff>6*n:
            return []
        ans = []
        for i in range(n):
            cur = min(6,diff-(n-i-1))
            ans.append(cur)
            diff -= cur
        return ans
