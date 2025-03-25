
class Solution:
    def longest_substring(self, characters: str) -> int:
        ind_dict = {}
        length = 0
        L = 0
        R = 0
        while(R < len(characters)):
            key = characters[R]
            if key in ind_dict.keys():
                L = max(L, ind_dict[key] + 1)
            
            ind_dict.update({key:R})
            length = max(length,R-L+1)
            R += 1
        return length

ans = Solution()
print(ans.longest_substring('aabcdea'))
