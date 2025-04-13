from typing import List
class Solution:
    def ascending2(self, nums: List[int])->List:

        length = len(nums)
        result = [0] * length
        pos = length - 1
        left = 0
        right = length -1

        while(left <= right):

            if abs(nums[right]) > abs(nums[left]):
                result[pos] = nums[right]**2
                right -= 1
            
            else:
                result[pos] = nums[left]**2
                left += 1
            pos -= 1

        return result
    
ans = Solution()
print(ans.ascending2([-4,-2,0,1,2,3,5]))
