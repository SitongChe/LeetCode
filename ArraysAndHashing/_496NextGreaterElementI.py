#https://leetcode.com/problems/next-greater-element-i/description/
#time O(n+m) ,space  O(n)
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexDict = {value:index for index,value in enumerate(nums2)}
        nextGreaterList = [-1]*len(nums2)
        stack = []
        for i in range(len(nums2)):
            while stack and nums2[stack[-1]]<nums2[i]:
                nextGreaterList[stack.pop()]=nums2[i]
            stack.append(i)
        return [nextGreaterList[indexDict[nums1[i]]] for i in range(len(nums1))]
        
