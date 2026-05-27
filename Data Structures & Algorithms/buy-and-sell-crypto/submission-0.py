class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_profit = 0
        buy = float('inf')

        for i in prices:
            if i < buy:
                buy = i
                continue
            
            print(i, buy, curr_profit)
            curr_profit = max(curr_profit, i-buy)

        return curr_profit

