#https://leetcode.com/problems/find-unique-binary-string/description/
#time O(N) space O(n)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = ""
        n = len(nums)
        for i in range(n):
            ans += str(1-int(nums[i][i]))
        return ans

