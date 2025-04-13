from typing import List

class Solution:
    def trapping(self, walls: List[int]) -> int:
        start = 0
        wall2 = 0
        wall1 = 0
        water_trapped = 0
        while(start < len(walls)):
            if walls[start]==0 or walls[start]<walls[start + 1]:
                start +=1
            else:
                wall1 = start
                