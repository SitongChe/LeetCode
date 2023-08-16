#https://leetcode.com/problems/robot-bounded-in-circle/description/
#time O(n) space O(1)
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x,y = 0,0
        dirx,diry = 0,1
        for instruction in instructions:
            if instruction == 'G':
                x+=dirx
                y+=diry
            elif instruction == 'L':
                dirx,diry = -diry,dirx
            else:
                dirx,diry = diry,-dirx
        return (x,y)==(0,0) or (dirx,diry)!=(0,1)
