

def solution(A, K) :
     
    
    if len(set(A)) == 1 or len(A) == K or  len(A) < 2 : 
        return A
     
        
    for index in range(K):
        pop = A.pop()
        A.insert(0, pop)
    
    
    return A
