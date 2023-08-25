#Problem: Given a knapsack with a total weight capacity and a list of items with weight w(i) and value v(i), determine the max total value you can carry.

Constraints
Can we replace the items once they are placed in the knapsack?
Yes, this is the unbounded knapsack problem
Can we split an item?
No
Can we get an input item with weight of 0 or value of 0?
No
Do we need to return the items that make up the max total value?
No, just the total value
Can we assume the inputs are valid?
No
Are the inputs in sorted order by val/weight?
Yes
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
a 1 | 1
b 3 | 2
c 7 | 4

max value = 14



class Item(object):

    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)
        
class Knapsack(object):

Time O(2^n)
Space O(n)
    def fill_knapsack_1(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError
        if not input_items or not total_weight:
            return 0
        n = len(input_items)
        self.ans = 0
        def traceback(index,curWeight,curValue):
            self.ans = max(self.ans,curValue)
            for i in range(index,n):
                if input_items[i].weight+curWeight<=total_weight:
                    traceback(i+1,input_items[i].weight+curWeight,input_items[i].value+curValue)
        traceback(0,0,0)
        return self.ans
 
Complexity:
Time: O(n * w), where n is the number of items and w is the total weight
Space: O(w), where w is the total weight
    def fill_knapsack(self, items, total_weight):
        if items is None or total_weight is None:
            raise TypeError('items or total_weight cannot be None')
        if not items or total_weight == 0:
            return 0
        num_rows = len(items)
        num_cols = total_weight + 1
        T = [0] * (num_cols)
        for i in range(num_rows):
            for j in range(num_cols):
                if j >= items[i].weight:
                    T[j] = max(items[i].value + T[j - items[i].weight],
                               T[j])
        return T[-1]
            
