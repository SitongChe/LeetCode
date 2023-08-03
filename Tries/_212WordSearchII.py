#https://leetcode.com/problems/word-search-ii/
#time O(m * n * L * W), space trie tree O(L * W), ans O(W)
class TreeNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False
        self.ref = 0

class Trie:
    def __init__(self):
        self.root = TreeNode()

    def addWord(self,word):
        cur = self.root
        for w in word:
            cur.ref += 1
            if w not in cur.chars:
                cur.chars[w]=TreeNode()
            cur = cur.chars[w]
        cur.ref+=1
        cur.isWord = True
    
    def removeWord(self,word):
        cur = self.root
        for w in word:
            cur.ref-=1
            cur = cur.chars[w]
        cur.ref -=1
        cur.isWord = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def traceback(i,j,cur,tmp):
            if cur.isWord:
                trie.removeWord(tmp)
                ans.append(tmp)
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or board[i][j] not in cur.chars or cur.ref <=0 :
                return

            visited.add((i,j))
            traceback(i+1,j,cur.chars[board[i][j]],tmp+board[i][j])
            traceback(i-1,j,cur.chars[board[i][j]],tmp+board[i][j])
            traceback(i,j+1,cur.chars[board[i][j]],tmp+board[i][j])
            traceback(i,j-1,cur.chars[board[i][j]],tmp+board[i][j])
            visited.remove((i,j))
        
        m = len(board)
        n = len(board[0])
        trie = Trie()
        for word in words:
            trie.addWord(word)
        ans = []
        for i in range(m):
            for j in range(n):
                visited = set()
                traceback(i,j,trie.root,"")
        return ans


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
