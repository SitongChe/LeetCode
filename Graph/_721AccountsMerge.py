#https://leetcode.com/problems/accounts-merge/description/
#time O(A * E) space O(A + E)
#union find
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = {}
        def find(x):
            uf.setdefault(x,x)
            if x!=uf[x]:
                uf[x]=find(uf[x])
            return uf[x]
        def union(x,y):
            rootx = find(x)
            rooty = find(y)
            uf[rootx] = rooty
        ownerByEmail = {}
        for i,account in enumerate(accounts):
            for j,email in enumerate(account):
                if j == 0:
                    continue
                if email in ownerByEmail:
                    union(ownerByEmail[email],i)
                ownerByEmail[email] = i
        ans = defaultdict(list)
        for email, owner in ownerByEmail.items():
            ans[find(owner)].append(email)
        return [ [accounts[key][0]]+sorted(val) for key,val in ans.items()]



        
