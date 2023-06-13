from Graph._127WordLadder import Solution

def main():
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    
    solution = Solution()
    length = solution.ladderLength(beginWord, endWord, wordList)
    print("Shortest transformation length:", length)

if __name__ == "__main__":
    main()
