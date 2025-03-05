def MaxWater(arr):
    '''
    Takes the array as input, where each element in array represents height of container
    This function finds the container that can collect max water
    Time Complexity = O(n)
    Space Complexity = O(1)
    '''
    Wall1 = 0
    Wall2 = len(arr)-1
    max_area = 0

    while(Wall1 < Wall2):

        height = min(arr[Wall2],arr[Wall1])
        width = Wall2 - Wall1
        area = height * width
        max_area = max(max_area,area)

        if(arr[Wall1] < arr[Wall2]):
            Wall1 += 1
        else :
            Wall2 -= 1
    
    return max_area

container_height = input("Enter the Array of Heights for container").split()

for i in range(len(container_height)):
    container_height[i] = int(container_height[i])

print(f'The Area of Container holding maximum water is {MaxWater(container_height)}')
