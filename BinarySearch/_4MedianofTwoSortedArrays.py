#https://leetcode.com/problems/median-of-two-sorted-arrays/
#time  O(log(min(N, M))), space O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left = 0
        if len(nums1)>len(nums2):
            nums1,nums2 = nums2,nums1
        right = len(nums1)*2
        total = len(nums1)+len(nums2)
        while True:
            mid = left+(right-left)//2
            mid2 = total-mid
            Aleft = nums1[(mid-1)//2] if mid>0 else -inf
            Aright = nums1[mid//2] if mid<len(nums1)*2 else inf
            Bleft = nums2[(mid2-1)//2] if mid2>0 else -inf
            Bright = nums2[mid2//2] if mid2<len(nums2)*2 else inf

            if Aleft<=Bright and Aright>=Bleft:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                right = mid-1
            else:
                left = mid+1
