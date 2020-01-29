import math

def solution(N):
    # write your code in Python 3.6
    bi_number = bin( N )
    bi_number = format(N, 'b')
    print(bi_number)
    prev_b = ''
    max_counter = 0
    counter = 0
    for b in bi_number:
        if prev_b == '1' and b == '0':
            counter += 1
        elif prev_b == '0' and b == '0' :
            counter += 1
        elif prev_b == '0' and b == '1' :
            if max_counter < counter :
                max_counter = counter
            counter = 0

        prev_b = b


    return max_counter



print(solution(1041))
print(solution(15))
print(solution(32))
