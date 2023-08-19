#Problem: Flip one bit from 0 to 1 to maximize the longest sequence of 1s.

Constraints
Is the input an int, base 2?
Yes
Can we assume the input is a 32 bit number?
Yes
Do we have to validate the length of the input?
No
Is the output an int?
Yes
Can we assume the inputs are valid?
No
Can we assume we are using a positive number since Python doesn't have an >>> operator?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> Exception
All 1's -> Count of 1s
All 0's -> 1
General case
0000 1111 1101 1101 1111 0011 1111 0000 -> 10 (ten)

Complexity:
Time: O(b)
Space: O(b)

class Bits(object):
    MAX_BITS = 32
    def flip_bit(self, num):
        if num is None:
            raise TypeError
        if num == -1:
            return self.MAX_BITS
        if num == 0:
            return 1
        segments=[]
        while num:
            count = 0
            while num and num&1==0:
                count+=1
                num>>=1
            segments.append(count)
            count = 0
            while num and num&1==1:
                count+=1
                num>>=1
            segments.append(count)
        n = len(segments)
        cur = 0
        ans = 0
        for i in range(0,n,2):
            prev = segments[i-1] if i-1>=0 else 0
            next = segments[i+1] if i+1<n else 0
            if segments[i]>1:
                cur = max(prev,next)+1
            else:
                cur = prev+next+1
            ans = max(ans,cur)
        return ans
        
        
        
