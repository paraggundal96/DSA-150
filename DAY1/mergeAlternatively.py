class Solution:
    def mergeAlternately(self, word1:str, word2:str)->str:
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        L1 = list(word1)
        L2 = list(word2)
        if len(L1) == len(L2):
            newL = []
            for i in range(len(L1)):
                newL.append(L1[i])
                newL.append(L2[i])
            return "".join(newL)
        elif len(L1)> len(L2):
            newL = []
            for i in range(len(L2)):
                newL.append(L1[i])
                newL.append(L2[i])
            text = "".join(newL)
            return text + word1[len(L2):]
        else:
            newL = []
            for i in range(len(L1)):
                newL.append(L1[i])
                newL.append(L2[i])
            text = "".join(newL)
            return text + word2[len(L1):]

ans = Solution()
print(ans.mergeAlternately('abef','cd'))



        