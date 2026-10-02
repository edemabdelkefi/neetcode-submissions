class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prix_min = prices[0]
        profit_max = 0

        for prix in prices:
            prix_min = min(prix_min, prix)
            profit_max = max(profit_max, prix - prix_min)

        return profit_max
