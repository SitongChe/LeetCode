#https://practice.geeksforgeeks.org/problems/alien-dictionary/1
#time O(n * m) space O(n * m), n number of words, m length of each word
from typing import List
from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        indegree=defaultdict()
        for i in range(len(alien_dict)-1):
            word1,word2 = alien_dict[i],alien_dict[i+1]
            for j in range(min(len(word1),len(word2))):
                if word1[j]!=word2[j]:
                    graph[word1[j]].append(word2[j])
                    indegree[word2[j]]=indegree.get(word2[j], 0)+1
                    indegree[word1[j]]=indegree.get(word1[j], 0)
                    break
                
        queue = [chr(ord('a') + i) for i in range(K) if indegree.get(chr(ord('a') + i), 0)==0]
        ans = ""
        while queue:
            cur = queue.pop(0)
            ans += cur
            for node in graph[cur]:
                indegree[node]-=1
                if indegree[node]==0:
                    queue.append(node)
        
        if max([i for i in indegree.values()])==0:
            return ans
        return ""



#{
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends
