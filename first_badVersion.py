class Solution:

    def isBadVersion(self, num: int):
        return num >= 5
    
    def first_Bad_version(self, n: int) -> int:

        start = 1
        end = n

        while(start <= end):

            mid = (start + end)//2
            if(self.isBadVersion(mid)):
                if(mid == 1 or (mid-1>0 and not self.isBadVersion(mid-1))):
                    return mid
                end = mid -1

            else:
                start = mid + 1

        return start,end
    
ans = Solution()
print(ans.first_Bad_version(10))