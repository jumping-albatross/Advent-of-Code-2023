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


def try_round(conditions, backups):
    """Assume incoming conditions are not impossible"""

    # print(f"Incoming: {conditions}, {backups}")
    idx = 0
    offset = backups[0]

    arrangements = 0

    while idx + offset <= len(conditions):
        is_damaged = is_damaged_spring(conditions[idx : idx + offset])

        # print(
        #     f'line 37, {is_damaged}, "{conditions[idx : idx + offset]}", {idx}, "{conditions[:idx]}"'
        # )

        if is_damaged and conditions[:idx].find("#") == -1:
            # print(f"here len(backups) = {len(backups)}, backups = {backups}, idx = {idx}")
            if len(backups) == 1:
                if len(conditions) == idx + offset:
                    return arrangements + 1
                else:
                    if conditions[idx + offset :].find("#") == -1:
                        arrangements += 1
            elif idx + offset < len(conditions) and conditions[idx + offset] != "#":
                # print(
                #     f"   Call: {conditions[idx + offset + 1:]}     {backups[1:]}"
                # )
                arrangements += try_round(conditions[idx + offset + 1 :], backups[1:])
        idx += 1
    # print("return", arrangements, conditions, backups)
    return arrangements


for conditions, backups in rows:
    arrangements = try_round(conditions, backups)
    field_arrangements.append(arrangements)

print("Arrangements", sum(field_arrangements))
# print(field_arrangements)
print("Expected arrangements", 21)
print("[1, 4, 1, 1, 4, 10]")
