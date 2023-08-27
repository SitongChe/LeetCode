#Problem: Implement radix sort.

Constraints
Is the input a list?
Yes
Can we assume the inputs are valid?
Check for None in place of an array
Assume array elements are ints
Do we know the max digits to handle?
No
Are the digits base 10?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
[] -> []
[128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]

Complexity:
Time: O(k*n), where n is the number of items and k is the number of digits in the largest item
Space: O(k+n)
Misc:
Not in-place
Most implementations are stable
If k (the number of digits) is less than log(n), radix sort can be faster than algorithms such as quicksort.

class RadixSort(object):

    def sort(self, array, base=10):
        if array is None:
            raise TypeError
        if not array:
            return []
        maxNum = max(array)
        maxDigits = len(str(maxNum))
        cur_array=array
        for i in range(maxDigits):
            buckets = [[] for _ in range(base)]
            for a in cur_array:
                buckets[(a//(base**i))%base].append(a)
            cur_array = []
            for bucket in buckets:
                cur_array.extend(bucket)
                
        return cur_array
            
