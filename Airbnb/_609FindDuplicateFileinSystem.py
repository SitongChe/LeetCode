#https://leetcode.com/problems/find-duplicate-file-in-system/description/
#time O(n * m) space O(n * m)
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contents = defaultdict(list)
        for path in paths:
            parts = path.split(" ")
            directory = parts[0]
            for i in range(1,len(parts)):
                name, content = parts[i].split("(")
                contents[content].append(directory+"/"+name)
        ans = []
        for c,p in contents.items():
            if len(p)>1:
                ans.append(p)
        return ans
                
