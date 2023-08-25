#Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine which items to select to maximize total value.

Constraints
Can we replace the items once they are placed in the knapsack?
No, this is the 0/1 knapsack problem
Can we split an item?
No
Can we get an input item with weight of 0 or value of 0?
No
Can we assume the inputs are valid?
No
Are the inputs in sorted order by val/weight?
Yes, if not we'd need to sort them first
Can we assume this fits memory?
Yes

Test Cases
items or total weight is None -> Exception
items or total weight is 0 -> 0
General case
total_weight = 8
items
  v | w
  0 | 0
a 2 | 2
b 4 | 2
c 6 | 4
d 9 | 5

max value = 13
items
  v | w
b 4 | 2
d 9 | 5

Time O(2^n)
Space O(n)

class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)
        
class Knapsack(object):

    def fill_knapsack(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError
        if not input_items or not total_weight:
            return 0
        n = len(input_items)
        self.maxValue = 0
        self.ans = []
        input_items.sort(key = lambda x:x.weight, reverse=True)
        def traceback(index,curWeight,curValue,tmp):
            if self.maxValue<curValue:
                self.maxValue = curValue
                self.ans = tmp.copy()
            for i in range(index,n):
                if curWeight + input_items[i].weight <= total_weight:
                    tmp.append(input_items[i])
                    traceback(i+1,curWeight + input_items[i].weight,curValue + input_items[i].value,tmp)
                    tmp.pop()
        traceback(0,0,0,[])
        return self.ans
        
