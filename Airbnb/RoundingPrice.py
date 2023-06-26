#time O(n) space O(n)
import math
class Solution:
    def rounding(self,prices):
        sum = 0
        roundedSum = 0
        ans = []
        posDiffs = []
        negDiffs = []
        for i,price in enumerate(prices):
            sum+=price
            roundedPrice = round(price)
            diff = roundedPrice-price
            if diff > 0:
                posDiffs.append([diff,i])
            elif diff<0:
                negDiffs.append([diff,i])
            ans.append(roundedPrice)
            roundedSum += roundedPrice
        sumRounded = round(sum)
        diffCount = sumRounded-roundedSum
        if diffCount>0:
            negDiffs.sort()
            for i in range(diffCount):
                ans[negDiffs[i][1]]+=1
        elif diffCount<0:
            posDiffs.sort()
            for i in range(-diffCount):
                ans[posDiffs[i][1]]-=1
        return ans
            

def main():
    solution = Solution()
    optput = solution.rounding([1.5, 2.51, 3.6, 3.6, 4.6])
    print("output:", optput)

if __name__ == "__main__":
    main()
