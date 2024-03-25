from typing import List
class Solution:
    '''
    I/P: int array of temp, +ve, repeat
        min len = 1
    O/P: same len as input (int)
    Clarifying Questions:
        same ? => not considered as warmer
    APPROACH:
        using monotonic stack
        (finding next/previous greater/smaller element)
        we pop whenever this behaviour changes

        going right to left pushing values on stack
        top of stack will store the max temp for curr idx
        if val >= top of stack
            pop until curr is greater than top
        push if curr_val is smaller than top

        stack grows high value to low value
        temp = [1.5,1,2,3,4,5]
        stack = 
        top  [1] -> [1.5]
                    [2]
                    [3]
                    [4]
        base        [5]  
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        t = len(temp)                                                           #     idx [0], [1]
        monotonic_stack = []                                                    # f = [[temp, idx]]
        ans = [0 for _ in range(t)]

        for i in range(t - 1, -1, -1):                                          # going right to left
            curr_temp = temp[i]
            while monotonic_stack and curr_temp >= monotonic_stack[-1][0]:      # take temp from stack, at 
                monotonic_stack.pop() 

            if monotonic_stack:
                ans[i] = monotonic_stack[-1][1] - i                             # take idx from stack
            else:
                ans[i] = 0                                                      # don't acutally need it, initialized val is 0, writing for clarity
            
            monotonic_stack.append([curr_temp, i])
        return ans