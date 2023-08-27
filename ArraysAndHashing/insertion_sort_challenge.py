#Problem: Implement insertion sort.

Constraints
Is a naive solution sufficient?
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
Time: O(n^2) average, worst. O(1) best if input is already sorted
Space: O(1) for the iterative solution

class InsertionSort(object):

    def sort(self, data):
        if data is None:
            raise TypeError
        if not data:
            return []
        n = len(data)
        for i in range(1,n):
            for j in range(i):
                if data[j]>data[i]:
                    break
            data[j+1:i+1]=data[j:i]
            data[j]=data[i]
        return data
