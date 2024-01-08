with open('day_03.dat') as f:
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

raw = ['.' * len(raw[0])] + raw + ['.' * len(raw[0])]
raw = ['.' + x.strip() + '.' for x in raw]

# for _r in raw:
#     print(_r)

s = 0

def extract_str_number(r, c):
    '''Given the row and column of a known digit extract the whole number as a string'''
    while c > 0:
        c -= 1
        if not raw[r][c].isdigit():
            c += 1
            break

    n = ''
    for i in range(c, len(raw[r])):
        if raw[r][i].isdigit():
            n += raw[r][i]
        else:
            return(n)

for r in range(len(raw)):
    for c in range(len(raw[r])):
        if raw[r][c] == '*':
            # test for adjacent symbol
            gears = []

            if raw[r - 1][c - 1].isdigit():
                gears.append(extract_str_number(r-1,c-1))
                if not raw[r-1][c].isdigit() and raw[r-1][c+1].isdigit():
                        gears.append(extract_str_number(r-1,c+1))
            elif raw[r - 1][c].isdigit():
                gears.append(extract_str_number(r-1,c))
            elif raw[r - 1][c+1].isdigit():
                gears.append(extract_str_number(r-1,c+1))

            if raw[r][c - 1].isdigit():
                gears.append(extract_str_number(r,c-1))
            if raw[r][c+1].isdigit():
                gears.append(extract_str_number(r,c+1))

            if raw[r + 1][c - 1].isdigit():
                gears.append(extract_str_number(r+1,c-1))
                if not raw[r+1][c].isdigit() and raw[r+1][c+1].isdigit():
                        gears.append(extract_str_number(r+1,c+1))
            elif raw[r + 1][c].isdigit():
                gears.append(extract_str_number(r+1,c))
            elif raw[r + 1][c+1].isdigit():
                gears.append(extract_str_number(r+1,c+1))
            if len(gears) == 2:
                print(gears)
                s += int(gears[0]) * int(gears[1])
    
print(f"WRONG: {s} vs 467835 = {s - 467835}" if s != 467835 else "SUCCESS")
print("Part 2", s)