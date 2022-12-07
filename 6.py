
# %% Setup
with open('6.txt', 'r') as f:
    text = f.read()


def find_marker(ml, text):
    for i, tup in enumerate(zip(*[text[i:] for i in range(ml)])):
        if len(set(tup)) == ml:
            return i + ml


# %% Part 1
find_marker(4, text)
# %% Part 2
find_marker(14, text)
