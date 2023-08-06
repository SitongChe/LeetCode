#https://leetcode.com/problems/find-unique-binary-string/description/
#time O(2^m) space O(n+m)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def traceback(index,tmp):
            if self.ans:
                    return
            if index == m:
                if tmp not in visited:
                    self.ans = tmp
                return
            for i in range(2):
                traceback(index+1,tmp+str(i))

        n = len(nums)
        m = len(nums[0])
        self.ans = ""
        visited=set(nums)
        traceback(0,"")
        return self.ans
 
#time O(m) space O(m)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        ans = ""
        for i in range(n):
            cur = 1-int(nums[i][i])
            ans += str(cur)
        return ans

