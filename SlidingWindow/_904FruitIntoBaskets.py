#https://leetcode.com/problems/fruit-into-baskets/description/
#time O(N), space O(1)
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #find the max length of the sub array that contain at most 2 fruit
        k = 2
        count = defaultdict(int)
        n = len(fruits)
        if n<3:
            return n
        start = 0
        ans = 0
        for end in range(n):
            if count[fruits[end]]==0:
                k-=1
            count[fruits[end]]+=1
            while k<0:
                count[fruits[start]]-=1
                if count[fruits[start]]==0:
                    k+=1
                start+=1
            ans = max(ans,end-start+1)
        return ans
