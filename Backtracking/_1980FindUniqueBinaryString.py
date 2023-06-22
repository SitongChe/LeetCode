#https://leetcode.com/problems/find-unique-binary-string/description/
#time O(2^N) space O(n)
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def traceback():
            if self.ans:
                return
            if len(tmp)==n:
                string = "".join(tmp)
                if string in numsSet:
                    return
                self.ans = string
                return
            for i in range(2):
                tmp.append(str(i))
                traceback()
                tmp.pop()

        self.ans = None
        n = len(nums)
        tmp = []
        numsSet = set(nums)
        traceback()
        return self.ans
