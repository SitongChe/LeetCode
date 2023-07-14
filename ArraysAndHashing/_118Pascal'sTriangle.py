#https://leetcode.com/problems/pascals-triangle/description/
#time O(n^2) ,space  O(n)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        if numRows == 0:
            return ans
        tmp = [1]
        ans.append(tmp)
        for i in range(numRows-1):
            line = [1]
            for j in range(len(tmp)-1):
                line.append(tmp[j]+tmp[j+1])
            line.append(1)
            tmp = line
            ans.append(line)
        return ans

