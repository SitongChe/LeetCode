#Problem: Implement a hash table with set, get, and remove methods.

Constraints
For simplicity, are the keys integers only?
Yes
For collision resolution, can we use chaining?
Yes
Do we have to worry about load factors?
No
Load Factor = Number of Elements / Size of Hash Table
Medium Load Factor: A load factor between 0.5 and 0.7 is often considered a good balance. The hash table is neither too sparse nor too crowded. It strikes a balance between memory efficiency and search efficiency.
Do we have to validate inputs?
No
Can we assume this fits memory?
Yes

Test Cases
get no matching key -> KeyError exception
get matching key -> value
set no matching key -> new key, value
set matching key -> update value
remove no matching key -> KeyError exception
remove matching key -> remove key, value



class Item(object):

    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

Complexity:
Time: O(1)
Space: O(1)
    def _hash_function(self, key):
        return key%self.size

Complexity:
Time: O(1)avg, O(n)worst
Space: O(1)
    def set(self, key, value):
        hashValue = self._hash_function(key)
        for i,node in enumerate(self.table[hashValue]):
            if node.key == key:
                self.table[hashValue][i].value=value
                return
        self.table[hashValue].append(Item(key,value))

Complexity:
Time: O(1)avg, O(n)worst
Space: O(1)
    def get(self, key):
        hashValue = self._hash_function(key)
        for node in self.table[hashValue]:
            if node.key == key:
                return node.value
        raise KeyError
            
Complexity:
Time: O(1)avg, O(n)worst
Space: O(1)
    def remove(self, key):
        hashValue = self._hash_function(key)
        for i,node in enumerate(self.table[hashValue]):
            if node.key == key:
                del self.table[hashValue][i]
                return
        raise KeyError
