#https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/description/
#time O(n log n) ,space  O(1)
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        def sorter(x,y):
            n = len(x)
            m = len(y)
            if n!=m:
                return -1 if n<m else 1
            for i in range(n):
                if x[i]<y[i]:
                    return -1
                elif x[i]>y[i]:
                    return 1
            return 0
        nums.sort(key = cmp_to_key(sorter), reverse = True)
        return nums[k-1]

