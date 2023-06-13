#https://leetcode.com/problems/top-k-frequent-elements/
#time O(n + m log m) ,space  O(m) n: the length of the nums list  m: number of distinct elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = defaultdict(list)
        for key,v in count.items():
            freq[v].append(key)
        ans=[]
        for key,v in sorted(freq.items(), reverse=True):
            for vv in v:
                ans.append(vv)
                if len(ans)==k:
                    return ans
        return ans
        
