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
    
ans = Solution()
print(ans.kadane_window([-1,-1,2,-1]))
            