#https://leetcode.com/problems/snakes-and-ladders/description/
#time O(N^2) space O(N^2)
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def squareToPos(square):
            i = (square-1)//n
            j = (square-1)%n
            if i%2:
                j = n-1-j
            i = n-1-i
            return [i,j]
        queue = [1]
        move = 0
        visited = set()
        while queue:
            size = len(queue)
            for _ in range(size):
                square = queue.pop(0)
                if square == n*n:
                    return move
                for k in range(1,7):
                    nextSquare = square+k
                    if nextSquare in visited:
                        continue
                    if nextSquare>n*n:
                        continue
                    visited.add(nextSquare)
                    nexti,nextj = squareToPos(nextSquare)
                    if board[nexti][nextj]!=-1:
                        nextSquare = board[nexti][nextj]
                    queue.append(nextSquare)
            move+=1
        return -1
