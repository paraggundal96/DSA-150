from typing import List

class Solution:
    '''
    Brute Force 1
    Using the Hash Map
    Space Complexity: O(n)
    Time Complexity: O(n)
    '''
    def listing(self, nums: List[int]) -> List[int]:

        list_ = []

        for i in nums:
            list_.append(i)

        return list_
    
    def searching(self, nums: List[int]) -> int:
        for j in range(len(nums)):
            if j not in self.listing(nums):
                return j
        return -1   
    
    '''
    Optimized Solution using sum of first N terms
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''

    def missing(self, nums:List[int]) -> int:
        n = len(nums)
        intended_sum = n*(n+1)/2
        actual_sum = 0
        for i in range(len(nums)):
            actual_sum += nums[i]

        return int(intended_sum - actual_sum)

ans = Solution()
print(ans.missing([1,2,0]))