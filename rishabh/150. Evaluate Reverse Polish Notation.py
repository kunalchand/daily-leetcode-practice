import math
from typing import List

class Solution:
    '''
    Class representing a solution for evaluating Reverse Polish Notation expressions.

    Attributes:
        None

    Methods:
        perform_operation: Performs the arithmetic operation based on the given operator.
        evalRPN: Evaluates the given list of tokens in Reverse Polish Notation (RPN) format.

    Approach:
        The approach involves using a stack. 
        1. Iterate through the tokens from left to right.
        2. If the token is a digit, push it onto the stack.
        3. If the token is an operator, pop the top two elements from the stack, perform the operation, and push the result back onto the stack.
        4. Continue until all tokens are processed.
        5. The final result is the top element of the stack.

    Time Complexity:
        The time complexity of the evalRPN method is O(N), where N is the number of tokens.

    Space Complexity:
        The space complexity of the evalRPN method is O(N/2) in the worst case scenario, where N is the number of tokens.

    '''

    def perform_operation(self, first_operand, second_operand, operation):
        '''
        Performs the arithmetic operation based on the given operator.

        Parameters:
            first_operand (int): The first operand of the operation.
            second_operand (int): The second operand of the operation.
            operation (str): The operator to be applied.

        Returns:
            int: The result of the arithmetic operation.
        '''
        if operation == "+":
            return first_operand + second_operand
        elif operation == "-":
            return first_operand - second_operand
        elif operation == "*":
            return first_operand * second_operand
        elif operation == "/":
            res = first_operand / second_operand 
            if res > 0:
                return math.floor(res)
            else:
                return math.ceil(res)  # if res is negative, truncate it towards 0 not the lesser value

    def evalRPN(self, tokens: List[str]) -> int:
        '''
        Evaluates the given list of tokens in Reverse Polish Notation (RPN) format.

        Parameters:
            tokens (List[str]): The list of tokens representing the RPN expression.

        Returns:
            int: The result of evaluating the RPN expression.
        '''
        stack = []
        operators = {"+", "-", "/", "*"}                # allowed operators

        for t in tokens:
            # If t is a number
            if t not in operators:
                stack.append(int(t))
            else:
                # If t is an operator
                top = stack.pop()
                second_top = stack.pop()
                new_ele = self.perform_operation(second_top, top, t)
                stack.append(new_ele)

        return stack.pop()

    def check(self):
        '''
        Performs a check on some division operations to ensure proper floor/ceiling division behavior.
        '''
        print(5 / 2)                 # 2.5
        print(-5 / 2)                # -2.5
        print(5 // 2)                # 2
        print(-5 // 2)               # -3 => we want -2 here for above cases that's why ceil
        print(math.ceil(-5 / 2))     # -2

# Unit tests
def test_evalRPN():
    sol = Solution()
    assert sol.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert sol.evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert sol.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22

def test_perform_operation():
    sol = Solution()
    assert sol.perform_operation(5, 2, "/") == 2
    assert sol.perform_operation(-5, 2, "/") == -2

# Run unit tests
test_evalRPN()
test_perform_operation()

