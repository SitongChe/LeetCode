#https://leetcode.com/problems/verifying-an-alien-dictionary/description/
#time O(L) space O(1)
#priority queue
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> str:
        orderWithIndex = {c:i for i,c in enumerate(order)}
        for i in range(len(words)-1):
            word1 = words[i]
            word2 = words[i+1]
            for j in range(len(word1)):
                if j == len(word2):
                    return False
                if word1[j]!=word2[j]:
                    if orderWithIndex[word1[j]]>orderWithIndex[word2[j]]:
                        return False
                    break
        return True
