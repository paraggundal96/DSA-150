from typing import List

class Solution:
    def kadane_window(self, nums: List[int])->int:

        max_sum = nums[0]
        current_sum = 0
        L,maxL,maxR = 0,0,0

        for R in range(len(nums)):
            if current_sum < 0:
                L = R
                current_sum = 0
            
            current_sum += nums[R]

            if current_sum > max_sum :
                max_sum = current_sum
                maxL, maxR = L, R

        return max_sum,[maxL,maxR]
    def maxContainer(self, walls: List[int]) -> int:

        L = 0
        R = len(walls)-1
        area = 0
        if len(walls) <= 1:
            return 0
        while(L<R):
            area = max(area,min(walls[L],walls[R]) * (R-L))
            if walls[L] < walls[R]:
                L+=1
            else:
                R-=1
        return area

    
ans = Solution()
print(ans.kadane_window([-1,-1,2,-1]))
print(ans.maxContainer([1,8,6,2,9,4]))
            