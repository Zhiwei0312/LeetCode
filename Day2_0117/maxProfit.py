# calculate the max difference between two points

class Solution:
# brute force
# O(n2), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                ans = max(ans, prices[j] - prices[i])
        return ans

# 对任意一天作为卖出日，
# 能获得的最大合法利润，一定来自『它之前的最低买入价』
# 我们固定在第 i 天卖出，卖价是 prices[i]
# 在第 i 天之前，选哪一天买，利润最大？
# 最低价是min_price, 用另一个更高的价格x > min_price购买
# 卖出日固定，最优买入价一定是之前的最低价
    def maxProfit_1timescan(self, prices: List[int]) -> int:
        min_price = 10**18
        best = 0
        for p in prices:
            if p < min_price:
                min_price = p # 记录p之前的最小价格
            best = max(best, p - min_price) # 记录最大利润
        return best