#Problem: Implement the method draw_line(screen, width, x1, x2) where screen is a list of bytes, width is divisible by 8, and x1, x2 are absolute pixel positions.

Constraints
Can we assume the inputs are valid?
No
For the output, do we set corresponding bits in screen?
Yes
Can we assume this fits memory?
Yes

Test Cases
Invalid inputs -> Exception
screen is empty
width = 0
any input param is None
x1 or x2 is out of bounds
General case for len(screen) = 20, width = 32:
x1 = 2, x2 = 6
screen[0] = int('00111110', base=2)
x1 = 68, x2 = 80
screen[8], int('00001111', base=2)
screen[9], int('11111111', base=2)
screen[10], int('10000000', base=2)

class BitsScreen(object):

    def draw_line_1(self, screen, width, x1, x2):
        if not screen or x1 is None or x2 is None:
            raise TypeError
        n = len(screen)
        if width == 0 or width%8 or x1>=n*8 or x2>=n*8:
            raise ValueError
        for i in range(x1,x2+1):
            screen[i//8]|=1<<(7-i%8)
            
    def draw_line(self, screen, width, x1, x2):
        if None in (screen, width, x1, x2):
            raise TypeError
        n = len(screen)
        if not screen or not width or width == 0 or width%8 or x1<0 or x2<0 or x1>x2 or x1>=n*8 or x2>=n*8:
            raise ValueError
        start_bit = x1%8
        end_bit = x2%8
        start_byte = x1//8
        end_byte = x2//8
        first_full_byte = start_byte + (1 if start_bit!=0 else 0)
        last_full_byte = end_byte - (1 if end_bit!=7 else 0)
        for byte in range(first_full_byte, last_full_byte+1):
            screen[byte]=int('11111111',base=2)
        start_mask = (1<<(8-start_bit))-1
        end_mask = int('11111111',base=2) & (~((1<<(8-end_bit-1))-1))
        if start_byte == end_byte:
            screen[start_byte]|=start_mask&end_mask
        else:
            screen[start_byte]|=start_mask
            screen[end_byte]|=end_mask
