#https://leetcode.com/problems/plus-one/description/
#time O(n) space O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carry = 0
        digits[n-1]+=1
        if digits[n-1]>=10:
            digits[n-1]=digits[n-1]%10
            carry = 1
        for i in range(n-2,-1,-1):
            if carry==0:
                break
            digits[i]+=carry
            carry = 0
            if digits[i]>=10:
                digits[i]=digits[i]%10
                carry = 1
        if carry:
            digits=[1]+digits
        return digits
