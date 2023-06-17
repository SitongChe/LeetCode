
#time O(n) space O(n)
class Vector2D:
    def __init__(self, vectors):
        self.vector2D = vectors
        self.col = 0
        self.row = 0
        self.prevCol = -1
        self.prevRow = -1
        
    def next(self):
        if not self.hasNext():
            return -1
        self.prevCol = self.col
        self.prevRow = self.row
        ans = self.vector2D[self.row][self.col]
        self.col += 1
        print("current:"+str(ans) + "  prevRow:"+str(self.prevRow)+"  prevCol: "+str(self.prevCol)+"  row:"+str(self.row)+"  col:"+str(self.col))
        return ans
        
    def hasNext(self):
        self.moveCursor()
        return self.row < len(self.vector2D) and self.col < len(self.vector2D[self.row])
        
    def remove(self):
        if self.prevCol != -1 and self.prevRow != -1:
            print("removing "+str(self.vector2D[self.prevRow][self.prevCol]) )
            del self.vector2D[self.prevRow][self.prevCol]
            self.prevCol=-1
            self.prevRow=-1
            if self.col >0 :
                self.col -= 1
        
    
    def moveCursor(self):
        while self.row < len(self.vector2D) and self.col == len(self.vector2D[self.row]):
            self.col = 0
            self.row+=1
            
    
    
def main():
    vectors = [[1,2,3],[4],[5,6]]
    vector2D = Vector2D(vectors)
    vector2D.next()
    vector2D.remove()
    vector2D.next()
    vector2D.next()
    vector2D.next()
    vector2D.remove()
    vector2D.next()
    vector2D.remove()
        
if __name__ == "__main__":
    main()
