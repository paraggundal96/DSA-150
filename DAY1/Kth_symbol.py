class Solution:
    def kthSymbol(self, n:int, k:int)->int:
        if n == 1:
            return 0
        L = 2**(n-1)

        if k > n/2:
            return int(not self.kthSymbol(n-1,k-(L/2)))
        else:
            return self.kthSymbol(n-1,k)
        
ans = Solution()

print(ans.kthSymbol(4,8))