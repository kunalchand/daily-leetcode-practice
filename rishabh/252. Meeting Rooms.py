from typing import List
class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def is_overlap(i1, i2):
            return i1[1] > i2[0]
        
        intervals.sort(key=lambda i : i[0])
        for idx in range(len(intervals)-1):
            if is_overlap(intervals[idx], intervals[idx+1]): return False
        
        return True
    
print(Solution().canAttendMeetings([[1,2],[2,3],[1,5]]))
print(Solution().canAttendMeetings([[7,10],[2,4]]))