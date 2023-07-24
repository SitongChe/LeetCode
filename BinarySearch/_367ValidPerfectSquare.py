#https://leetcode.com/problems/valid-perfect-square/description/
#time O(N), space O(1)
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left+1<right:
            mid = left+(right-left)//2
            square = mid*mid
            if square == num:
                return True
            elif square<num:
                left = mid
            else:
                right = mid
        if left*left == num or right * right == num:
            return True
        return False
