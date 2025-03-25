from typing import List

class Solution:
    def starting_gas_station(self, gas: List[int], cost: List[int]) -> int:

        initial = 0
        start = initial
        gas_amount = gas[start]
        station_visited = 0

        while(station_visited<len(gas)):
            if gas_amount >= cost[start]:
                gas_amount+=(gas[(start+1)%len(gas)]-cost[start])
                start = (start+ 1)%len(gas)
                station_visited+=1
            else:
                initial += 1
                start = initial
                gas_amount = gas[start]
                station_visited = 0
        
        return initial
ans = Solution()
print(ans.starting_gas_station([4,5,2,6],[3,4,5,1]))