class Solution:
    def minCostClimbingStairs(self, cost):
        prev_2, prev = cost[0], cost[1]
        for i in range(2, len(cost)):
            prev_2, prev = prev, cost[i] + min(prev_2, prev)
        return min(prev_2, prev)
        