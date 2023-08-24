#Problem: Move all zeroes in a list to the end.

Constraints
Is the input an array of ints?
Yes
Is the output a new array of ints?
No, do this in-place
Do we need to maintain ordering of non-zero values?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
* None -> TypeError
* [0, 1, 0, 3, 12] -> [1, 3, 12, 0, 0]
* [1, 0] -> [1, 0]
* [0, 1] -> [1, 0]
* [0] -> [0]
* [1] -> [1]
* [1, 1] -> [1, 1]


Complexity:
Time: O(n)
Space: O(1)

class Solution(object):

    def move_zeroes(self, nums):
        if nums is None:
            raise TypeError
        pos = 0
        for num in nums:
            if num!=0:
                nums[pos]=num
                pos+=1
        while pos<len(nums):
            nums[pos]=0
            pos+=1
            
            
