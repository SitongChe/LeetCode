#https://leetcode.com/problems/permutations-ii/description/
#time O(N!) space O(N)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def traceback():
            if len(tmp)==n:
                ans.append(tmp.copy())
                return
            for i in range(n):
                if i not in used:
                    if i-1>=0 and nums[i]==nums[i-1] and i-1 not in used:
                        continue
                    tmp.append(nums[i])
                    used.add(i)
                    traceback()
                    tmp.pop()
                    used.remove(i)
        ans = []
        tmp = []
        used = set()
        n = len(nums)
        nums.sort()
        traceback()
        return ans
        
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def traceback(index):
            if index == n:
                ans.append(nums.copy())
                return
            visited = set()
            for i in range(index,n):
                if nums[i] in visited:
                    continue
                visited.add(nums[i])
                nums[i],nums[index]=nums[index],nums[i]
                traceback(index+1)
                nums[i],nums[index]=nums[index],nums[i]
        ans = []
        n = len(nums)
        nums.sort()
        traceback(0)
        return ans


                    



