#Problem: Implement a trie with find, insert, remove, and list_words methods.

Constraints
Can we assume we are working with strings?
Yes
Are the strings in ASCII?
Yes
Should find only match exact words with a terminating character?
Yes
Should list_words only return words with a terminating character?
Yes
Can we assume this fits memory?
Yes

Test Cases

         root
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

find

* Find on an empty trie
* Find non-matching
* Find matching

insert

* Insert on empty trie
* Insert to make a leaf terminator char
* Insert to extend an existing terminator char

remove

* Remove me
* Remove mens
* Remove a
* Remove has

list_words

* List empty
* List general case

#time O(m * n + k^2), space trie tree O(m*n), ans O(k)
from collections import OrderedDict


class Node(object):

    def __init__(self, data, parent=None, terminates=False):
        self.data = data
        self.parent = parent
        self.children = {}
        self.terminates = terminates
        self.ref = 0


class Trie(object):

    def __init__(self):
        self.root = Node('')

Complexity:
Time: O(m), where m is the length of the word
Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach

    def find(self, word):
        if word is None:
            raise TypeError
        cur = self.root
        for c in word:
            if c not in cur.children:
                return None
            cur = cur.children[c]
        return cur if cur.terminates else None

Complexity:
Time: O(m), where m is the length of the word
Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
    def insert(self, word):
        if word is None:
            raise TypeError
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Node(c,cur)
            cur = cur.children[c]
            cur.ref+=1
        cur.terminates = True

    def remove(self, word):
        if not word:
            return
        cur = self.root
        for c in word:
            if c not in cur.children or cur.children[c].ref == 0:
                raise KeyError
            cur.children[c].ref-=1
            if cur.children[c].ref == 0:
                del cur.children[c]
                return
            cur = cur.children[c]
        cur.terminates = False

Complexity:
Time: O(m+h), where where m is the length of the word and h is the tree height
Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
    def remove2(self, word):
        if word is None:
            raise TypeError('word cannot be None')
        node = self.find(word)
        if node is None:
            raise KeyError('word does not exist')
        node.terminates = False
        parent = node.parent
        while parent is not None:
            # As we are propagating the delete up the
            # parents, if this node has children, stop
            # here to prevent orphaning its children.
            # Or
            # if this node is a terminating node that is
            # not the terminating node of the input word,
            # stop to prevent removing the associated word.
            if node.children or node.terminates:
                return
            del parent.children[node.key]
            node = parent
            parent = parent.parent


Complexity:
Time: O(n)
Space: O(h) for the recursion depth (tree height), or O(1) if using an iterative approach
    def bfs(self):
        queue = [(self.root,"")]
        ans = []
        while queue:
            cur,tmp = queue.pop(0)
            if cur.terminates:
                ans.append(tmp)
            for node in cur.children.values():
                queue.append((node,tmp+node.data))
        return ans
    def dfs(self,node,tmp,ans):
        if node.terminates:
            ans.append(tmp)
        for child in node.children.values():
            self.dfs(child,tmp+child.data,ans)

    def list_words(self):
        #return self.bfs()
        ans = []
        self.dfs(self.root,"",ans)
        return ans
        
