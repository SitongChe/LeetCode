#https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/
#time O(n) space O(1)
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        ans = sum(cardPoints[:k])
        res = ans
        for i in range(k):
            ans -= cardPoints[k-i-1]
            ans += cardPoints[n-1-i]
            res = max(ans,res)
        return res
