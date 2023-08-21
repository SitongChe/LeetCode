#Problem: Create a class with an insert method to insert an int to a list. It should also support calculating the max, min, mean, and mode in O(1).

Constraints
Can we assume the inputs are valid?
No
Is there a range of inputs?
0 <= item <= 100
Should mean return a float?
Yes
Should the other results return an int?
Yes
If there are multiple modes, what do we return?
Any of the modes
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
[] -> ValueError
[5, 2, 7, 9, 9, 2, 9, 4, 3, 3, 2]
max: 9
min: 2
mean: 55
mode: 9 or 2

Complexity:
Time: O(1)
Space: O(1), we are treating the 101 element array as a constant O(1), we could also see this as O(k)

from collections import defaultdict
class Solution(object):

    def __init__(self, upper_limit=100):
        self.upper_limit = upper_limit
        self.max = None
        self.min = None
        self.total = 0
        self.count = 0
        self.mean = None
        self.freq = defaultdict(int)
        self.mode = None
        self.most_freq_count = 0
        
    def insert(self, val):
        if val is None:
            raise TypeError
        self.max = max(self.max,val) if self.max else val
        self.min = min(self.min,val) if self.min else val
        self.total += val
        self.count += 1
        self.mean = self.total/self.count
        self.freq[val]+=1
        if self.freq[val] > self.most_freq_count:
            self.most_freq_count = self.freq[val]
            self.mode = val
        
        
        
