#Problem: Check if a number is prime.

Constraints
Is it correct that 1 is not considered a prime number?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
Not an int -> Exception
Less than 2 -> False
General case


Complexity:
Time: O(n) where n is the value of the input number
Space: O(1)

import math
class Math(object):

    def check_prime(self, num):
        if num is None:
            raise TypeError
        if not isinstance(num, int):
            raise TypeError("Input must be an integer")
        if num < 2:
            return False
        for i in range(2,int(math.sqrt(num)+1)):
            if num%i==0:
                return False
        return True
