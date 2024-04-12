class Solution:
    '''
    APPROACH: Using Hashmap
    Store the freq of each char in s in a map
    Traverse order to make output from the map
    Time: O(m + n), lengths of order and s
    '''
    def customSortString(self, order: str, s: str) -> str:
        
        # make a char_freq_map from s
        char_freq_map = {}      # a -> 2
        for char in s:
            char_freq_map[char] = char_freq_map.get(char, 0) + 1

        # prepare output by traversing the order
        # for each char in order, check its existance and frequency in map
        # add char to output that many times
        # once done, remove this char from map (useful in next step)
        out = []
        for char in order:
            if char in char_freq_map:
                out.append(char * char_freq_map[char])
                char_freq_map.pop(char)

        # add remaining chars in output from map, if there are any
        for key, val in char_freq_map.items():
            out.append(key * val)

        return "".join(out)

order = "xyz"
s = "abc"       # abc

order = "cba"   # cbad
s = "abcd"
print(Solution().customSortString(order, s))