from typing import List
class Moutain:
    def valid_monutain(self, mountain: List[int]) -> bool:

        i = 1
        while(i<len(mountain) and mountain[i]>mountain[i-1]):
            i += 1
        if(i == len(mountain) or i == 1) :
            return False
        while(i<len(mountain) and mountain[i]<mountain[i-1]):
            i += 1
        return i == len(mountain)
    
mountain1 = Moutain()
print(mountain1.valid_monutain([1,2,3,2,1]))
print(mountain1.valid_monutain([1,2,3,2,1,2]))