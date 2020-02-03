import math
import sys

def solution(A):

    all_value = sum(A)
    ret_val = 9999
    sum_minus = 0
    for item in A[:-1]:
        sum_minus += item
        all_value -= item
        temp_val = all_value - sum_minus
        # print( str(temp_val), str(sum_minus), str(item))
        temp_val = int(math.fabs(temp_val))
        if temp_val < ret_val:
            ret_val = temp_val

    return ret_val
