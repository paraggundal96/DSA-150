stack = []

nums = [1,0,0,3,4,2,7]

result = []

for num in reversed(range(len(nums))):

    if not stack:
        result.append(-1)
    
    elif stack[-1] > num:
        result.append(stack[-1])
    
    else:
        while stack[-1] < num:
            stack.pop()
        if not stack:
            result.append(-1)
        else:
            result.append(stack[-1])
    
    stack.append(num)

print(result)
        

