class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0]*(n+1)
        dp[-2] = cost[-1]
        # dp[-1]= float("inf")
        for i in range(n-2, -1, -1):
            dp[i] = min(dp[i+1], dp[i+2])+cost[i]
        return min(dp[0], dp[1])