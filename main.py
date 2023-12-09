testing = True

if testing:
    raw = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.strip().split('\n')
else:
    with open('data09.txt') as f:
        raw = f.read().strip().split('\n')

sequences = [list(map(int, x.strip().split())) for x in raw]

# predict next number in sequence

def differences(s):
    new_s = []
    for i in range(len(s) - 1):
        new_s.append(s[i+1] - s[i])
    return new_s

s = 0

for sequence in sequences:
    rounds = [sequence]
    while sum(rounds[-1]) != 0:
        rounds.append(differences(rounds[-1]))
    for i in range(len(rounds) - 1, 0, -1):
        rounds[i - 1].append(rounds[i][-1] - rounds[i][-2])