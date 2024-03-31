#Problem: Implement a function that groups identical items based on their order in the list.

Constraints
Can we use extra data structures?
Yes

Test Cases
group_ordered([1,2,1,3,2]) -> [1,1,2,2,3]
group_ordered(['a','b','a') -> ['a','a','b']
group_ordered([1,1,2,3,4,5,2,1]-> [1,1,1,2,2,3,4,5]
group_ordered([]) -> []
group_ordered([1]) -> [1]
group_ordered(None) -> None

Complexity:
Time complexity O(n log n).
Space complexity O(n)

from collections import defaultdict
def group_ordered(list_in):
    if list_in is None:
        return None
    count = defaultdict(int)
    firstIndex = defaultdict(int)
    for i in range(len(list_in)):
        if list_in[i] not in firstIndex:
            firstIndex[list_in[i]]=i
        count[list_in[i]]+=1
    ans = []
    for key,value in sorted(firstIndex.items(), key = lambda x:x[1]):
        for j in range(count[key]):
            ans.append(key)
    return ans
    
