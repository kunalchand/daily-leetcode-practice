'''
APPROACH-1: store min-val in the same stack
'''
class MinStackApproach1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = [(None, float('inf'))] # [(curr_val, min_val)]

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        
        Parameters:
        val (int): The element to be pushed onto the stack.
        """
        self.stack.append((val, min(val, self.getMin())))
            
    def pop(self) -> None:
        """
        Removes the element from the top of the stack.
        """
        self.stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        
        Returns:
        int: The top element of the stack.
        """
        return self.stack[-1][0]

    def getMin(self) -> int:
        """
        Get the minimum element from the stack.
        
        Returns:
        int: The minimum element in the stack.
        """
        return self.stack[-1][1]
        

'''
APPROACH-2: Make another stack that will keep track of min-vals
'''
class MinStackApproach2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = [float('inf')]
        

    def push(self, val: int) -> None:
        """
        Push element val onto stack.
        
        Parameters:
        val (int): The element to be pushed onto the stack.
        """
        self.stack.append(val)
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)
        

    def pop(self) -> None:
        """
        Removes the element from the top of the stack.
        """
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        """
        Get the top element of the stack.
        
        Returns:
        int: The top element of the stack.
        """
        return self.stack[-1]
        

    def getMin(self) -> int:
        """
        Get the minimum element from the stack.
        
        Returns:
        int: The minimum element in the stack.
        """
        return self.min_stack[-1]
        

# Unit Tests

import unittest

class TestMinStack(unittest.TestCase):
    def test_approach_1(self):
        min_stack = MinStackApproach1()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)   # returns -3
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)      # returns 0
        self.assertEqual(min_stack.getMin(), -2)   # returns -2

    def test_approach_2(self):
        min_stack = MinStackApproach2()
        min_stack.push(-2)
        min_stack.push(0)
        min_stack.push(-3)
        self.assertEqual(min_stack.getMin(), -3)   # returns -3
        min_stack.pop()
        self.assertEqual(min_stack.top(), 0)      # returns 0
        self.assertEqual(min_stack.getMin(), -2)   # returns -2

if __name__ == "__main__":
    unittest.main()
