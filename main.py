testing = False

if testing:
    raw = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.strip().split('\n')
else:
    with open('data09.txt') as f:
        raw = f.read().strip().split('\n')

sequences = [list(map(int, x.strip().split())) for x in raw]


def differences(s):
    return [s[i + 1] - s[i] for i in range(len(s) - 1)]


s = 0
t = 0
for sequence in sequences:
    history = [sequence]

    while set(history[-1]) != {0}:
        history.append(differences(history[-1]))

    for i in range(len(history) - 1, 0, -1):
        history[i - 1].append(history[i - 1][-1] + history[i][-1])
        history[i - 1].insert(0, (history[i - 1][0] - history[i][0]))

    s += history[0][-1]
    t += history[0][0]

print(f'Part 1: {s}')
print(f'Part 2: {t}')
