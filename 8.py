# %%
import numpy as np
from itertools import product

with open('8_test.txt', 'r') as f:
    text = f.read()

trees = np.array([[int(c) for c in line] for line in text.splitlines()])
m, n = trees.shape
# %%

visible = np.full(trees.shape, False)
rot = np.array([[0, 1], [-1, 0]])
outer = np.array([1, 0])
inner = np.array([0, 1])
num_trees = 0
for start in [np.array(tup) for tup in ((0, 0), (0, n-1), (m-1, n-1), (m-1, 0))]:
    for _ in range(abs(outer[0])*m+abs(outer[1])*n): # makes generalizable to arbitrary mxn
        pos = start.copy()
        highest = -np.inf
        for i in range(abs(inner[0])*m+abs(inner[1])*n):
            this = trees[tuple(pos)]
            if this > highest:
                visible[tuple(pos)] = True
                highest = this
            pos += inner
        start += outer

    outer = rot@outer
    inner = rot@inner

visible.sum()

# %%

ss = np.ones(trees.shape)
ds = [np.array(tup) for tup in ((0, 1), (1, 0), (0, -1), (-1, 0))]
for tup in product(range(m), range(n)):
    pos = np.array(tup)
    for d in ds:
        checking = pos.copy()
        checking += d
        s = 0
        while 0 <= checking[0] < m and 0 <= checking[1] < n: #inbounds
            s += 1
            if trees[tuple(checking)] >= trees[tuple(pos)]:
                break
            checking += d
        ss[tuple(pos)] *= s  

np.max(ss)
# %%
