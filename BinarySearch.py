def binary_search(arr,key):

    start = 0
    end = len(arr)-1
   

    while(start <= end):
        mid = (start + end)//2

        if(arr[mid] == key):
            return mid
    
        elif(arr[mid] < key):
            start = mid + 1

        elif(arr[mid] > key):
            end = mid - 1
            
    return -1
        
array = [1,2,3,4,6,7]

key = 6
print(binary_search(array,4))


