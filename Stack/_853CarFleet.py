#https://leetcode.com/problems/car-fleet/
#time O(n log n) space O(N)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p,s) for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        stack = []
        for p,s in pairs:
            time = (target-p)/s
            if not stack or stack[-1]<time:
                stack.append(time)
        return len(stack)

