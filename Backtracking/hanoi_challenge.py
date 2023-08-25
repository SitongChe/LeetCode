#Problem: Implement the Towers of Hanoi with 3 towers and N disks.

Constraints
Can we assume we already have a stack class that can be used for this problem?
Yes
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
None tower(s) -> Exception
0 disks -> None
1 disk
2 or more disks

Time O(2^n)
Space O(n)
 class Hanoi(object):

    def move_disks(self, num_disks, src, dest, buff):
        if src is None or dest is None or buff is None:
            raise TypeError
        if num_disks == 0:
            return
        self.move_disks(num_disks-1, src, buff, dest)
        dest.push(src.pop())
        self.move_disks(num_disks-1, buff, dest, src)
            
