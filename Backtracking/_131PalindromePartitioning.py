#https://leetcode.com/problems/palindrome-partitioning/
#time O(2^N) space O(N*2^N)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def isPalindrome(cur):
            i = 0
            j = len(cur)-1
            while i<j:
                if cur[i]!=cur[j]:
                    return False
                i+=1
                j-=1
            return True

        def traceback(index,tmp):
            if index == n:
                ans.append(tmp.copy())
                return
            for i in range(index,n):
                cur = s[index:i+1]
                if isPalindrome(cur):
                    tmp.append(cur)
                    traceback(i+1,tmp)
                    tmp.pop()
   
        n = len(s)
        ans = []
        traceback(0,[])
        return ans
        

                    



