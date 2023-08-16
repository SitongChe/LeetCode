#https://leetcode.com/problems/detect-squares/description/
#time O(n) space O(n)
class DetectSquares:

    def __init__(self):
        self.counts = defaultdict(int)
        self.points = set()

    def add(self, point: List[int]) -> None:
        self.counts[tuple(point)]+=1
        self.points.add(tuple(point))

    def count(self, point: List[int]) -> int:
        ans = 0
        x,y = point
        for xx,yy in self.points:
            if abs(xx-x)==abs(yy-y) and xx!=x and yy!=y:
                ans+=self.counts[(xx,y)]*self.counts[(x,yy)]*self.counts[(xx,yy)]
        return ans

        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
