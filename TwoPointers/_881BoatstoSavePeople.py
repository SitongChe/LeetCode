#https://leetcode.com/problems/boats-to-save-people/description/
#time O(n), space O(1)
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        n = len(people)
        r = n-1
        ans = 0
        while l<=r:
            remaining = limit-people[r]
            r-=1
            ans +=1
            if l<=r and remaining >= people[l]:
                l+=1
        return ans
