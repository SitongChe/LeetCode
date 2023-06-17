#https://leetcode.com/problems/text-justification/description/
#time O(n) space O(n)
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def justifyLastLine(words):
            lastLine = " ".join(words)
            return lastLine+" "*(maxWidth-len(lastLine))
        def justifySingleLine(words):
            if len(words)==1:
                return justifyLastLine(words)
            line_length = sum(len(word) for word in words)
            spaceTotal = maxWidth-line_length
            numOfSlot = len(words)-1
            spaceEach = spaceTotal//numOfSlot
            spaceExtra = spaceTotal % numOfSlot
            line = words[0]
            for i in range(1,numOfSlot+1):
                space = spaceEach + (1 if spaceExtra>0 else 0)
                line +=  " "*(space) + words[i]
                spaceExtra-=1
            return line
        n = len(words)
        ans = []
        total = 0
        tmp = []
        while words:
            cur = words.pop(0)
            m = len(cur)
            if total+m > maxWidth:
                ans.append(justifySingleLine(tmp))
                tmp = []
                total =0
            total += m+1
            tmp.append(cur)

        if tmp:
            ans.append(justifyLastLine(tmp))
        return ans
