#https://leetcode.com/problems/word-ladder/
#time O(N * K^2) space O(N * K^2) N is the number of words and K is the length of the words.
#bfs+map
from typing import List
from collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        patterns = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                patterns[pattern].append(word)
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)
        ans = 1
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.pop(0)
                if cur == endWord:
                    return ans
                for i in range(len(cur)):
                    pattern = cur[:i]+"*"+cur[i+1:]
                    for word in patterns[pattern]:
                        if word not in visited:
                            visited.add(word)
                            queue.append(word)
            ans += 1
        return 0
            
                    



