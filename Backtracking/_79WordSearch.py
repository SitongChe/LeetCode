#https://leetcode.com/problems/word-search/
#time O(M*N*4^k) space O(M*N)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traceback(i,j,index):
            if index == len(word):
                self.ans = True
                return
            if i<0 or i>=m or j<0 or j>=n or (i,j) in visited or board[i][j]!=word[index]:
                return
            visited.add((i,j))
            traceback(i+1,j,index+1)
            traceback(i-1,j,index+1)
            traceback(i,j+1,index+1)
            traceback(i,j-1,index+1)
            visited.remove((i,j))

        m = len(board)
        n = len(board[0])
        self.ans = False

        count = Counter()
        for i in range(m):
            count += Counter(board[i])
        if count[word[0]]>count[word[-1]]:
            word = word[::-1]
            
        for i in range(m):
            for j in range(n):
                visited = set()
                traceback(i,j,0)
                if self.ans:
                    return True
        return False

        



