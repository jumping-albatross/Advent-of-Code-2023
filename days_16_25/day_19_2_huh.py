with open('day_19_testing.txt') as f:
    raw = f.read().split('\n')

aa = {'x':0, 'm':0, 'a':0, 's':0}
for i, l in enumerate(raw):
    print('0123456789' * 3)
    print(l)
    aa['x'] = max(int(aa['x']), int(l[6]))
    aa['m'] = max(int(aa['m']), int(l[14]))
    aa['a'] = max(int(aa['a']), int(l[22]))
    aa['s'] = max(int(aa['s']), int(l[30]))
    for z in 'xmas':
        if aa[z] == 3:
            print(i, aa)
            5/0
print(aa)