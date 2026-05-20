from typing import List

def max_histogram_area(heights:List[int]) -> int:
    n = len(heights)
    right = [n] * n
    left = [-1] * n
    width = [0] * n
    max_area = float("-inf")
    stack = []

    # NSL

    for i in range(n):

        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        
        if stack:
            left[i] = stack[-1][1]
    
    # NSR

    for i in range(n-1, -1, -1):

        while stack and stack[-1][0] >= heights[i]:
            stack.pop()
        
        if stack:
            right[i] = stack[-1][1]
    
    for i in range(n):

        width[i] = right[n-i-1] - left[i] - 1

        area = width[i] * heights[i]

        max_area = max(area, max_area)
    
    return max_area




        

