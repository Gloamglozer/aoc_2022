# %%
with open("3.txt.", 'r') as f:
    lines = f.read().splitlines()


def priority(char):
    num = ord(char)
    if num < 97:
        return num-38
    else:
        return num-96


p = 0
for line in lines:
    n = len(line)
    common = set(line[:n//2]) & set(line[-n//2:])
    p += priority(next(iter(common)))
p

# %%
p2 = 0
for a, b, c in zip(lines[::3], lines[1::3], lines[2::3]):
    common = set(a) & set(b) & set(c)
    p2 += priority(next(iter(common)))
p2
