def solution(A):
    # write your code in Python 3.6
    A.sort()
    
    stack = []
    for index, item in enumerate( A ):
        
        if index > 0 : 
            if len(stack) >0 and stack[-1] == item:
                stack.pop()
                continue
        
        stack.append(item)        
    
    return stack[0]
