#https://leetcode.com/problems/contains-duplicate-ii/description/
#time O(N), space O(k), where k is the size of the character set
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        l = 0
        window = set()
        for r in range(n):
            if r-l>k:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
