#https://leetcode.com/problems/palindrome-pairs/description/
#time O(n * m^2) space O(n * m), n number of words, m length of each word
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(word):
            return word == word[::-1]

        n = len(words)
        ans = []
        reversedWordIndexDict = {word[::-1]:i for i,word in enumerate(words)}
        for i in range(n):
            m = len(words[i])
            for j in range(m+1):
                left = words[i][:j]
                right = words[i][j:]
                if isPalindrome(left) and right in reversedWordIndexDict and reversedWordIndexDict[right]!=i:
                    ans.append([reversedWordIndexDict[right],i])
                if j!=m and isPalindrome(right) and left in reversedWordIndexDict and reversedWordIndexDict[left]!=i:
                    ans.append([i,reversedWordIndexDict[left]])
        return ans
