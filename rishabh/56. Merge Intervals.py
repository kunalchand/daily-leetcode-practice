from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort
        # traverse
            # keep increasing the blob if overlap
            # add blob to res if found a break and start a new blob
            # keep doing this till reached end
        intervals.sort(key=lambda x:x[0])
        res, cloud = [], intervals[0]
        left, right = 0, 1              # left and right boundaries
        
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