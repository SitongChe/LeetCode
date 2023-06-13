#https://leetcode.com/problems/word-ladder/
#time O(N * K^2) space O(N * K^2) N is the number of words and K is the length of the words.
#bfs+map
from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        queue = [beginWord]
        ans = 0
        visited = set()
        visited.add(beginWord)
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                patterns[pattern].append(word)

        while queue:
            n = len(queue)
            ans += 1
            for i in range(n):
                cur = queue.pop(0)
                if cur == endWord:
                    return ans
                for j in range(len(cur)):
                    pattern = cur[:j]+"*"+cur[j+1:]
                    for word in patterns[pattern]:
                        if word not in visited:
                            queue.append(word)
                            visited.add(word)
            
        return 0
                    



