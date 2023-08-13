#https://leetcode.com/problems/partition-labels/description/
#time O(n) space O(26)
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        maxIndexForChar = {}
        for i,c in enumerate(s):
            maxIndexForChar[c]=i
        n = len(s)
        curLength = 0
        goal = 0
        ans = []
        for i in range(n):
            goal = max(goal, maxIndexForChar[s[i]])
            curLength+=1
            if i==goal:
                ans.append(curLength)
                goal = 0
                curLength = 0
        return ans


        
