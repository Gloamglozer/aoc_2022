
# %% Setup
import os

os.chdir(os.path.split(__file__)[0])  # start at current dir
starting_dir = os.getcwd()
with open('7.txt', 'r') as f:
    lines = f.readlines()

os.remove("7")
os.mkdir("7")
os.chdir("7")

line_iter = iter(lines[1:])

i = 0
length = len(lines)
while True:
    i += 1
    if i >= length:
        break
    syms = lines[i].split()
    if syms[0] == "$":  # splitting lags behind one iteration
        if syms[1] == "ls":
            i += 1
            cmd_syms = lines[i].split()
            print(cmd_syms[0])
            while cmd_syms[0] != "$":
                if cmd_syms[0] == 'dir':
                    os.mkdir(cmd_syms[1])
                else:
                    with open(cmd_syms[1], 'w') as f:
                        f.write(cmd_syms[0])
                i += 1
                if i >= length:
                    break
                cmd_syms = lines[i].split()
            else:  # We do have the next command
                i -= 1  # reset index so top of loop can handle this
                continue
        elif syms[1] == "cd":
            os.chdir(syms[2])

os.chdir(os.path.split(__file__)[0])  # start at current dir


def traverse(d, dir_dict):
    os.chdir(d)
    total_size = 0
    for node in os.listdir():
        if os.path.isdir(node):
            total_size += traverse(node, dir_dict)
        else:  # file
            total_size += int(open(node, 'r').read())

    dir_dict[os.getcwd()] = total_size
    os.chdir('..')
    return total_size


dir_dict = {}

size_used = traverse('7', dir_dict)

small_dir_total = 0
for size in dir_dict.values():
    if size <= 100000:
        small_dir_total += size
small_dir_total
# %% Part 2
size_to_free = 30000000 - (70000000 - size_used)

for size in sorted(dir_dict.values()):
    if size >= size_to_free:
        break

size

# %%
