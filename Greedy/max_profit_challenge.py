#Problem: Given a list of stock prices, find the max profit from 1 buy and 1 sell.

Constraints
Are all prices positive ints?
Yes
Is the output an int?
Yes
If profit is negative, do we return the smallest negative loss?
Yes
If there are less than two prices, what do we return?
Exception
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
Zero or one price -> ValueError
No profit
[8, 5, 3, 2, 1] -> -1
General case
[5, 3, 7, 4, 2, 6, 9] -> 7

Complexity:
Time: O(n)
Space: O(1)

class Solution(object):

    def find_max_profit(self, prices):
        if prices is None:
            raise TypeError
        n = len(prices)
        if n == 0 or n == 1:
            raise ValueError
        
        minPrice = prices[0]
        ans = prices[1]-prices[0]
        for i in range(1,len(prices)):
            ans = max(ans,prices[i]-minPrice)
            minPrice = min(minPrice,prices[i])
        return ans
            
            
