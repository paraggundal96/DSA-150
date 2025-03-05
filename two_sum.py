from typing import List

class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        key_dict = {}
        for i in range(len(nums)):
            key = target - nums[i]
            if key in key_dict.keys():
                return [key_dict[key],i]
            key_dict.update({nums[i]:i})
        return []
            
        
obj = Solution()
print(obj.two_sum([1,2,4,5,6],10))
