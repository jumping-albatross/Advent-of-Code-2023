raw = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")

# with open("data12.txt") as r:
#     raw = r.read().split("\n")

rows = []

for row in raw:
    conditions, backup = row.split(' ')
    conditions = list(conditions)
    backup = [int(x) for x in backup.split(',')]
    rows.append([conditions, backup])

