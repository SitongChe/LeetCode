#https://leetcode.com/problems/group-anagrams/
#time O(N),space O(N)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for str in strs:
            count = [0]*26
            for c in str:
                count[ord(c)-ord("a")]+=1
            map[tuple(count)].append(str)
        return [v for k,v in map.items()]


        
            


