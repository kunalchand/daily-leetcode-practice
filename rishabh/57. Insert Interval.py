# https://leetcode.com/problems/insert-interval/description/
from typing import List

class Solution:
    '''
    APPROACH-1: check if green and orange overlap, add to list, pop for next iteration
    orange: given intervals
    green: new interval
    TIME: O(N)
    SPACE: O(1)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # return boolean, start, end of merged interval
        def valid_overlap(interval1, interval2):
            flag, S, E = False, -1, -1
            s1, e1 = interval1[0], interval1[1] # orange
            s2, e2 = interval2[0], interval2[1] # green

            # if there is left/right partial overlap OR whole green lies inside orange
            if s1 <= s2 <= e1 or s1 <= e2 <= e1:
                flag, S, E = True, min(s1,s2), max(e1,e2)

            # whole orange lies inside green
            elif s2 <= s1 <= e2 and s2 <= e1 <= e2:
                flag, S, E = True, s2, e2

            return flag, S, E

        res = []        
        res.append(newInterval)
        for curr_interval in intervals:
            tail = res.pop()
            # check if there's any valid overlap btw curr_interval and last_appended_interval
            overlap, start, end = valid_overlap(curr_interval, tail)
            # if there is overlap, append the merged interval
            if overlap: res.append([start, end])
            # if there is no overlap, simply insert the intervals in order
            else:
                # if the last_added_interval in res is behind the current interval, add last_added_interval
                if tail[1] <= curr_interval[0]: res.extend([tail, curr_interval])
                # if curr_interval is behind last_added_interval, add curr_interval first
                elif curr_interval[1] <= tail[0]: res.extend([curr_interval, tail])
        return res


    '''
    APPROACH-2: add valid intervals to list as you traverse through the list
    non-overlapping conditions:
        check if new_interval is on the left of curr_interval, if yes, then add new_interval to res and all the remaining intervals to res and return
        check if new_interval is on the right of curr_interval, if yes, then add curr_interval to res and continue the loop
    overlapping condition:
        make a merged_interval and continue the loop. Don't add to res yet, it may grow in size 
        add to res when whole loop is traversed
    TIME: O(N)
    SPACE: O(1)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for idx, curr_interval in enumerate(intervals):
            # Non-overlapping condition-1: if new_interval is on the left of curr_interval
            if newInterval[1] < curr_interval[0]:
                res.append(newInterval)
                return res + intervals[idx:]
            # Non-overlapping condition-2: if new_interval is on the right of curr_interval
            elif curr_interval[1] <  newInterval[0]:
                res.append(curr_interval)
            # Overlap
            else: 
                merged_interval = [min(curr_interval[0], newInterval[0]), max(curr_interval[1], newInterval[1])]
                newInterval = merged_interval
        
        res.append(newInterval)     # if non-overlapping condition-1 is never true
        return res

    '''
    APPROACH-3: insert new_interval at the relevant position
    use the concept of merge intervals(https://leetcode.com/problems/merge-intervals/description/) to make the output
    TIME: O(N)
    SPACE: O(1)
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left, idx = 0, -1
        for idx, curr_interval in enumerate(intervals):
            if newInterval[left] < curr_interval[left]:                         # add interval to its correct position
                intervals.insert(idx, newInterval)
                break
        if idx == len(intervals) - 1: intervals.append(newInterval)             # if pointer reaches end, append new interval at end
        return self.merge(intervals)

    def merge(self, sorted_intervals: List[List[int]]) -> List[List[int]]:
        # sort
        # traverse
            # keep increasing the blob if overlap
            # add blob to res if found a break and start a new blob
            # keep doing this till reached end
        # intervals.sort(key=lambda x:x[0])
        left, right = 0,1
        res, cloud = [], sorted_intervals[0]

        for idx in range(1, len(sorted_intervals)):
            curr_interval = sorted_intervals[idx]
            # overlap
            if cloud[right] >= curr_interval[left]:                                 # cloud is coming over the curr_interval 
                cloud = [cloud[left], max(cloud[right], curr_interval[right])]      # merge curr_interval into cloud
            else:   # no overlap
                res.append(cloud)
                cloud = curr_interval

        res.append(cloud)
        return res 



# intervals, newInterval = [[1,3],[6,9]], [2,5]
intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
# print(Solution().insert(intervals, newInterval))
print(Solution().insert3(intervals, newInterval))
