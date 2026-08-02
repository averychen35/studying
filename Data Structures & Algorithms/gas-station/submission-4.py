class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_gas = 0
        res = 0
        for i in range(len(gas)):
            total_gas += gas[i]
            total_gas -= cost[i]
            if total_gas < 0:
                total_gas = 0
                res = (i + 1) % len(gas)
        return res
