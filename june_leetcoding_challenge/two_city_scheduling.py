# https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost = 0
        refund = []
        
        for A, B in costs:
            refund.append(B - A)
            min_cost += A
        refund.sort()
        
        for i in range(len(costs) // 2):
            min_cost += refund[i]
        
        return min_cost    
