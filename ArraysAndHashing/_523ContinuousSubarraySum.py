#https://leetcode.com/problems/continuous-subarray-sum/description/
#time O(n) ,space  O(1)
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        hashmap[0]=-1
        sum = 0
        for i,num in enumerate(nums):
            sum += num
            if sum%k in hashmap:
                if i-hashmap[sum%k]>=2:
                    return True
                else:
                    continue
            hashmap[sum%k] = i
        return False
