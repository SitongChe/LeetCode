#https://leetcode.com/problems/open-the-lock/description/
#time O(10000) space O(10000)
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def bfs(tmp):
            ans = []
            for i in range(4):
                prev = tmp[i]
                for offsite in [1,-1]:
                    cur = (int(prev)+offsite+10)%10
                    newStr = tmp[:i]+str(cur)+tmp[i+1:]
                    ans.append(newStr)
            return ans
        if "0000" in deadends:
            return -1
        visited = set(deadends)
        visited.add("0000")
        queue = ["0000"]
        step = 0
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if cur == target:
                    return step
                for newStr in bfs(cur):
                    if newStr not in visited:
                        visited.add(newStr)
                        queue.append(newStr)
            step+=1
        return -1
        


        
