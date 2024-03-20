from typing import List
class Solution:
        '''
        I/O:
            I: int array, unsorted, 0 and +ve, repeat
            O: max_profit or 0
        
        Edge case:
            repeat, decreasing, single element

        Approach:
            1. Brute Force:     Time: O(N ^ 2), Space: O(1)
                calculate profit every day for each day
            
            2. pointer, traversing right to left, running max
            time, space: O(N), O(1)
            max_val_in_right = 10
            max_profit = 9

               x 
            [7,1,10,5,3,6,4]

            3. suffix sum       space: O(N)
            [7, 1, 10,5,3,6,4]
            
            [10 10 10 6 6 6 4]

            4. 2 pointer/ sliding-window
            time, space: O(N), O(1)
            max_profit = max(max_profit, curr_profit)
            curr_profit = 3

               b       s 
            [7,1,5,3,6,4]

                   b   s
            [7,3,5,1,6,4]
        '''
        '''
        APPROACH-1: 2 POINTERS / SLIDING WINDOW
        TIME: O(N)
        '''
        def maxProfit(self, prices: List[int]) -> int:
            buy = 0
            curr_profit, max_profit = 0, 0

            for sell in range(len(prices)):
                if prices[sell] <= prices[buy]:
                    buy = sell                      # update buy
                
                curr_profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, curr_profit)

            return max_profit
        
        '''
        APPROACH-2: BRUTE FORCE
        TIME: O(N ^ 2)
        '''
        def maxProfit(self, prices: List[int]) -> int:
            curr_profit, max_profit = 0, 0

            for l in range(len(prices)):
                for r in range(l, len(prices)):
                    curr_profit = prices[r] - prices[l]
                    max_profit = max(max_profit, curr_profit)

            return max_profit
        
        '''
        APPROACH-3: RUNNING MAX, while traversing right to left
        TIME: O(N)
        '''
        def maxProfit(self, prices: List[int]) -> int:
            running_max = prices[-1]
            max_profit = 0

            for i in range(len(prices) - 1, -1, -1):
                if prices[i] >= running_max:
                    running_max = prices[i]
                curr_profit = running_max - prices[i]
                max_profit = max(max_profit, curr_profit)
            
            return max_profit
                
        '''
        APPROACH-4: Suffix max array, will contain max val in right of curr ele at prices
        similar to above: RUNNING MAX, while traversing right to left
        TIME: O(N)
        '''
        def maxProfit(self, prices: List[int]) -> int:
            max_profit = 0
            suffix_max = [0] * len(prices)

            # fill suffix_max
            suffix_max[-1] = float('-inf')
            for i in range(len(prices) - 2, -1, -1):
                suffix_max[i] = max(suffix_max[i + 1], prices[i + 1])
            
            # calculate profit
            for i in range(len(prices)):
                curr_profit = suffix_max[i] - prices[i]
                max_profit = max(max_profit, curr_profit)
            
            return max_profit


                

prices = [7,1,5,3,6,4]
print(Solution().maxProfit(prices))