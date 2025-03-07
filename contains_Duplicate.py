from typing import List

class Solution:

    def contains_duplicate(self, nums: List[int]) -> bool:

        hash_map = {}

        for r in nums:
            if r in hash_map.keys():
                return True
            hash_map.update({r:True})

        return False
    

ans = Solution()
print(ans.contains_duplicate([1,2,3,4,5]))
print(ans.contains_duplicate([1,2,3,4,1]))
