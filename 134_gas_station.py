class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, tank, total_gas = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total_gas += tank
                tank = 0

        if total_gas + tank < 0:
            return -1
        return start
