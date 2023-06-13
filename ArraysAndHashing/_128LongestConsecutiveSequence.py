#https://leetcode.com/problems/two-sum/
#time O(N),space O(N)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        n = len(nums)
        ans = 0
        for i in range(n):
            cur = nums[i]
            if cur-1 not in numSet:
                length = 1
                while cur+length in numSet:
                    length+=1
                ans = max(ans, length)
        return ans

#time O(N),space O(N)
#union find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uf = {}
        size = {}
        if len(nums)==0:
            return 0
        def find(x):
            uf.setdefault(x,x)
            size.setdefault(x,1)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]

        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            if size[rootx]<size[rooty]:
                size[rooty]+=size[rootx]
                uf[rootx]=rooty
            else:
                size[rootx]+=size[rooty]
                uf[rooty]=rootx
        
        for num in nums:
            if num in uf:
                continue
            find(num)
            if num-1 in uf:
                union(num-1,num)
            if num+1 in uf:
                union(num+1,num)
        return max(size.values())



        

        
            


