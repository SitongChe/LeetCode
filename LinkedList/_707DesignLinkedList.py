#https://leetcode.com/problems/design-linked-list/description/
#time O(1) O(index), space O(1)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, index: int) -> int:
        cur = self.head
        for i in range(index):
            if not cur:
                return -1
            cur = cur.next
        if not cur or not cur.next or cur.next == self.tail:
            return -1
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        prev = self.head
        next = self.head.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
        

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        prev = self.tail.prev
        next = self.tail
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        for i in range(index):
            if not cur:
                return
            cur = cur.next
        if not cur or not cur.next:
            return
        node = ListNode(val)
        prev = cur
        next = cur.next
        node.prev = prev
        node.next = next
        prev.next = node
        next.prev = node
        
        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for i in range(index):
            if not cur:
                return
            cur = cur.next
        if not cur or not cur.next or cur.next == self.tail:
            return
        prev = cur
        next = cur.next.next
        prev.next = next
        next.prev = prev
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
