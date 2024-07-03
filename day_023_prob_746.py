class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mcost = [0] * len(cost)
        mcost[0], mcost[1] = cost[0], cost[1]
        for i in range(2,len(cost)):
            mcost[i] = cost[i] + min(mcost[i-1],mcost[i-2])
        return min(mcost[-1],mcost[-2])