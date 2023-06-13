#https://leetcode.com/problems/word-search/
#time O(M*N*4^k) space O(M*N)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def traceback(i,j,visited,index):
            if i<0 or i>=m or j<0 or j>=n or visited[i][j] or board[i][j]!=word[index]:
                return
            if index == len(word)-1:
                self.ans = True
                return
            visited[i][j]=True
            traceback(i+1,j,visited,index+1)
            traceback(i-1,j,visited,index+1)
            traceback(i,j+1,visited,index+1)
            traceback(i,j-1,visited,index+1)
            visited[i][j]=False
        count = Counter()
        for i in range(m):
            count+=Counter(board[i])
        if count[word[0]]>count[word[-1]]:
            word = word[::-1]
        self.ans = False
        for i in range(m):
            for j in range(n):
                if board[i][j]==word[0]:
                    visited = [[False]*n for i in range(m)]
                    traceback(i,j,visited,0)
                    if self.ans == True:
                        return True
        return False


                    



