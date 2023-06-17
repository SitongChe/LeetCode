#https://leetcode.com/problems/kth-largest-element-in-an-array/description/
#time O(n) space O(n)
#quick select
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(left, right, pivot_index):
            pivot = nums[pivot_index]
            # Move the pivot element to the rightmost position
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
            
            # Move all elements smaller than the pivot to the left
            store_index = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[i], nums[store_index] = nums[store_index], nums[i]
                    store_index += 1
            
            # Move the pivot element to its final sorted position
            nums[store_index], nums[right] = nums[right], nums[store_index]
            
            return store_index
        
        def quick_select(left, right, k_smallest):
            if left == right:
                return nums[left]
            
            # Choose a random pivot index
            pivot_index = random.randint(left, right)
            
            # Partition the array around the pivot
            pivot_index = partition(left, right, pivot_index)
            
            if k_smallest == pivot_index:
                return nums[k_smallest]
            elif k_smallest < pivot_index:
                return quick_select(left, pivot_index - 1, k_smallest)
            else:
                return quick_select(pivot_index + 1, right, k_smallest)
        
        # Convert kth largest to kth smallest index
        k_smallest = len(nums) - k
        
        return quick_select(0, len(nums) - 1, k_smallest)
