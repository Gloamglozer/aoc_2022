# %% Setup

from copy import deepcopy

with open('5.txt', 'r') as f:
    starting_crates, instructions = f.read().split('\n\n')

crate_state_lines = starting_crates.splitlines()
n_stacks = len(crate_state_lines[-1].split())

cl_start = [[] for _ in range(n_stacks)]

for line in crate_state_lines[-2::-1]:
    for i, crate in enumerate(line[1::4]):
        if not crate == " ":
            cl_start[i].append(crate)


def move(cl, n, f, t, model="9000"):
    if model == '9001':
        cl[t-1] += cl[f-1][-n:]
    else:
        cl[t-1] += cl[f-1][:-n-1:-1]
    cl[f-1] = cl[f-1][:-n]


# %% Part 1
cl = deepcopy(cl_start)
for ins in instructions.splitlines():
    move(cl, *list(map(int, ins.split()[1::2])))

''.join([c.pop() for c in cl])

# %% Part 2
cl = deepcopy(cl_start)
for ins in instructions.splitlines():
    move(cl, *list(map(int, ins.split()[1::2])), model='9001')

''.join([c.pop() for c in cl])
