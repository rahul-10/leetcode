class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        hash_map = {}

        for idx, val in enumerate(s):
            hash_map[val] = hash_map.get(val, 0) + cost[idx]

        max_cost = total_cost = 0
        
        for cost in hash_map.values():
            if cost > max_cost:
                max_cost = cost
            
            total_cost += cost

        return total_cost-max_cost

            
        