from typing import List
class Solution:
    '''
    APPROACH-1: cloud/blob
    sort
    traverse
        keep increasing the blob if overlap
        add blob to res if found a break and start a new blob
        keep doing this till reached end
    TIME: O(N * log N), sorting
    SPACE: O(N), res array
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res, cloud = [], intervals[0]
        left, right = 0, 1                  # left and right boundaries
        
        for idx in range(1, len(intervals)):
            curr_interval = intervals[idx]
            # overlap
            if cloud[right] >= curr_interval[left]:                               # cloud is coming over the curr_interval 
                cloud = [cloud[left], max(cloud[right], curr_interval[right])]    # merge curr_interval into cloud
            else:   # no overlap
                res.append(cloud)
                cloud = curr_interval

        res.append(cloud)
        return res 
    
    '''
    APPROACH-2: add to output[], pop/update latest value of output if merging
    TIME: O(N * log N), sorting
    SPACE: O(N), res array
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        left, right, latest = 0, 1, -1      # left and right boundaries

        intervals.sort(key=lambda x:x[0])
        output.append(intervals[0])
        for curr_interval in intervals:
            # overlap => # merge => update right boundary of the latest element in output[]
            if output[latest][right] >= curr_interval[left]:
                output[latest][right] = max(output[latest][right], curr_interval[right])
            else: # no overlap
                output.append(curr_interval)

        return output 