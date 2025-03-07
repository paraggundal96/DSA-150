from typing import List

class Solution:
    
    def first_last_pos(self, nums: List[int], target: int) -> List[int]:
        '''
        Brute Force Solution
        Space Complexity: O(n) --> hash map increases with count of target in array
        Time Complexity: O(n) --> iterates entire loops
        '''

        hash_map = {target : []}
        i = 0
        for i in range(len(nums)):
            if nums[i] == target:
                hash_map[target].append(i)
        
        if len(hash_map[target]) == 0:
            return [-1,-1]
        
        elif len(hash_map[target]) == 1:
            return [hash_map[target][0],hash_map[target][0]]
        
        else:
            return [hash_map[target][0],hash_map[target][-1]]
        
    '''
    More Optimized Solution yet a Brute Force 2 with
    Time Complexity: O(n)
    Space Complexity: O(1)
    '''

    def first_pos(self, nums: List[int], target: int) -> int:
        
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
    
    def last_pos(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)-1,0,-1):
            if nums[i] == target:
                return i
        return -1
    
    def optimized_sol(self, nums: List[int], target: int) -> List[int]:
        first = self.first_pos(nums,target)
        last = self.last_pos(nums,target)
        return [first,last]
    
    '''
    Optimized the solution by Binary Search
    Time Complexity: O(logn)
    Space Complexity: O(1)
    '''

    def first_occurence(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1

        while(start <= end):
            
            mid = (start + end)//2

            if(nums[mid] == target):
                if(mid == 0 or nums[mid-1]!=target):
                    return mid
                end = mid -1

            elif(nums[mid] > target):
                end = mid -1

            else:
                start = mid + 1

    def last_occurence(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums)-1

        while(start <= end):
            mid = (start + end) // 2

            if(nums[mid] == target):
                if(mid == len(nums)-1 or nums[mid + 1]!=target):
                    return mid
                start = mid + 1

            elif(nums[mid] < target):
                start = mid + 1

            else:
                end = mid - 1

    def pos_search(self, nums: List[int], target: int) -> List[int]:

        if target < nums[0] or target > nums[-1]:
            return [-1,-1]
        
        first = self.first_occurence(nums,target)
        last = self.last_occurence(nums,target)

        return [first, last]


ans = Solution()
print(ans.pos_search([0,0,0,1,1,0,1,0,1],1))
print(ans.pos_search([1,2,3,4,5],3))
print(ans.pos_search([1,2,3,4,1],10))




            
