#Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BCCD4'. Only compress the string if it saves space.

Constraints
Can we assume the string is ASCII?
Yes
Note: Unicode strings could require special handling depending on your language
Is this case sensitive?
Yes
Can we use additional data structures?
Yes
Can we assume this fits in memory?
Yes

Test Cases
None -> None
'' -> ''
'AABBCC' -> 'AABBCC'
'AAABCCDDDD' -> 'A3BCCD4'

Complexity:
Time: O(n)
Space: O(n)

1
def split_to_blocks(string):
    block = ''
    for char, next_char in zip(string, string[1:] + ' '):
        block += char
        if char is not next_char:
            yield block
            block = ''


def compress_block(block):
    if len(block) <= 2:
        return block
    else:
        return block[0] + str(len(block))


def compress_string(string):
    if string is None or not string:
        return string
    compressed = (compress_block(block) for block in split_to_blocks(string))
    result = ''.join(compressed)
    return result if len(result) < len(string) else string


2
def compress_string(string):
    if string is None or not string:
        return string
    n = len(string)
    i = 0
    ans = ""
    while i<n:
        count = 1
        while i+1<n and string[i+1]==string[i]:
            count+=1
            i+=1
        if count>2:
            ans+=string[i]
            ans+=str(count)
        elif count == 2:
            ans+=string[i]
            ans+=string[i]
        else:
            ans+=string[i]
        i+=1
    return ans
