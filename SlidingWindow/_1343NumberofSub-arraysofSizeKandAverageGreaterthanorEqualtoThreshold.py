#https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/
#time O(N), space O(1)
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        n = len(arr)
        cur = sum(arr[:k-1])
        for r in range(k-1,n):
            cur += arr[r]
            if cur/k>=threshold:
                ans+=1
            cur -= arr[r-k+1]
        return ans
