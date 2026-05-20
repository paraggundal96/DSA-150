# Stock Span Problem
from typing import List


def stock_span(prices:List[int]):

    span = []
    stack = []

    for i in range(len(prices)):

        while stack and stack[-1][0] <= prices[i]:
            stack.pop()
        
        if not stack:
            span.append(i + 1)
        else:
            span.append(i - stack[-1][1])
        
        stack.append((prices[i],i))
    
    return span