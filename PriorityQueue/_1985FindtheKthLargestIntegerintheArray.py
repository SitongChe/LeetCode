#https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/
#time O((m + n) log n) space O(N)
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums = [-int(num) for num in nums]
        heapq.heapify(nums)
        for i in range(k-1):
            heapq.heappop(nums)
        return str(-nums[0])

class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sort(x,y):
            n = len(x)
            m = len(y)
            if n!=m:
                return -1 if n<m else 1
            else:
                return -1 if x<y else 1
            return 0

        nums.sort(key = cmp_to_key(sort), reverse = True)
        return nums[k-1]
