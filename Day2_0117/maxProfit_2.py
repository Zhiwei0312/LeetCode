# 多次买入卖出

class Solution:
# griddy search to include all upwards lope
# O(n), O(1)
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0;
        N = len(prices);

        for i in range(1,N):
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
            
        return profit
    
# dynamic programming: 把一个大问题拆解成一系列由状态的小问题
# 逐步保存最有结果，避免重复计算
# state 描述当前处境
# transition 今天能从哪些状态变成当前状态
# optimal substructure 当前最优解，只依赖于之前的最优解
    def maxProfit_DP(self, prices: List[int]) -> int:
        cash = 0 # 不持股最大利润: 一开始是0，初始状态不持股
        hold = -10**18 # 持股最大利润

        # 计算的是手上有的钱，而不是股市里的钱
        for p in prices:
            # 今日不持股：
            # 昨日不持股：cash
            # 昨日持股，今日卖出： 得到今日的价格
            cash = max(cash, hold + p)
            # 今日持股：
            # 昨日持股：hold
            # 昨日不持股，今日持股：cash - p
            hold = max(hold, cash - p) 
        return cash