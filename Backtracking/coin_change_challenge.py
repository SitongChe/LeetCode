#Problem: Determine the total number of unique ways to make n cents, given coins of denominations less than n cents.

Constraints
Do the coins have to reach exactly n cents?
Yes
Can we assume we have an infinite number of coins to make n cents?
Yes
Do we need to report the combination(s) of coins that represent the minimum?
No
Can we assume the coin denominations are given in sorted order?
No
Can we assume this fits memory?
Yes

Test Cases
coins: None or n: None -> Exception
coins: [] or n: 0 -> 0
coins: [1, 2, 3], n: 5 -> 5


#time O(2^N) space O(N)
class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            raise TypeError
        if not coins or not total:
            return 0
        n = len(coins)
        coins.sort()
        self.ans = 0
        def traceback(index,target):
            if target==0:
                self.ans+=1
                return
            if target<0:
                return
            for i in range(index,n):
                traceback(i,target-coins[i])
        traceback(0,total)
        return self.ans
        
   
Algorithm
We'll use a bottom-up dynamic programming approach.
The rows (i) represent the coin values.
The columns (j) represent the totals.

  -------------------------
  | 0 | 1 | 2 | 3 | 4 | 5 |
  -------------------------
0 | 1 | 0 | 0 | 0 | 0 | 0 |
1 | 1 | 1 | 1 | 1 | 1 | 1 |
2 | 1 | 1 | 2 | 2 | 3 | 3 |
3 | 1 | 1 | 2 | 3 | 4 | 5 |
  -------------------------

Number of ways to get total n with coin[n] equals:
* Number of ways to get total n with coin[n - 1] plus
* Number of ways to get total n - coin[n]

if j == 0:
    T[i][j] = 1
if row == 0:
    T[i][j] = 0
if coins[i] >= j
    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
else:
    T[i][j] = T[i - 1][j]

The answer will be in the bottom right corner of the matrix.

Complexity:
Time: O(i * j)
Space: O(i * j)

class CoinChanger(object):

    def make_change(self, coins, total):
        if coins is None or total is None:
            return None
        if not coins or total == 0:
            return 0
        coins = [0] + coins
        num_rows = len(coins)
        num_cols = total + 1
        T = [[None] * num_cols for _ in range(num_rows)]
        for i in range(num_rows):
            for j in range(num_cols):
                if i == 0:
                    T[i][j] = 0
                    continue
                if j == 0:
                    T[i][j] = 1
                    continue
                if coins[i] <= j:
                    T[i][j] = T[i - 1][j] + T[i][j - coins[i]]
                else:
                    T[i][j] = T[i - 1][j]
        return T[num_rows - 1][num_cols - 1]

Complexity:
Time: O(mn); let the number of coins be m. We iterate from arr[coin] -> arr[n], or ~ n operations on each coin, hence n*m.
Space: O(n)

def change_ways(n, coins):
    if n is None or coins is None:
        raise TypeError
    if n == 0:
        return 0
    ans = [1]+[0]*n
    for coin in coins:
        for i in range(coin,n+1):
            ans[i]+=ans[i-coin]
    return ans[n]
                    



