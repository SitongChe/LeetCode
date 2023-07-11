#https://leetcode.com/problems/length-of-last-word/description/
#time O(n) ,space  O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for c in s[::-1]:
            if c == ' ':
                if count>0:
                    return count
            else:
                count+=1
        return count

