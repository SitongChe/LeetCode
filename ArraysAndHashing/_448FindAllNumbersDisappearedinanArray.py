#https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
#time O(n) ,space  O(1)
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n)-1
            nums[i]=-1*abs(nums[i])
        ans = []
        for i,n in enumerate(nums):
            if n > 0:
                ans.append(i+1)
        return ans

