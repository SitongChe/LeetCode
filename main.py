from OpenAI._71SimplifyPath import Solution

def main():
    current = "/facebook/instagram"
    change = "../abc/def/~/aaa"
    
    solution = Solution()
    optput = solution.applyChange(current, change)
    print("output:", optput)

if __name__ == "__main__":
    main()
