from collections import Counter
import heapq

class Group:
    def __init__(self, char, occurance):
        self.char = char
        self.occurance = occurance

    # reverse the behaviour of __lt__() i.e. less than method
    def __lt__(self, other):
        # default => return self.occurance < other.occurance should return True
        return self.occurance > other.occurance


class Solution:
    ## Approach-1: store char and its occurance in dict
    ## sort dict and make result
    ## Time: O(n * log n)
    ## Space: O(n)
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)               # {char : occurance} 
        res = ""
        # for letter, freq in counter.most_common():
        # print(counter)
        # sort dict in reverse order based on occurance
        for char, occurance in (sorted(counter.items(),key= lambda item: item[1], reverse=True)): # 26 * log 26
            res += char * occurance
            # for _ in range(occurance):
            #     res += char                # append 'char' to res, 'occurance' times
        return res
    


    ## Approach-2: store char and its occurance on a max-heap (heap is sorted based on occurance)
    ## heap-node: (char, occurance) 
    ## keep popping max node until heap is empty
    ## Time: O(n * log n)
    ## Space: O(n)
    def frequencySort2(self, s: str) -> str:
        counter = Counter(s)
        h = []
        res = ""
        for k, v in counter.items():
            heapq.heappush(h, Group(k,v))
        
        while h:
            item = heapq.heappop(h)
            res += item.char * item.occurance
        return res


    ## Approach-3: counter dict and buckets
    ## Time: O(n)
    ## Space: O(n)
    def frequencySort3(self, s: str) -> str:
        counter = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        print(buckets)

        # fill buckets, ith bucket will store the chars that occur ith number of times in s
        for char, occurance in counter.items():
            buckets[occurance].append(char)

        res = []
        # traverse buckets from end and add to res
        for i in range(len(buckets) - 1, 0, -1):
            for char in buckets[i]:
                res.append(char * i)

        print(buckets)
        return "".join(res)
    

obj = Solution()
# print(obj.frequencySort("tree"))
# print(obj.frequencySort2("tree"))
print(obj.frequencySort3("tree"))