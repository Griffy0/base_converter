#convert base 10 to base 2

import numpy as np

def highest_pow(x):
    return int(np.floor(np.log2(x)))

def iter_loop(x, bin, last):
    highest = highest_pow(x)
    remainder = x-2**highest
    if (last-highest > 0):
        bin = bin + (['0']*(last-highest-1))
    bin.append('1')
    if remainder > 1:
        return iter_loop(remainder, bin, highest)
    bin = bin + (['0']*(highest-1))
    return bin

def iter_loop_wrapper(x):
    bin=[]
    if (x == 0):
        return '0'
    if (x == 1):
        return '1'
    out = iter_loop(x, bin, highest_pow(x)+1)
    out.append(str(x%2))
    return ''.join(out)

to_convert = int(input())
print(iter_loop_wrapper(to_convert))


