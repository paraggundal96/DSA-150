from typing import List

class Solution:
    def isCommon(self, arr1: List[str], arr2: List[str]) -> bool:
        dict = {}
        if len(arr1) == 0 or len(arr2) == 0:  # have a look here
            return False
        for elements in arr1:
            dict.update({elements.lower():False})
        for elements in arr2:
            if elements.lower() in dict.keys():
                return True
        return False

ans = Solution()
print(ans.isCommon(['a','b','c','c'],['x','r','x']))
