#https://github.com/oloturia/AoC2023/blob/main/day21/part1.py
#
testing = True

if testing:
    grid = """

1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
""".strip().split('\n')
else:
    with open('day_22.txt') as f:
        grid = f.read().strip().split('\n')
