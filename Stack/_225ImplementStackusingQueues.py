#https://leetcode.com/problems/implement-stack-using-queues/description/
#time O(n) space O(N)
class MyStack:

    def __init__(self):
        self.queue = []
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        tmpQueue = []
        while len(self.queue)>1:
            tmpQueue.append(self.queue.pop(0))
        ans = self.queue.pop(0)
        self.queue = tmpQueue
        return ans
        

    def top(self) -> int:
        tmpQueue = []
        while len(self.queue)>1:
            tmpQueue.append(self.queue.pop(0))
        ans = self.queue[0]
        tmpQueue.append(self.queue.pop(0))
        self.queue = tmpQueue
        return ans
        

    def empty(self) -> bool:
        return len(self.queue)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
