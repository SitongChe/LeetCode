#https://leetcode.com/problems/sort-an-array/description/
#time O(n log n) ,space  O(n) 
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(l,m,r):
            left = nums[l:m+1]
            right = nums[m+1:r+1]
            i,j,k= 0,0,l
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i+=1
                else:
                    nums[k]=right[j]
                    j+=1
                k+=1
            if i<len(left):
                nums[k:r+1]=left[i:]
            if j<len(right):
                nums[k:r+1]=right[j:]
        def mergeSort(l,r):
            if l == r:
                return
            m = l+(r-l)//2
            mergeSort(l,m)
            mergeSort(m+1,r)
            merge(l,m,r)
        mergeSort(0,len(nums)-1)
        return nums

