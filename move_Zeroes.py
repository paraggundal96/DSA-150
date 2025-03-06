from typing import List

class Solution:
    def move_zeroes(self, nums: List[int]) -> List[int]:
        j = 0
        i = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for i in range(j, len(nums)):
            nums[i] = 0

        return nums

ans= Solution()
print(ans.move_zero_single([0,1,2,0,3]))
