#https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
#time O(n) space O(N)
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for c in s:
            if stack and stack[-1][0]==c:
                stack[-1][1]+=1
            else:
                stack.append([c,1])
            if stack[-1][1]==k:
                stack.pop()
        ans = ""
        for i in range(len(stack)):
            ans += stack[i][0]*stack[i][1]
        return ans



        

