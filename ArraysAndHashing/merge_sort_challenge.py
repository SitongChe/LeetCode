#Problem: Implement merge sort.

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
Left and right subarrays of different lengths

Complexity:
Time: O(n log(n))
Space: O(n)

class MergeSort(object):
    def merge(self,a,b):
        if not a:
            return b
        if not b:
            return a
        ans = []
        i = 0
        j = 0
        while i<len(a) and j<len(b):
            curA = a[i]
            curB = b[j]
            if curA<curB:
                ans.append(curA)
                i+=1
            else:
                ans.append(curB)
                j+=1
        if i<len(a):
            ans.extend(a[i:])
        if j<len(b):
            ans.extend(b[j:])
        return ans

    def sort(self, data):
        if data is None:
            raise TypeError
        if not data:
            return []
        n = len(data)
        if n == 1:
            return data
        a = self.sort(data[:n//2])
        b = self.sort(data[n//2:])
        return self.merge(a,b)
        
