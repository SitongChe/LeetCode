#https://leetcode.com/problems/unique-binary-search-trees/description/
#time O(N), space O(N)

class Solution:
    def numTrees(self, n: int) -> int:
        def num(n):
            if n in mp:
                return mp[n]
            total = 0
            for i in range(n):
                total += num(i)*num(n-i-1)
            mp[n]=total
            return total
        if n == 0:
            return 0
        mp = {}
        mp[0]=1
        mp[1]=1
        mp[2]=2
        return num(n)

