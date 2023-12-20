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

# with open("data19.txt") as f:
#     raw = f.read().strip()


raw_i, raw_parts = raw.split('\n\n')
raw_i = raw_i.split('\n')

instructions = {}

for inst in raw_i:
    name, _r = inst[:-1].split('{')
    rules = [x.split(":") if ':' in x else x for x in _r.split(',')]
    print(name, rules)
    instructions[name] = rules

possibilities = 0

for a in instructions['in']:
    