#Problem: Return all subsets of a set.

Constraints
Should the resulting subsets be unique?
Yes, treat 'ab' and 'bc' as the same
Is the empty set included as a subset?
Yes
Are the inputs unique?
No
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
* None -> None
* [] -> [[]]
* ['a'] -> [[],
            ['a']]
* ['a', 'b'] -> [[],
                 ['a'],
                 ['b'],
                 ['a', 'b']]
* ['a', 'b', 'c'] -> [[],
                      ['a'],
                      ['b'],
                      ['c'],
                      ['a', 'b'],
                      ['a', 'c'],
                      ['b', 'c'],
                      ['a', 'b', 'c']]

Time O(2^n)
Space O(n)

class Combinatoric(object):

    def find_power_set_recursive(self, input_set):
        if input_set is None:
            return None
        if not input_set:
            return [[]]
        n = len(input_set)
        ans = []
        if n == 1:
            ans.append([])
            ans.append(input_set)
            return ans
        last = input_set[-1]
        prev = self.find_power_set_recursive(input_set[:n-1])
        for i in range(len(prev)):
            ans.append(prev[i])
            ans.append(prev[i]+[last])
        return ans
            

    def find_power_set_iterative(self, input_set):
        if input_set is None:
            return None
        if not input_set:
            return [[]]
        ans = [[],[input_set[0]]]
        n = len(input_set)
        for i in range(1,n):
            size = len(ans)
            for j in range(size):
                ans.append(ans[j]+[input_set[i]])
        return ans
                
