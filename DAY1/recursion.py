class Solution:
    def sum_N_descending(self,num:int)->int:

        if num == 1:
            return 1
        return num + self.sum_N_descending(num-1)
    
    def sum_N_ascending(self, curr:int, num: int)->int:

        if curr == num:
            return num
        return curr + self.sum_N_ascending(curr+1, num)

ans = Solution()
#print(ans.sum_N_descending(5))
print(ans.sum_N_ascending(0,5))