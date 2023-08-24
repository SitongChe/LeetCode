#Problem: Find how many times a sentence can fit on a screen.

Constraints
Can we assume sentence is ASCII?
Yes
Can we assume the inputs are valid?
No
Is the output an integer?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
rows < 0 or cols < 0 -> ValueError
cols = 0 -> 0
sentence = '' -> 0
rows = 2, cols = 8, sentence = ["hello", "world"] -> 1
rows = 3, cols = 6, sentence = ["a", "bcd", "e"] -> 2
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"] -> 1


Complexity:
Time: O(rows * n), where n is the number of words in the sentence.
Space: O(1)

class Solution(object):

    def count_sentence_fit(self, sentence, rows, cols):
        if sentence is None or rows is None or cols is None:
            raise TypeError
        if rows<0 or cols<0:
            raise ValueError
        if not sentence or cols == 0 or rows == 0:
            return 0
        count = 0
        curRow = 0
        curCol = 0
        i = 0
        while curCol < cols:
            for word in sentence:
                if len(word)>cols-curCol:
                    curCol = 0
                    curRow+=1
                if curRow == rows:
                    return count
                curCol+=len(word)+1
            count+=1
        return count
        
Algorithm
It can be relatively straightforward to come up with the brute force solution, check out the method count_sentence_fit_brute_force below.
The optimized solutions is discussed in more depth here.
rows = 4
cols = 6
sentence = ['abc', 'de', 'f']

"abc de f abc de f abc de f ..." // start=0
 012345                          // start=start+cols+adjustment=0+6+1=7 (1 space removed in screen string)
        012345                   // start=7+6+0=13
              012345             // start=13+6-1=18 (1 space added)
                   012345        // start=18+6+1=25 (1 space added)
                          012345
Complexity:
Time: O(1)
Space: O(1)

class Solution(object):

    def count_sentence_fit(self, sentence, rows, cols):
        if sentence is None:
            raise TypeError('sentence cannot be None')
        if rows is None or cols is None:
            raise TypeError('rows and cols cannot be None')
        if rows < 0 or cols < 0:
            raise ValueError('rows and cols cannot be negative')
        if cols == 0 or not sentence:
            return 0
        string = ' '.join(sentence) + ' '
        start = 0
        str_len = len(string)
        for row in range(rows):
            start += cols
            # We don't need extra space for the current row
            if string[start % str_len] == ' ':
                start += 1
            # The current row can't fit, so we'll need to
            # remove characters from the next word
            else:
                while (start > 0 and string[(start - 1) % str_len] != ' '):
                    start -= 1
        return start // str_len
                
