#Problem: Find all valid combinations of n-pairs of parentheses.

Constraints
Is the input an integer representing the number of pairs?
Yes
Can we assume the inputs are valid?
No
Is the output a list of valid combinations?
Yes
Should the output have duplicates?
No
Can we assume this fits memory?
Yes

Test Cases
* None -> Exception
* Negative -> Exception
* 0 -> []
* 1 -> ['()']
* 2 -> ['(())', '()()']
* 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']


Complexity:
Time: O(4^n/n^(3/2)), see Catalan numbers - 1, 1, 2, 5, 14, 42, 132...
Space complexity: O(n), due to the implicit call stack storing a maximum of 2n function calls)

class Parentheses(object):
    def find(self,left,right,tmp):
        if left == 0 and right == 0:
            self.ans.append(tmp)
            return
        if left:
            self.find(left-1,right,tmp+"(")
        if right>left:
            self.find(left,right-1,tmp+")")
        

    def find_pair(self, num_pairs):
        if num_pairs is None:
            raise TypeError
        if num_pairs < 0:
            raise ValueError
        if num_pairs == 0:
            return []
        self.ans = []
        self.find(num_pairs,num_pairs,"")
        return self.ans
            
