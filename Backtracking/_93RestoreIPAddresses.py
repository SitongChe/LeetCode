#https://leetcode.com/problems/restore-ip-addresses/description/
#time O(3^4) space O(4)
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def traceback(index,tmp):
            if index == n and len(tmp)==4:
                ans.append(".".join(tmp))
                return
            if len(tmp)>4:
                return
            for i in range(index,n):
                cur = s[index:i+1]
                curNum = int(cur)
                if (curNum == 0 and len(cur)==1) or (curNum<=255 and cur[0]!='0'):
                    tmp.append(cur)
                    traceback(i+1,tmp)
                    tmp.pop()

        n = len(s)
        ans = []
        traceback(0,[])
        return ans
        
