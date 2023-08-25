#Problem: Implement fibonacci recursively, dynamically, and iteratively.

Constraints
Does the sequence start at 0 or 1?
0
Can we assume the inputs are valid non-negative ints?
Yes
Are you looking for a recursive or iterative solution?
Implement both
Can we assume this fits memory?
Yes

Test Cases
n = 0 -> 0
n = 1 -> 1
n = 6 -> 8
Fib sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...


class Math(object):
    mem = {}
    
Complexity:
Time: O(2^n)
Space: O(1)
    def fib_iterative(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        a = 0
        b = 1
        for _ in range(n-1):
            a,b = b,a+b
        return b
            

Complexity:
Time: O(2^n) if not using mem, O(n) if used mem
Space: O(n)
    def fib_recursive(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in self.mem:
            return self.mem[n]
        self.mem[n]=self.fib_recursive(n-1)+self.fib_recursive(n-2)
        return self.mem[n]

Complexity:
Time: O(n)
Space: O(n)
    def fib_dynamic(self, n):
        if n == 0:
            return 0
        ans = [0]*(n+1)
        ans[1]=1
        for i in range(2,n+1):
            ans[i]=ans[i-1]+ans[i-2]
        return ans[n]
