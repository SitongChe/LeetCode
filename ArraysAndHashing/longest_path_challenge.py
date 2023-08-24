#Problem: Find the longest absolute file path.

Constraints
Is the input a string?
Yes
Can we assume the input is valid?
No
Will there always be a file in the input?
Yes
Is the output an int?
Yes
Can we assume this fits memory?
Yes

Test Cases
None -> TypeError
'' -> 0
'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext' -> 32

Complexity:
Time: O(n)
Space: O(n)

class Solution(object):

    def length_longest_path(self, file_system):
        if file_system is None:
            raise TypeError('file_system cannot be None')
        max_len = 0
        path_len = {0: 0}
        for line in file_system.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                max_len = max(max_len, path_len[depth] + len(name))
            else:
                path_len[depth + 1] = path_len[depth] + len(name) + 1
        return max_len
