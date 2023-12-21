with open('data03.txt') as f:
    raw = f.read().split('\n')

# raw = '''467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..'''.split('\n')

raw = [x.strip() for x in raw]

# for _r in raw:
#     print(_r)

s = 0

for r in range(len(raw)):
    is_part = False
    n = ''
    for c in range(len(raw[r])):
        if raw[r][c].isdigit():
            n += raw[r][c]
            rl = len(raw) - 1
            cl = len(raw[r]) - 1
            # test for adjacent symbol
            adj_chars = ''
            adj_chars += raw[max(r - 1, 0)][max(c - 1, 0)]
            adj_chars += raw[max(r - 1, 0)][c]
            adj_chars += raw[max(r - 1, 0)][min(c + 1, cl)]
 
            adj_chars += raw[r][max(c - 1, 0)]
            adj_chars += raw[r][min(c + 1, cl)]

            adj_chars += raw[min(r + 1, rl)][max(c - 1, 0)]
            adj_chars += raw[min(r + 1, rl)][c]
            adj_chars += raw[min(r + 1, rl)][min(c + 1, cl)]

            for ch in adj_chars:
                if not ch.isdigit() and ch != '.':
                    is_part = True
                    break
        else:
            if n != '' and is_part:
                s += int(n)
            n = ''
            is_part = False
    if n != '' and is_part:
        s += int(n)
    n = ''
    is_part = False
    
print("Part 1", s)