import random
from Miller_Rabin import primality_test
import math
import Graphing
import time
import itertools
import csv

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a, b):
    return (a // gcd(a, b)) * b

def total_three(n):
    threes = 0
    combined_tuples = tuple(itertools.combinations_with_replacement([i for i in range(1, n + 1)], 3))
    for i in range(len(combined_tuples)):
        a, b, c = combined_tuples[i]
        total = lcm(a, b) + lcm(a, c) + lcm(b, c)
        if(total % 3 == 0):
            threes += 1
    return threes / math.comb((n + 2), 3)

def total_distinct(n):
    distinct_lcms = []
    combined_tuples = tuple(itertools.combinations_with_replacement([i for i in range(1, n + 1)], 3))
    for i in range(len(combined_tuples)):
        a, b, c = combined_tuples[i]
        total = lcm(a, b) + lcm(a, c) + lcm(b, c)
        distinct_lcms.append(total)
    distinct_lcms = set(distinct_lcms)
    return len(distinct_lcms)
 
def rand_three(n, iter):
    total = 0
    threes = 0
    for i in range(iter):
        a = random.randint(1, n)
        b = random.randint(1, n)
        c = random.randint(1, n)
        add_val = 0
        if(a != b and b != c and a != c):
            add_val = 1
        elif(a == b and b == c):
            add_val = 6
        else:
            add_val = 2
        lcm_sum = lcm(a, b) + lcm(a, c) + lcm(b, c)
        if(lcm_sum % 3 == 0):
            threes += add_val
        total += add_val
    return threes / total

def rand_distinct(n, iter):
    distinct_lcms = []
    for i in range(iter):
        a = random.randint(1, n)
        b = random.randint(1, n)
        c = random.randint(1, n)
        lcm_sum = lcm(a, b) + lcm(a, c) + lcm(b, c)
        distinct_lcms.append(lcm_sum)
    distinct_lcms = set(distinct_lcms)
    return len(distinct_lcms)

x_vals = [i for i in range(1, 200)]
y_vals = []
for i in range(1, 200):
    next_val = total_distinct(i)
    print(i, next_val)
    y_vals.append(next_val)
'''for i in range(50, 100):
    next_val = rand_distinct(i, 10000)
    print(i, next_val)
    y_vals.append(next_val)'''

merge_list = [(x_vals[i], y_vals[i]) for i in range(0, len(list(x_vals)))]
with open('total_distinct.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_NONNUMERIC)
    wr.writerow(merge_list)

Graphing.graph_func(x_vals, y_vals)
