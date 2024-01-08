# note: manually find and replace '  ' with ' '

raw = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''

with open('day_04.dat') as f:
    raw = f.read()

raw = [x.split(': ')[1] for x in raw.split('\n')]
raw = [x.strip().split(' | ') for x in raw]
raw = [[set(x[0].split()), set(x[1].split())] for x in raw]

s = 0  # sum of 2**(wins-1) where win > 0
for card in raw:
    s += int(2**(len(card[0] & card[1]) - 1))

print('Part 1 Goal', 13)
print(f'Part 1 = {s}')

t = 0  # total scratchcards
scratchcards = list(range(len(raw)))

while len(scratchcards) > 0:
    c_id = scratchcards.pop()
    t += 1
    card = raw[c_id]
    wins = len(card[0] & card[1])
    new_cards = list(range(c_id + 1, c_id + 1 + wins))
    scratchcards += new_cards

print(t)
