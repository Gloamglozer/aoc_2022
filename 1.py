# %% Part 1
with open('1.txt', 'r') as f:
    text = f.read()

cals = [sum(map(int, elf.split('\n'))) for elf in text.split('\n\n')]

max(cals)
# %% Part 2
sum(sorted(cals)[-3:])
