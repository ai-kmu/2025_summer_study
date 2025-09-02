class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = float('inf')
        dp = [INF] * (amount + 1)
        dp[0] = 0  # 0원은 동전 0개로 만들 수 있음

        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != INF else -1
