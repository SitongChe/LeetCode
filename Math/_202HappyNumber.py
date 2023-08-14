#https://leetcode.com/problems/happy-number/description/
#time O(d), where "d" is the number of digits in the input number. space O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def sumSquare(n):
            total = 0
            while n:
                total += (n%10)**2
                n//=10
            return total
        slow,fast = n,sumSquare(n)
        while slow!=fast:
            fast = sumSquare(sumSquare(fast))
            slow = sumSquare(slow)
        return fast == 1
        
        
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1 or n == 7:
            return True
        if n//10==0:
            return False
        total = 0
        while n:
            total+=(n%10)**2
            n//=10
        return self.isHappy(total)
        
