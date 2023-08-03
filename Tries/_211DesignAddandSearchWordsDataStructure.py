#https://leetcode.com/problems/design-add-and-search-words-data-structure/
#time O(L), where L is the length of the word or prefix being processed; space O(N*M), where N is the number of words and M is the average length of the words.
class TreeNode:
    def __init__(self):
        self.isWord = False
        self.chars = {}

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.chars:
                cur.chars[w]=TreeNode()
            cur = cur.chars[w]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        def dfs(cur,index):
            for i in range(index,n):
                w = word[i]
                if w!='.':
                    if w not in cur.chars:
                        return False
                    cur = cur.chars[w]
                else:
                    for node in cur.chars.values():
                        if dfs(node,i+1):
                            return True
                    return False
            return cur.isWord
        n = len(word)
        return dfs(self.root,0)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
