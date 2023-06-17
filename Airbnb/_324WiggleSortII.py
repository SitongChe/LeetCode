#https://leetcode.com/problems/wiggle-sort-ii/description/
#time O(n) space O(1)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def findMedian(nums):
            nums.sort()
            n = len(nums)
            if n % 2 == 1:
                return nums[n // 2]
            else:
                return min(nums[n // 2 - 1], nums[n // 2])

        n = len(nums)
        if n == 0:
            return
        median = findMedian(nums)
        # Index Mapping: Map the elements to their final positions
        index_mapping = lambda i: (2 * i + 1) % (n | 1)
        
        # Dutch National Flag partitioning
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[index_mapping(i)] < median:
                nums[index_mapping(i)], nums[index_mapping(right)] = nums[index_mapping(right)], nums[index_mapping(i)]
                right -= 1
            elif nums[index_mapping(i)] > median:
                nums[index_mapping(i)], nums[index_mapping(left)] = nums[index_mapping(left)], nums[index_mapping(i)]
                left += 1
                i += 1
            else:
                i += 1
                
                
                
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def findMedian(nums):
            heapq.heapify(nums)
            for i in range(len(nums)//2):
                heapq.heappop(nums)
            return nums[0]
            

        n = len(nums)
        if n == 0:
            return
        median = findMedian(nums.copy())
        ans = nums.copy()
        # Dutch National Flag partitioning
        left, i, right = 0, 0, n - 1
        while i <= right:
            if ans[i] > median:
                ans[right],ans[i] = ans[i],ans[right]
                right -= 1
            elif ans[i] < median:
                ans[left],ans[i] = ans[i],ans[left]
                left += 1
                i += 1
            else:
                i += 1
        mid = (n - 1) // 2
        nums[::2] = ans[mid::-1]
        nums[1::2] = ans[:mid:-1]

