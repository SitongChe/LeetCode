#Problem: Given sorted arrays A, B, merge B into A in sorted order.

Constraints
Does A have enough space for B?
Yes
Can the inputs have duplicate array items?
Yes
Can we assume the inputs are valid?
No
Does the inputs also include the actual size of A and B?
Yes
Can we assume this fits memory?
Yes

Test Cases
A or B is None -> Exception
index of last A or B < 0 -> Exception
A or B is empty
General case
A = [1, 3, 5, 7, 9, None, None, None]
B = [4, 5, 6]
A = [1, 3, 4, 5, 5, 6, 7, 9]

Complexity:
Time: O(m + n)
Space: O(1)

class Array(object):

    def merge_into(self, source, dest, source_end_index, dest_end_index):
        if source is None or dest is None:
            raise TypeError
        if source_end_index<0 or dest_end_index<0:
            raise ValueError
        if not source:
            return dest
        if not dest:
            return source
        i = source_end_index-1
        j = dest_end_index-1
        index = len(source)-1
        while j>=0:
            a = source[i] if i>=0 else -float("inf")
            b = dest[j]
            if a<b:
                source[index]=b
                j-=1
            else:
                source[index]=a
                i-=1
            index-=1
        return source
