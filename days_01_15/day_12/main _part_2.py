raw = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split("\n")

with open("day_12.dat") as r:
    raw = r.read().split("\n")

rows = []
for row in raw:
    conditions, backups = row.split(" ")
    backups = [int(x) for x in backups.split(",")]
    rows.append([conditions, backups])

is_part_two = True
if is_part_two:
    # unfold
    for i, row in enumerate(rows):
        rows[i][0] = row[0] + ("?" + row[0]) * 4
        rows[i][1] = row[1] * 5

field_arrangements = []


def is_damaged_spring(conditions):
    return conditions.find(".") < 0


def memoize(f):
    memo = {}

    def helper(x, y):
        if (x, tuple(y)) not in memo:
            memo[(x, tuple(y))] = f(x, y)
        return memo[(x, tuple(y))]

    return helper


@memoize
def try_round(c_s, backups):
    """Assume discarded conditions that have been examined are possible"""

    i = 0
    offset = backups[0]

    arrangements = 0

    while i + offset <= len(c_s):
        is_damaged = is_damaged_spring(c_s[i : i + offset])

        if is_damaged and c_s[:i].find("#") == -1:
            if len(backups) == 1:
                if len(c_s) == i + offset:
                    return arrangements + 1
                else:
                    if c_s[i + offset :].find("#") == -1:
                        arrangements += 1
            elif i + offset < len(c_s) and c_s[i + offset] != "#":
                arrangements += try_round(c_s[i + offset + 1 :], backups[1:])
        i += 1
    return arrangements


for conditions, backups in rows:
    arrangements = try_round(conditions, backups)
    field_arrangements.append(arrangements)

print(f"Part 2:\nObserved arrangements = {sum(field_arrangements)}")
# print(field_arrangements)
print("Expected arrangements = 525152")
print("[1, 16384, 1, 16, 2500, 506250]")
