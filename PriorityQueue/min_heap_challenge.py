#Problem: Implement a min heap with extract_min and insert methods.

Constraints
Can we assume the inputs are ints?
Yes
Can we assume this fits memory?
Yes

Test Cases
Extract min of an empty tree
Extract min general case
Insert into an empty tree
Insert general case (left and right insert)
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
     
extract_min(): 5

          _15_
        /      \
       20      25
      / \     /  \
     22  40

insert(2):

          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15


Key Note:
We'll use an array to represent the tree, here are the indices:
          _0_
        /     \
       1       2
      / \     / \
     3   4
To get to a child, we take 2 * index + 1 (left child) or 2 * index + 2 (right child).
For example, the right child of index 1 is 2 * 1 + 2 = 4.


Complexity:
Time: O(lg(n))
Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

class MinHeap(object):

    def __init__(self):
        self.array = []

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array)==1:
            return self.array.pop()
        
        val = self.array[0]
        self.array[0]=self.array.pop()
        self._bottom_down(0)
        return val

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, data):
        if data is None:
            raise TypeError
        self.array.append(data)
        self._bubble_up(len(self.array)-1)
        
    def _find_min_child_index(self,index):
        n = len(self.array)
        left = index*2+1
        right = index*2+2
        if right >= n and left>= n:
            return -1
        elif right>=n:
            return left
        elif left>=n:
            return right
        else:
            if self.array[left]<self.array[right]:
                return left
            return right
            
        
    def _bottom_down(self, index):
        child_index = self._find_min_child_index(index)
        if child_index == -1:
            return
        if self.array[index]>self.array[child_index]:
            self.array[index],self.array[child_index]=self.array[child_index],self.array[index]
            self._bottom_down(child_index)
        
    def _bubble_up(self, index):
        if index == 0:
            return
        parent_index = (index-1)//2
        if self.array[parent_index]>self.array[index]:
            self.array[parent_index],self.array[index]=self.array[index],self.array[parent_index]
            self._bubble_up(parent_index)
            
