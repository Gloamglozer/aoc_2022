# %%
import numpy as np

with open('4.txt', 'r') as f:
    lines = f.read().splitlines()


def contains(a, b):
    return a[0] <= b[0] and b[1] <= a[1]


contained = 0
for line in lines:
    f, s = line.split(',')
    ft = list(map(int, f.split('-')))
    st = list(map(int, s.split('-')))
    if contains(ft, st) or contains(st, ft):
        contained += 1

contained

# %%part 2


def overlap(a, b):
    if a[0] in b or a[1] in b:
        return True
    if a[0] < b[1]:
        return b[0] < a[1]
    else:
        return False


contained = 0
for line in lines:
    f, s = line.split(',')
    ft = list(map(int, f.split('-')))
    st = list(map(int, s.split('-')))
    if overlap(ft, st):
        contained += 1

contained

# %%
