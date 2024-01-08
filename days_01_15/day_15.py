if 0:
    raw = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".split(',')
else:
    with open('day_15.dat') as f:
        raw = f.read().split(',')

steps = raw


def HASH(value):
    h = 0
    for ch in value:
        asc2i = ord(ch)
        h += asc2i
        h *= 17
        h %= 256
    return h


print(f"Part 1: {sum([HASH(s) for s in steps])}")

boxes_256 = [[] for _ in range(256)]

for step in steps:
    op_idx = max(step.find('-'), step.find('='))
    label = step[:op_idx]
    box_num = HASH(label)

    if step[op_idx] == '-':
        # dash (-): remove lens from box with label and keep original order
        for i in range(len(boxes_256[box_num])):
            if boxes_256[box_num][i][0] == label:
                boxes_256[box_num].pop(i)
                break
    else:
        # equals (=) and focal length:
        #  1. if old lens with same label, remove and replace in place
        focal_length = int(step[op_idx + 1:])

        for i in range(len(boxes_256[box_num])):
            if boxes_256[box_num][i][0] == label:
                boxes_256[box_num][i][1] = focal_length
                break
        else:
            #  2. if no lens with same label, add to the end of the list
            boxes_256[box_num].append([label, focal_length])

focusing_power = 0

for box_num, lenses in enumerate(boxes_256):
    for slot_num, (label, focal_length) in enumerate(lenses):
        # One plus the box number of the lens in question.
        # The slot number of the lens within the box: 1 for the first lens, 2 for the second lens, and so on.
        # The focal length of the lens.
        focusing_power += (box_num + 1) * (slot_num + 1) * focal_length

print(f"Part 2: {focusing_power = }")

# print("""TODO
# dentist
# optometrist
# letter to doc
# note to aunluk
# sms DS
# """)
