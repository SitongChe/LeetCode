#https://leetcode.com/problems/design-browser-history/description/
#time O(1) O(steps), space O(1)
class ListNode:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode("head")
        self.tail = ListNode("tail")
        node = ListNode(homepage)
        self.head.next = node
        self.tail.prev = node
        node.prev = self.head
        node.next = self.tail
        self.cur = node

    def visit(self, url: str) -> None:
        node = ListNode(url)
        prev = self.cur
        next = self.tail
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
        self.cur = node
        
    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.prev == self.head:
                return self.cur.val
            self.cur = self.cur.prev
        return self.cur.val
            
    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.cur.next == self.tail:
                return self.cur.val
            self.cur = self.cur.next
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
