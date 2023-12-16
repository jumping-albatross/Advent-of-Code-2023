raw = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7""".split(',')

with open('data15.txt') as f:
    raw = f.read().split(',')

steps = raw
t = 0

for step in steps:
    current = 0
    for ch in step:
        ascii = ord(ch)
        current += ascii
        current *= 17
        current %= 256
    t += current

print(t)