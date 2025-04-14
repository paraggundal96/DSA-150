class Solution:

    def pow(self, x:int, n:int)->int:

        if n == 1:
            return x
        return x * self.pow(x,n-1)
    
ans = Solution()
print(ans.pow(2,10))