class Solution:
    '''
    APPROAHC: 2 POINTERS
    use left/right_boundary and left/right pointers
    calculate trapped water between a boundary and a pointer
    at a given point, water can only be presenet if boundaries are greater than it
    move the pointer corresponding to the shorter boundary
    TIME: O(N)
    SPACE: O(1)
    '''
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1                        # left and right boundaries LB & RB
        LB, RB = height[left], height[right]
        water = 0

        while left < right:
            if LB < RB:                                         # move left pointer
                left += 1
                water += max(LB - height[left], 0)              # calculate water, 0 if val goes -ve
                LB = max(LB, height[left])                      # update LB if needed
            elif LB >= RB:
                right -= 1
                water += max(RB - height[right], 0)
                RB = max(RB, height[right])
            
        return water