class Solution:
    def non_repeating_char(self, characters :str) -> str:
        char_dict = {}
        for char in characters:
            if char in char_dict.keys():
                char_dict.update({char:True})
            else:
                char_dict.update({char:False})
        for char in characters:
            if char_dict[char] == False:
                return char
            
        return -1
    
ans = Solution()
print(ans.non_repeating_char('aabcdbcdefefhxi'))
