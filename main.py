testing = True

if testing:
    raw = '''0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45'''.strip().split('\n')
else:
    with open('data09.txt') as f:
        raw = f.read().strip().split('\n')

