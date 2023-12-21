print("Anton's solution")
num, exp = 50748685, 242101716911252

for j in range(1, num):
    if j * (num - j) > int(exp):
            print((num/2-j)*2)
            break

print("Eric's solution")

'''
Why not
0 = -h^2 + th - d
h is hold time
t is total time
d is distance travelled
'''

import math

raw = '''Time:      7  15   30
Distance:  9  40  200'''.split('\n')

with open('data06.txt') as f:
    raw = f.read().split('\n')

is_part_one = False
is_efficient = True

if is_part_one:
    t_d = [list(map(int, x.split()[1:])) for x in raw]
else:
    t_d = [[int(x.split(':')[1].replace(' ', ''))] for x in raw]

times = t_d[0]
distances = t_d[1]

final = 1
for i, t in enumerate(times):

    if is_efficient:
        d = distances[i]
    
        a = -1
        b = t
        c = -d
    
        hold_lower = (-b + (b**2 - 4 * a * c)**0.5) / (2 * a)
        hold_upper = (-b - (b**2 - 4 * a * c)**0.5) / (2 * a)
    
        if int(hold_upper) == hold_upper:
            hold_upper -= 1
        if int(hold_lower) == hold_lower:
            hold_lower += 1
    
        wins = math.floor(hold_upper) - math.ceil(hold_lower) + 1
    else:
        wins = 0
        for hold in range(1, t):
            release = t - hold
            calc_distance = release * hold
    
            if calc_distance > distances[i]:
                wins += 1
    
    final *= wins

print(final)
