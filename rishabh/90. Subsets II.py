from typing import List

'''
notice the base conditions 
APPROACH - 1
according to your binary tree you'll find the ans at leaf nodes
hence idx reaching end is imp, not the len(curr_path)
                []
              /    \
           /          \
          1              []
        /  \            /  \
      2     []        2     []
      /\    /\        /\    /\
     2 []  2  []     2 []  2  []



APPROACH - 2
every unique node is an answer if draw a left skewed tree
where at every node you can only have branches forward
eg:       []                ` denotes unique nodes
        / | \
       /  |  \
      /   |   \
    1`    2     2`
   /\    /
  2  2`  2`
 /
 2`
'''
'''
    I- List [int]
     - duplicates , repeated
     - -ve, 0, +ve
     - 1 to 10

    O - all possible subsets, but not repeated

    [1,2] => {[], [1], [1,2] == [2,1]}

    APPROACH:
        sort the input first to eliminate duplicate tuples
        and use same approach as subset, just use set() to eliminate duplicates
        
        2 IMPLEMENTATIONS:
        1: complete binary tree
        2: left skewed tree

'''
class Solution:
    # complete binary tree
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        output, seen = [], set()

        def backtrack(idx, curr_path):
            if idx == len(nums):                # idx == len(nums) - 1 won't work bcz idx becomes = to len only when idx has traveresd all the available idxes, now I just want to add and return. If I add and return at len(nums) - 1, I never made the biggest subset
                if tuple(curr_path) not in seen:
                    seen.add(tuple(curr_path))
                    output.append(curr_path.copy())
                return
            
            curr_path.append(nums[idx])
            backtrack(idx + 1, curr_path)       # explore left branch by including the curr element

            curr_path.pop()                     # backtrack
            backtrack(idx + 1, curr_path)       # explore right branch by NOT including the curr element

        # why sorting is required => order in tuple matters => 414 and 144 should be same, without sorting they act different
        nums.sort()                             # if not sorted ,imagine 2 paths (1,2,3,4) and (1,3,2,4) both will be different tuples, but actually they're the same subset
        backtrack(0, [])
        return output

        
    # skewed tree
    # here the terminating condition should be different than above
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        res, seen = [], set()

        def backtrack(start, curr_path):
            if start > len(nums):
                return
            
            # add every unique node into the res
            if tuple(curr_path) not in seen:
                seen.add(tuple(curr_path))
                res.append(curr_path.copy())
                # return

            for idx in range(start, len(nums)):
                curr_path.append(nums[idx])
                backtrack(idx + 1, curr_path)
                curr_path.pop()

        nums.sort()
        backtrack(0, [])
        return res

    
nums = [1,2,2]
print(Solution().subsetsWithDup2(nums))