class Solution(object):

    def gcd(self, word1:str, word2:str) -> int:
        L1 = len(word1)
        L2 = len(word2)
        while(L2!=0):
            L1,L2 = L2, L1%L2
        return L1

    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if str2+str1 == str1+str2:
            return str1[:self.gcd(str1,str2)]
        else:
            return ""


ans = Solution()
print(ans.gcdOfStrings('ABCABCDEF','ABC'))