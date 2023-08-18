#Problem: Implement Fizz Buzz.

Constraints
What is fizz buzz?
Return the string representation of numbers from 1 to n
Multiples of 3 -> 'Fizz'
Multiples of 5 -> 'Buzz'
Multiples of 3 and 5 -> 'FizzBuzz'
Can we assume the inputs are valid?
No
Can we assume this fits memory?
Yes

Test Cases
* None -> Exception
* < 1 -> Exception
* 15 ->
[
    '1',
    '2',
    'Fizz',
    '4',
    'Buzz',
    'Fizz',
    '7',
    '8',
    'Fizz',
    'Buzz',
    '11',
    'Fizz',
    '13',
    '14',
    'FizzBuzz'
]

Complexity:
Time: O(n)
Space: O(n)


class Solution(object):

    def fizz_buzz(self, num):
        if num is None:
            raise TypeError
        if num<1:
            raise ValueError
        ans = []
        for i in range(1,num+1):
            tmp = ""
            if i%3==0:
                tmp += "Fizz"
            if i%5==0:
                tmp+="Buzz"
            if tmp:
                ans.append(tmp)
            else:
                ans.append(str(i))
        return ans
