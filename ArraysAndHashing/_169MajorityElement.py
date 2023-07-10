#https://leetcode.com/problems/majority-element/description/
#time O(n) ,space  O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for n in nums:
            if count == 0:
                major = n
                count+=1
            elif n == major:
                count+=1
            else:
                count-=1
        return major

