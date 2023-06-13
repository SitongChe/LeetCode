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
        def dfs(word,cur):
            for i in range(len(word)):
                if word[i]=='.':
                    for node in cur.chars.values():
                        if dfs(word[i+1:],node):
                            return True
                    return False
                else:
                    if word[i] not in cur.chars:
                        return False
                    cur = cur.chars[word[i]]
            return cur.isWord
        return dfs(word,self.root)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
