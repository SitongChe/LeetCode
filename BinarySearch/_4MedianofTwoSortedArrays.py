#https://leetcode.com/problems/median-of-two-sorted-arrays/
#time  O(log(min(N, M))), space O(1)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2
        if len(B)<len(A):
            A,B = B,A
        left = 0
        right = len(A)-1
        total = len(A)+len(B)
        half = total//2
        while True:
            i = left+(right-left)//2
            j = half-i-2
            Aleft = A[i] if i>=0 else -inf
            Aright = A[i+1] if i+1<len(A) else inf
            Bleft = B[j] if j>=0 else -inf
            Bright = B[j+1] if j+1<len(B) else inf
            if Aleft<=Bright and Bleft<=Aright:
                if total%2:
                    return min(Aright,Bright)
                else:
                    return (max(Aleft,Bleft)+min(Aright,Bright))/2
            elif Aleft>Bright:
                right = i-1
            else:
                left = i+1

