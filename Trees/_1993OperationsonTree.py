#https://leetcode.com/problems/operations-on-tree/description/
#time O(h) spaceO(n)

class LockingTree:

    def __init__(self, parent: List[int]):
        self.parent = parent
        self.graph = defaultdict(list)
        n = len(parent)
        self.status = [[False,-1] for i in range(n)]
        for i in range(1,n):
            self.graph[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        if self.status[num][0]:
            return False
        self.status[num]=[True,user]
        return True

    def unlock(self, num: int, user: int) -> bool:
        if not self.status[num][0] or self.status[num][1]!=user:
            return False
        self.status[num]=[False,-1]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        cur = num
        while cur!=-1:
            if self.status[cur][0]:
                return False
            cur = self.parent[cur]
        found = False
        queue = [num]
        while queue:
            cur = queue.pop(0)
            for node in self.graph[cur]:
                if self.status[node][0]:
                    found = True
                    self.status[node]=[False,-1]
                queue.append(node)
        if found:
            self.status[num]=[True,user]
            return True
        return False

        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)
