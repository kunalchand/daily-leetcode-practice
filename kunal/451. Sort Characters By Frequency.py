class Group:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq > other.freq


class Solution:
    # Dictionary Approach
    """
    def frequencySort(self, s: str) -> str:
        dict_ = {}
        for char in s:
            dict_[char] = dict_.get(char, 0) + 1

        list_ = dict_.items()

        new_list = sorted(list_, key = lambda x: -x[1])

        ans = ""

        for key, value in new_list:
            for _ in range(value):
                ans += key

        return ans
    """

    # Heap Approach
    def frequencySort(self, s: str) -> str:
        dict_ = {}
        for char in s:
            dict_[char] = dict_.get(char, 0) + 1

        import heapq

        heap = []

        for key, value in dict_.items():
            heapq.heappush(heap, Group(key, value))

        ans = ""
        while heap:
            item = heapq.heappop(heap)
            for _ in range(item.freq):
                ans += item.char

        return ans

    # Bucket Approach:
    """
    def frequencySort(self, s: str) -> str:
        dict_ = {}
        for char in s:
            dict_[char] = dict_.get(char, 0) + 1
            
        bucket = [[] for _ in range(len(s) + 1)]
        
        
        for char, freq in dict_.items():
            bucket[freq].append(char)
            
        ans = ""
        
        for index in range(len(bucket) - 1, 0, -1):
            for char in bucket[index]:
                for _ in range(index):
                    ans += char
        
        return ans 
    """


print(Solution().frequencySort("tree"))
print(Solution().frequencySort("cccaaa"))
print(Solution().frequencySort("Aabb"))
