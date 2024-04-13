from typing import List
class Solution:
    '''
    [1,2,10]
    [1,2,2]
    '''
    '''
    APPROACH: 
    SORTING, AND CHECK ADJACENT ELEMENT
    Greedy
    TIME: O(N LOG N)
    Intial Implementation
    '''
    '''
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1          # set first element to 1 after sorting (according to rule)

        for idx in range(1, len(arr)):
            if arr[idx] - arr[idx - 1] <= 1:            # NO NEED TO DO THIS, YOU'RE TAKING MIN IN NEXT STEP
                continue
            arr[idx] = min(arr[idx], arr[idx - 1] + 1)
        
        return max(arr)
    '''
    
    '''
    BETTER Implementation
    Why? => you were changing the array in prev, unneccesary check to skip elements
    instead just calculate a val
    '''
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0

        for n in arr:
            # at every step, either take curr_ele or the prev ele, whichever is smaller
            prev = min(n, prev + 1)  

        return prev
