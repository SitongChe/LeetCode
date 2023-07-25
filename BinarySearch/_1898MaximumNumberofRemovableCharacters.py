#https://leetcode.com/problems/maximum-number-of-removable-characters/description/
#time get O(len(s)*log(len(removable)), space O(len(removable))
class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def containsSub(skip):
            j = 0
            for i in range(len(s)):
                if i not in skip:
                    if s[i]==p[j]:
                        j+=1
                        if j == len(p):
                            return True
            return False

        n = len(removable)
        left = 0
        right = n-1
        while left+1<right:
            mid = left+(right-left)//2
            skip = set(removable[:mid+1])
            if containsSub(skip):
                left = mid
            else:
                right = mid
        if containsSub(set(removable[:right+1])):
            return right+1
        elif containsSub(set(removable[:left+1])):
            return left+1
        return 0
