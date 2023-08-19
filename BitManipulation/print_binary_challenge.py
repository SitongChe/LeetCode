#Problem: Given a real number between 0 and 1, print the binary representation. If the length of the representation is > 32, return 'ERROR'.

Constraints
Is the input a float?
Yes
Is the output a string?
Yes
Is 0 and 1 inclusive?
No
Does the result include a trailing zero and decimal point?
Yes
Is the leading zero and decimal point counted in the 32 char limit?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> 'ERROR'
Out of bounds (0, 1) -> 'ERROR'
General case
0.625 -> 0.101
0.987654321 -> 'ERROR'

Complexity:
Time: O(1)
Space: O(1)

class Bits(object):

    def print_binary(self, num):
        if num is None:
            return "ERROR"
        if num<=0 or num>=1:
            return "ERROR"
        ans = 0
        cur = 1
        bit = 1
        for i in range(32):
            if num == 0:
                return str(ans)
            cur /= 2
            bit /= 10
            if num>=cur:
                ans+=bit
                num-=cur
        return "ERROR"
