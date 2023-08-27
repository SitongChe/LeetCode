#Problem: Find the longest increasing subsequence.

Constraints
Are duplicates possible?
Yes
Can we assume the inputs are integers?
Yes
Can we assume the inputs are valid?
No
Do we expect the result to be an array of the longest increasing subsequence?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
[] -> []
[3, 4, -1, 0, 6, 2, 3] -> [-1, 0, 2, 3]

Complexity:
Time: O(n)
Space: O(n)

class Subsequence(object):

    def longest_inc_subseq(self, seq):
        if seq is None:
            raise TypeError
        if not seq:
            return []
        
        stack = []
        longest_subsequence = []
        
        for num in seq:
            while stack and stack[-1] > num:
                stack.pop()
            stack.append(num)
            
            if len(stack) > len(longest_subsequence):
                longest_subsequence = stack.copy()
        
        return longest_subsequence

