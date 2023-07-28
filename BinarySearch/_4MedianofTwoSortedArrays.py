#https://leetcode.com/problems/median-of-two-sorted-arrays/
#time  O(log(min(N, M))), space O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def check(mid):
            mid2 = half-mid-2
            num1Left = nums1[mid] if mid>= 0 else -inf
            num2Left = nums2[mid2] if mid2>=0 else -inf
            num1Right = nums1[mid+1] if mid+1<len(nums1) else inf
            num2Right = nums2[mid2+1] if mid2+1<len(nums2) else inf

            if num1Left<=num2Right and num2Left<=num1Right:
                if total%2:
                    self.ans = min(num1Right,num2Right)
                else:
                    self.ans = (max(num1Left,num2Left)+min(num1Right,num2Right))/2
            return [num1Left,num2Left,num1Right,num2Right]

        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1
        left = -1
        right = len(nums1)-1
        total = len(nums1)+len(nums2)
        half = total//2
        self.ans = inf
        while left+1<right:
            mid = left+(right-left)//2
            num1Left,num2Left,num1Right,num2Right = check(mid)
            if self.ans != inf:
                return self.ans
            if num1Left>num2Right:
                right = mid
            else:
                left = mid

        check(left)
        if self.ans != inf:
            return self.ans
        check(right)
        if self.ans != inf:
            return self.ans
