from typing import List

'''
I/O:
-ve?            X
sorted ? =>     discussed that it doesn't matter
no duplicates


[2], t = 1 => []

    Approaches:
        backtracking
            pure recursion
            iterative recursion


    TIME: O(N ^ (T/M))  NOT SURE, CONFIRM THIS
    SPACE: O(T/M), T: target value, M: minimum value, t:10, m: 2 => [2,2,2,2,2]

    In both cases it will create a tree which is densely populated at left
    as you move right it'll have fewer and fewer branches

    from a current node you can only go to the branches of itself and next elements 
    not a complete tree where every node has same number of branches
    only the leftmost path will have the branches = len(nums)

'''
class IterativeRecursion:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        def helper(start) -> None:
            if sum(path) > target:
                return
            if sum(path) == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                helper(i)
                path.pop()

        helper(0)
        return res

    # same as above, just uses curr_sum as argument instead of sum() in base cases
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output, l = [], len(candidates)
        curr_path = []
        
        def dfs(start, curr_sum):
            if curr_sum == target: 
                output.append(curr_path[:])
            if curr_sum > target: 
                return
            
            for idx in range(start, l):
                curr_sum += candidates[start]
                curr_path.append(candidates[idx])
                
                dfs(idx, curr_sum)
                
                curr_path.pop()
                curr_sum -= candidates[start]

        dfs(0, 0)
        return output
    
    # same as above, just uses curr_sum as outer variable instead of curr_sum as an argument
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        curr_sum = 0

        def helper(start):
            nonlocal curr_sum 

            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path.copy())
                return
            
            for i in range(start, len(nums)):
                curr_sum += nums[i]
                path.append(nums[i])
                helper(i)

                curr_sum -= nums[i]
                path.pop()

        helper(0)
        return res
    

class PureRecursion:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output, curr_path = [], []
        curr_sum = 0

        def backtrack(idx):
            nonlocal curr_sum
            
            if curr_sum == target:
                output.append(curr_path.copy())
                return
            
            if curr_sum > target or idx >= len(nums):
                return
            
            curr_path.append(nums[idx])                 # choose curr_ele
            curr_sum += nums[idx]
            backtrack(idx)                              # call for same idx (imagine left most branch for 2,2,2,2)

            curr_path.pop()                             # NOT choose curr_ele
            curr_sum -= nums[idx]
            backtrack(idx + 1)                          # call for next idx (imagine next branch). Standing at 3, I can only go to 3 and 5. Standing at 5 I can only go to 5

        backtrack(0)
        return output
    
    # SAME AS ABOVE, just passes variables as arguments instead of declaring them outside of the function
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx, curr_lst, sum_till_here):
            # base cases
            if sum_till_here == target:
                res.append(curr_lst[:])
                return
            if sum_till_here > target or idx >= len(candidates):
                return

            curr_lst.append(candidates[idx])                                # include candidate
            backtrack(idx, curr_lst, sum_till_here + candidates[idx])       # call for same idx (imagine left most branch for 2,2,2,2)
        
            curr_lst.pop()                                                  # NOT include the curr candidate
            backtrack(idx + 1, curr_lst, sum_till_here)                     # call for next idx (imagine next branch). Standing at 3, I can only go to 3 and 5. Standing at 5 I can only go to 5


        backtrack(0,[],0)
        return res
    
print(PureRecursion().combinationSum_check([2,3,5], 8))