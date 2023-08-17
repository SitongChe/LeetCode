#https://leetcode.com/problems/shuffle-the-array/description/
#time  O(n), O(1)
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        #1 <= nums[i] <= 10^3 so only take up to 10 bits, 1024. we can use the rest 32-10 bits to store more data
        for i in range(n):
            nums[i]<<=10
            nums[i]+=nums[i+n]
        mask = 2**10-1
        for j in range(2*n-1,-1,-2):
            cur = nums[j//2]
            nums[j]=cur&mask
            nums[j-1]=cur>>10
        return nums
