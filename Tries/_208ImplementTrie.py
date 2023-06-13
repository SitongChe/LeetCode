#https://leetcode.com/problems/implement-trie-prefix-tree/
#time O(L), where L is the length of the word or prefix being processed; space O(N*M), where N is the number of words and M is the average length of the words.
class TreeNode:
    def __init__(self):
        self.isWord = False
        self.chars = {}

class Trie:
    def __init__(self):
        self.root = TreeNode()
        
    def insert(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.chars:
                cur.chars[w]=TreeNode()
            cur = cur.chars[w]
        cur.isWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w not in cur.chars:
                return False
            cur = cur.chars[w]
        return cur.isWord
        
    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w not in cur.chars:
                return False
            cur = cur.chars[w]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
