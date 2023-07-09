#https://leetcode.com/problems/maximum-number-of-balloons/description/
#time O(n) ,space  O(1)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(count['b'],count['l']//2,count['o']//2,count['a'],count['n'])
