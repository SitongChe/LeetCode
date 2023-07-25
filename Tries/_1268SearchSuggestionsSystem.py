#https://leetcode.com/problems/search-suggestions-system/description/
#time O(m * n + k^2), space trie tree O(m*n), ans O(k)
class TreeNode:
    def __init__(self):
        self.chars = {}
        self.isWord = False
class Trie:
    def __init__(self):
        self.root = TreeNode()
    def insert(self,word):
        cur = self.root
        for w in word:
            if ord(w) not in cur.chars:
                cur.chars[ord(w)]=TreeNode()
            cur = cur.chars[ord(w)]
        cur.isWord = True
    def search(self,word):
        cur = self.root
        for w in word:
            if ord(w) not in cur.chars:
                return None
            cur = cur.chars[ord(w)]
        return cur
        
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        def dfs(cur,tmp,levelAns):
            if len(levelAns)==3:
                return
            if cur.isWord:
                levelAns.append(tmp)
            for w in sorted(cur.chars):
                dfs(cur.chars[w],tmp+chr(w),levelAns)

        trie = Trie()
        ans = []
        for product in products:
            trie.insert(product)
        tmp = ""
        for w in searchWord:
            tmp += w
            levelAns = []
            cur = trie.search(tmp)
            if cur:
                dfs(cur,tmp,levelAns)
            ans.append(levelAns)
        return ans

                
            

