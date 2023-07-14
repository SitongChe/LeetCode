#https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/description/
#time O(n) ,space  O(1)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxNum = -1
        for i in range(n-1,-1,-1):
            tmp = maxNum
            maxNum = max(maxNum, arr[i])
            arr[i]=tmp

        return arr
