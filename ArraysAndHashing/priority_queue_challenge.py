#Problem: Implement a priority queue backed by an array.

Constraints
Do we expect the methods to be insert, extract_min, and decrease_key?
Yes
Can we assume there aren't any duplicate keys?
Yes
Do we need to validate inputs?
No
Can we assume this fits memory?
Yes

Test Cases
insert
insert general case -> inserted node
extract_min
extract_min from an empty list -> None
extract_min general case -> min node
decrease_key
decrease_key an invalid key -> None
decrease_key general case -> updated node


class PriorityQueueNode(object):

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue(object):

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

Complexity:
Time: O(n)
Space: O(1)
    def insert(self, node):
        n = len(self.array)
        index = n
        for i in range(n):
            if self.array[i].key>node.key:
                index = i-1
                break
        self.array = self.array[:index+1]+[node]+self.array[index+1:]

Complexity:
Time: O(1)
Space: O(1)
    def extract_min(self):
        if not self.array:
            return None
        node = self.array[0]
        del self.array[0]
        return node

Complexity:
Time: O(n)
Space: O(1)
    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj == obj:
                node.key = new_key
                return
        return None
