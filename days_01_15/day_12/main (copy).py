raw = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".split(
    "\n"
)

# with open("data12.txt") as r:
#     raw = r.read().split("\n")

rows = []
for row in raw:
    conditions, backups = row.split(" ")
    backups = [int(x) for x in backups.split(",")]
    rows.append([conditions, backups])

field_arrangements = []


def is_damaged_spring(conditions):
    return conditions.find(".") < 0


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

print(f"Part 1:\nObserved arrangements = {sum(field_arrangements)}")
# print(field_arrangements)
print("Expected arrangements = 21")
print("[1, 4, 1, 1, 4, 10]")
