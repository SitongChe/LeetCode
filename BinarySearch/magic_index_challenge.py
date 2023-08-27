#Problem: Find the magic index in an array, where array[i] = i.

Constraints
Is the array sorted?
Yes
Are the elements in the array distinct?
No
Does a magic index always exist?
No
If there is no magic index, do we just return -1?
Yes
Are negative values allowed in the array?
Yes
If there are multiple magic values, what do we return?
Return the left-most one
Can we assume this fits memory?
Yes

Test Cases
None input -> -1
Empty array -> -1
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
Result: 2
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
Result: 6
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
Result: -1

Complexity:
Time: O(log(n))
Space: O(log(n))

class MagicIndex(object):
    def find(self,array,left,right):
        if left>right:
            return -1
        mid = left+(right-left)//2
        if array[mid]==mid:
            return mid
        leftAns=self.find(array,left,min(mid-1,array[mid]))
        if leftAns != -1:
            return leftAns
        rightAns=self.find(array,max(mid+1,array[mid]),right)
        return rightAns

    def find_magic_index(self, array):
        if array is None or not array:
            return -1
        left = 0
        right = len(array)-1
        return self.find(array,left,right)
