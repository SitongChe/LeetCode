#https://leetcode.com/problems/add-to-array-form-of-integer/description/
#time  O(max(len(num), log10(k))), O(len(num))
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = len(num)
        carry = 0
        i = n-1
        while k or carry:
            cur = k%10+carry
            if i>=0:
                cur+=num[i]
                num[i]=cur%10
                i-=1
            else:
                num=[cur%10]+num
            carry = cur//10
            k//=10
        return num
