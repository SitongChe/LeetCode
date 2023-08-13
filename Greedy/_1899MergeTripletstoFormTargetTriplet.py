#https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/
#time O(n) space O(1)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        foundx,foundy,foundz = False,False,False
        for x,y,z in triplets:
            if x>target[0] or y>target[1] or z>target[2]:
                continue
            if x == target[0]:
                foundx = True
            if y == target[1]:
                foundy = True
            if z == target[2]:
                foundz = True
        return foundx and foundy and foundz
 
#time O(n) space O(n)
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = [[x,y,z] for x,y,z in triplets if x<=target[0] and y<=target[1] and z<=target[2]]
        if not candidates:
            return False
        if max([x for x,y,z in candidates])==target[0] and max([y for x,y,z in candidates])==target[1] and max([z for x,y,z in candidates])==target[2]:
            return True
        return False
        
