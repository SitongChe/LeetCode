#https://leetcode.com/problems/asteroid-collision/description/
#time O(N) space O(N)
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n == 0:
            return []
        stack = []
        for asteroid in asteroids:
            while stack and stack[-1]>0 and asteroid<0:
                if abs(stack[-1])<abs(asteroid):
                    stack.pop()
                elif abs(stack[-1])==abs(asteroid):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack
