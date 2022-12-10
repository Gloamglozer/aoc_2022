# %%
import numpy as np

dir_dict = {'R': np.array([1, 0]),
            'L': np.array([-1, 0]),
            'U': np.array([0, 1]),
            'D': np.array([0, -1])
            }
with open('9.txt', 'r') as f:
    lines = f.readlines()
    dirs = [dir_dict[line.split()[0]] for line in lines]
    dists = [int(line.split()[1]) for line in lines]


def update_tail(tail, head):
    diff = head-tail
    if np.linalg.norm(diff) >= 1.9:
        return tail + np.sign(diff)
    else:  # the tail is nsew adjacent
        return tail


def num_unique_tail_pos(rope_len=2):
    visited_by_tail = set(((0, 0),))
    rope = [np.array([0, 0]) for _ in range(rope_len)]
    for dir, dist in zip(dirs, dists):
        for _ in range(dist):
            rope[0] += dir
            for i in range(rope_len-1):
                rope[i+1] = update_tail(rope[i+1], rope[i])
            visited_by_tail.update((tuple(rope[-1]),))
    return len(visited_by_tail)


num_unique_tail_pos(2)
# %%
num_unique_tail_pos(10)
