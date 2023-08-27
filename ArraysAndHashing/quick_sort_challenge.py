#Problem: Implement quick sort.

Constraints
Is a naive solution sufficient (ie not in-place)?
Yes
Are duplicates allowed?
Yes
Can we assume the input is valid?
No
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
Empty input -> []
One element -> [element]
Two or more elements

Complexity:
Time: O(nlogn)
Space: O(n)

class QuickSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError
        if not data:
            return []
        n = len(data)
        if n == 1:
            return data
        left = []
        right = []
        middle = []
        pivot_index = n//2
        pivot_value = data[pivot_index]
        for d in data:
            if d<pivot_value:
                left.append(d)
            elif d==pivot_value:
                middle.append(d)
            else:
                right.append(d)
        return self.sort(left)+middle+self.sort(right)
