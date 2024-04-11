from typing import List
from collections import defaultdict

class Solution:
    '''
    Edge cases:
        disconnected components
        - [1,2], [5,6]
        - [1,0], [2,0]

    Node  =>    Courses

    TIME: O(N + E)
    '''
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        def dfs(course):
            # base cases
            if course in visited:
                return False
            
            if course_prereq_map[course] == []:
                return True
            
            visited.add(course)

            # check prereqs for given course
            for prereq in course_prereq_map[course]:
                # if any prereq can't be completed, return False for given course
                if not dfs(prereq):
                    return False
            
            # given course can be completed
            visited.remove(course)
            course_prereq_map[course] = []
            return True


        course_prereq_map = { i : [] for i in range(numCourses) }  # course -> [prereqs for this course]
        visited = set()     # visit all courses along current DFS path

        # make adj_lst in the format cr : [pre_req]
        for course, prereq in prerequisites:
            course_prereq_map[course].append(prereq)

        # traverse the graph (all nodes)
        # check if a given course can be completed or not
        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
        
    
    '''
    APPROACH-2: prereq -> [courses I can go to from this prereq]
    '''
    def canFinish2(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # for every prereq, check if we can reach the end
        def dfs(prereq):
            if prereq in visited_on_curr_path:
                return False
            
            if prereq not in prereq_course_map:     # if reached an end node
                return True                         # only end nodes will not have a key in map
            
            visited_overall.add(prereq)
            visited_on_curr_path.add(prereq)

            # check the course(s) for this prereq
            for course in prereq_course_map[prereq]:
                if not dfs(course):
                    return False
            visited_on_curr_path.remove(prereq)
            return True

        # traverse every path and see if there exist loop or not
        prereq_course_map = {}

        # make map
        for course, prereq in prerequisites:
            if prereq not in prereq_course_map:
                prereq_course_map[prereq] = [course]
            else:
                prereq_course_map[prereq].append(course)

        visited_on_curr_path = set()        # will add/remove nodes as path grows/shrinks
        visited_overall = set()             # keep track of all visited nodes (already explored paths) in the graph, never remove, used to stop duplicate work

        # start DFS from every node
        for pre in range(numCourses):
            if pre not in visited_overall:   # only check new paths
                if not dfs(pre):
                    return False             # return False if any path has cycle
        
        return True

        
prerequisites = [[1,0], [1,2], [1,3], [5,4], [7,6], [4,1], [6,1]]
print(Solution().canFinish2(8, prerequisites))

