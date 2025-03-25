from typing import List

class Solution:
    def distribute(self, ratings: List[int]) -> List:
        candy = []
        for i in range(len(ratings)):
            candy.append(1)
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = 1 + candy[i-1]
        
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candy[i] = max(candy[i],candy[i+1]+1)
        return sum(candy)

ans = Solution()
print(ans.distribute([1,0,2,2]))

    
