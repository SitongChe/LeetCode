#https://leetcode.com/problems/multiply-strings/description/
#time O(n * m) space O(n + m)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        m = len(num1)
        n = len(num2)
        ans = [0]*(m+n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                pos1 = i + j
                pos2 = pos1 + 1
                product += ans[pos2]
                ans[pos1] += product // 10
                ans[pos2] = product % 10
        i = 0
        while i < len(ans) and ans[i] == 0:
            i += 1
        return "".join(map(str, ans[i:]))
