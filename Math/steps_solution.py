#Problem: You are running up n steps. If you can take a single, double, or triple step, how many possible ways are there to run up to the nth step?

Constraints
If n == 0, what should the result be?
Go with 1, but discuss different approaches
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None or negative input -> Exception
n == 0 -> 1
n == 1 -> 1
n == 2 -> 2
n == 3 -> 4
n == 4 -> 7
n == 10 -> 274

Complexity:
Time: O(n), if using memoization
Space: O(n), where n is the recursion depth

class Steps(object):
    mem = {}
    def count_ways(self, num_steps):
        if num_steps is None:
            raise TypeError
        if num_steps < 0:
            raise TypeError
        if num_steps == 0:
            return 1
        if num_steps == 1:
            return 1
        if num_steps == 2:
            return 2
        if num_steps in self.mem:
            return self.mem[num_steps]
        self.mem[num_steps] = self.count_ways(num_steps-1)+self.count_ways(num_steps-2)+self.count_ways(num_steps-3)
        return self.mem[num_steps]
        
            
