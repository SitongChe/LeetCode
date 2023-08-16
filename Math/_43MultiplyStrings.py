#https://leetcode.com/problems/multiply-strings/description/
#time O(n1*n2) space O(n1+n2)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        num1 = num1[::-1]
        num2 = num2[::-1]
        n1 = len(num1)
        n2 = len(num2)
        ans = [0]*(n1+n2+1)
        for i in range(n1):
            for j in range(n2):
                product = (ord(num1[i])-ord('0'))*(ord(num2[j])-ord('0'))
                pos1 = i+j
                pos2 = pos1+1
                product += ans[pos1]
                ans[pos1]=product%10
                ans[pos2]+=product//10
        k = n1+n2
        while ans[k]==0:
            k-=1
        return "".join(map(str,ans[k::-1]))

        
