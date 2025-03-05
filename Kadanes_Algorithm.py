def kadane(List):

    max_sum = List[0]
    curr_sum = 0

    for item in List:
        curr_sum = max(curr_sum,0) + item
        max_sum = max(max_sum, curr_sum)
    return max_sum

def kadane_window_variation(List):

    L = 0
    maxL, maxR = 0,0
    max_sum = List[0]
    curr_sum = 0

    for R in range(len(List)):

        if curr_sum < 0:
            curr_sum = 0
            L = R

        curr_sum += List[R]
        if curr_sum > max_sum:
            max_sum = curr_sum
            maxL, maxR = L, R

    return [maxL, maxR]

myList = list(map(int, input('Enter the List Elements\n').split(' ')))

print(kadane(myList))
print(kadane_window_variation(myList))