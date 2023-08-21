#Problem: Generate a list of primes.

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
20 -> [False, False, True, True, False, True, False, True, False, False, False, True, False, True, False, False, False, True, False, True]

Complexity:
Time: O(n log log n)
Space: O(n)

for each prime, it eliminates its multiples, which takes roughly O(n / p) time, where p is the prime. Considering that there are about n / log n primes up to n, the total time complexity becomes O(n / 2 + n / 3 + n / 5 + ...) ≈ O(n log log n).

import math
class PrimeGenerator(object):
    def _next_prime(self,ans,prime):
        for i in range(prime+1,len(ans)):
            if ans[i]==True:
                return i
        return len(ans)
    
    def _cross_off(self,ans,prime):
        for i in range(prime * prime, len(ans), prime):
            ans[i] = False
        
    def generate_primes(self, max_num):
        if max_num is None or not isinstance(max_num,int):
            raise TypeError
        ans = [True]*max_num
        ans[0]=False
        ans[1]=False
        prime = 2
        while prime <= math.sqrt(max_num):
            self._cross_off(ans,prime)
            prime = self._next_prime(ans,prime)
        return ans
