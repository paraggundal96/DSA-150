class Solution:
    def two_sum(arr,target):

        for i in range(len(arr)):
            key = target - arr[i]
            for j in range(i+1,len(arr)):
                if(arr[j]==key):
                    return [i,j]
        return -1
        
print(Solution.two_sum([1,2,3,4,5],9))