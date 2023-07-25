#https://leetcode.com/problems/search-suggestions-system/description/
#time get O(N * M * log N + K * log N), space O(k)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        ans = []
        l = 0
        r = len(products)-1
        for i,w in enumerate(searchWord):
            while l<=r and (len(products[l])<=i or products[l][i]!=w):
                l+=1
            while l<=r and (len(products[r])<=i or products[r][i]!=w):
                r-=1
            res = []
            for j in range(min(3,r-l+1)):
                res.append(products[l+j])
            ans.append(res)
        return ans
            
            


                
            

