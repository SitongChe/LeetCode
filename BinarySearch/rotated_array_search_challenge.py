#Problem: Find an element in a sorted array that has been rotated a number of times.

Constraints
Is the input an array of ints?
Yes
Do we know how many times the array was rotated?
No
Was the array originally sorted in increasing or decreasing order?
Increasing
For the output, do we return the index?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
[] -> None
Not found -> None
General case with duplicates
General case without duplicates

Complexity:
Time: O(log n) if there are no duplicates, else O(n)
Space: O(1)

class Array(object):

    def search_sorted_array(self, array, val):
        if array is None or val is None:
            raise TypeError
        if not array:
            return None
        n = len(array)
        left = 0
        right = n-1
        while left+1<right:
            while left+1+1<right and array[left+1]==array[left]:
                left+=1
            while left+1<right-1 and array[right-1]==array[right]:
                right-=1
            mid = left+(right-left)//2
            if array[mid]==val:
                return mid
            if array[mid]>array[left]:
                if val>=array[left] and val<=array[mid]:
                    right = mid
                else:
                    left = mid
            elif array[mid]<array[left]:
                if val>=array[mid] and val<=array[right]:
                    left = mid
                else:
                    right = mid
                
        if array[left]==val:
            return left
        if array[right]==val:
            return right
        return None
