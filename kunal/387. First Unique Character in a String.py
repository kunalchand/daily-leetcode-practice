import heapq


class Group:
    def __init__(self, index, occurence):
        self.index = index
        self.occurence = occurence

    def __lt__(self, other):
        if self.occurence > other.occurence:
            return False
        elif self.occurence < other.occurence:
            return True
        else:
            if self.index > other.index:
                return False
            else:
                return True


class Solution:
    # Brute Force Approach
    """
    def firstUniqChar(self, s: str) -> int:

        for index_og, char_og in enumerate(s):
            flag = False
            for index_match, char_match in enumerate(s):
                if index_og != index_match and char_og == char_match:
                    flag = True
            if flag == False:
                return index_og

        return -1
    """

    # Set Approach
    """
    def firstUniqChar(self, s: str) -> int:
        set_all = set()
        set_duplicates = set()
        
        for char in s:
            if char in set_all:
                set_duplicates.add(char)
            else:
                set_all.add(char)
            
        ans = -1
        
        for index, char in enumerate(s):
            if char not in set_duplicates:
                ans = index
                break
                
        return ans
    """

    # Dict Approach
    """
    def firstUniqChar(self, s: str) -> int:
        dict_ = {}
        
        for index, char in enumerate(s):
            value_list = dict_.get(char, [index, 0])
            dict_[char] = [value_list[0], value_list[1] + 1]
            # if char in dict_:
            #     dict_[char][1] += 1
            # else:
            #     # [index, occurence]
            #     dict_[char] = [index, 1]
            
            
        for key, value_list in dict_.items():
            # value_list = [index, occurence]
            if value_list[1] == 1:
                return value_list[0]
        
        return -1
    """

    # Heap Approach
    def firstUniqChar(self, s: str) -> int:
        dict_ = {}

        for index, char in enumerate(s):
            value_list = dict_.get(char, [index, 0])
            dict_[char] = [value_list[0], value_list[1] + 1]

        heap = []

        for value in dict_.values():
            index = value[0]
            occurence = value[1]
            heapq.heappush(heap, Group(index, occurence))

        if heap[0].occurence == 1:
            return heap[0].index
        else:
            return -1


print(Solution().firstUniqChar("leetcode"))
print(Solution().firstUniqChar("loveleetcode"))
print(Solution().firstUniqChar("aabb"))
