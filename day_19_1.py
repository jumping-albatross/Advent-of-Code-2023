raw = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}""".strip()

with open("data19.txt") as f:
    raw = f.read().strip()

def generate_part(part):
    """converts x=,m=,a=,s= to (x, m, a, s)"""
    xmas = [int(p.split('=')[1]) for p in part]
    return tuple(xmas)

raw_i, raw_parts = raw.split('\n\n')
raw_i = raw_i.split('\n')
parts = raw_parts.split('\n')
for i, p in enumerate(parts):
    parts[i] = generate_part(p[1:-1].split(','))

X, M, A, S = 0, 1, 2, 3
instructions = {}

for inst in raw_i:
    name, _r = inst[:-1].split('{')
    rules = [x.split(":") if ':' in x else x for x in _r.split(',')]
    print(name, rules)
    instructions[name] = rules

def check_part(part, dest):
    x, m, a, s = part
    print(part, dest, x, m, a, s)
    rule = instructions[dest]
    for r in rule[:-1]:
        if type(r) == list:
            if eval(r[0]):
                return r[1]
    else:
        return rule[-1]

accepted = []
for part in parts:
    dest = check_part(part, 'in')
    while dest != 'A' and dest != 'R':
        dest = check_part(part, dest)

    if dest == 'A':
        accepted.append(part)

print()
print(f"n = {len(accepted)}")
s = 0
for good in accepted:
    s += sum(good)
print(f"sum = {s}")