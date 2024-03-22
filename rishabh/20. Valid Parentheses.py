class Solution:
    '''
    APPROACH-1: USING STACK, with hashmap
    TIME: O(N)
    SPACE: O(N)
    '''
    def isValid_approach_1(self, s: str) -> bool:
        """
        Check if the given string has valid parentheses using stack with a hashmap.

        Parameters:
        s (str): The input string containing parentheses.

        Returns:
        bool: True if the parentheses are valid, False otherwise.
        """
        parenthesis = {
                    ")" : "(", 
                    "}" : "{", 
                    "]" : "["
                    }
        open_ = {"(", "{", "["}
        close = {")", "}", "]"}

        stack = []
        for c in s:
            if c in open_:
                stack.append(c)
            elif c in close:
                if not stack or stack[-1] != parenthesis[c]:   # if stack is empty or top of stack is not equal to the counterpart of current char => False
                    return False                               
                stack.pop()                                    # if stack has some values and if top of stack is the counterpart for current char => pop
                    
        return len(stack) == 0


    '''
    APPROACH-2: USING STACK, if-else chain
    TIME: O(N)
    SPACE: O(N)
    '''
    def isValid_approach_2(self, s: str) -> bool:
        """
        Check if the given string has valid parentheses using stack with if-else chain.

        Parameters:
        s (str): The input string containing parentheses.

        Returns:
        bool: True if the parentheses are valid, False otherwise.
        """
        stack = []

        # open => push
        # close => compare with top
        #          if top is empty, invalid
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if len(stack) == 0:
                    return False
                if char == ")" and stack[-1] == "(":
                    stack.pop()
                    continue
                elif char == "}" and stack[-1] == "{":
                    stack.pop()
                    continue
                elif char == "]" and stack[-1] == "[":
                    stack.pop()
                    continue
                else:
                    return False    

        # if traversed the whole str and stack is empty => valid parenthesis
        return len(stack) == 0

# Unit Tests

import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_valid_parentheses_approach_1(self):
        self.assertTrue(self.sol.isValid_approach_1("()"))
        self.assertTrue(self.sol.isValid_approach_1("()[]{}"))
        self.assertTrue(self.sol.isValid_approach_1("{[]}"))
        self.assertFalse(self.sol.isValid_approach_1("(]"))
        self.assertFalse(self.sol.isValid_approach_1("([)]"))
        self.assertFalse(self.sol.isValid_approach_1("]"))

    def test_valid_parentheses_approach_2(self):
        self.assertTrue(self.sol.isValid_approach_2("()"))
        self.assertTrue(self.sol.isValid_approach_2("()[]{}"))
        self.assertTrue(self.sol.isValid_approach_2("{[]}"))
        self.assertFalse(self.sol.isValid_approach_2("(]"))
        self.assertFalse(self.sol.isValid_approach_2("([)]"))
        self.assertFalse(self.sol.isValid_approach_2("]"))

if __name__ == "__main__":
    unittest.main()
