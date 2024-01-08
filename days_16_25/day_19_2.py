if False:
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
else:
    with open("day_19.dat") as f:
        raw = f.read().strip()


raw_i, raw_parts = raw.split('\n\n')
raw_i = raw_i.split('\n')

instructions = {}

for inst in raw_i:
    name, _r = inst[:-1].split('{')
    rules = [x.split(":") if ':' in x else x for x in _r.split(',')]
    for r in rules:
        if type(r) == list:
            print(r)
            
    print(name, ",", rules)
    instructions[name] = rules
    
    # c = {'x' : 0, 'm' : 0, 'a' : 0, 's' : 0}
    # for a in 'xmas':
    #     for r in rules:
    #         if type(r) == list:
    #             c[a] += r[0].count(a)
    # print(c)
    

print()

XMAS = {}
for i, l in enumerate('xmas'):
    XMAS[l] = i

c = 0

def rec(dest_in, ranges_in):
    global c
    c += 1

    print(f"Recursion #{c}: {dest_in = }, {ranges_in = }")

    if dest_in == 'A':
        return ranges_in
    if dest_in == 'R':
        return None

    ranges_returned = []
    ranges_out = [[],[],[],[]]
    for i in instructions[dest_in]:
        if type(i) != list:
            ranges_returned.append(rec(i, ranges_in))
        else:
            condition, name = i
            idx = XMAS['x']
    return ranges_returned
# recursion

possibilities = rec('in', ((),(),(),()))
print(f"{possibilities = }")
print(f"{possibilities = } vs 167409079868000; % = {(possibilities - 167409079868000)/167409079868000 * 100:.1f}")