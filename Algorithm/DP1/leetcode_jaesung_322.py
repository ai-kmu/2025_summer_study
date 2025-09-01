class Solution:
    def coinChange(self, coins, amount):
        dp = [0] + [float('inf')]*amount
        for a in range(1, amount+1):
            for c in coins:
                if a >= c and dp[a-c] != float('inf'):
                    dp[a] = min(dp[a], dp[a-c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1
