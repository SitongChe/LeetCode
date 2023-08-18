#Problem: Determine the number of bits to flip to convert int a to int b'.

Constraints
Can we assume A and B are always ints?
Yes
Is the output an int?
Yes
Can we assume A and B are always the same number of bits?
Yes
Can we assume the inputs are valid (not None)?
No
Can we assume this fits memory?
Yes

Test Cases
A or B is None -> Exception
General case
  A = 11101
  B = 01111
  Result: 2

Time and Space complexity all O(1)

class Bits(object):

Time O(len(a))
Space O(1)
    def count_1(self,a):
        ans = 0
        while a:
            ans+=a&1
            a>>=1
        return ans
        
Time O(ans)
Space O(1)
    def count(self,a):
        ans = 0
        while a:
            ans+=1
            a &= a-1
        return ans

Time O(1)+O(count)
Space O(1)
    def bits_to_flip(self, a, b):
        if a is None or b is None:
            raise TypeError
        ans = a^b
        return self.count(ans)
