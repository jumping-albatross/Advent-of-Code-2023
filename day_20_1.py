import heapq

raw = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> in
&in -> a""".split('\n')

# raw = """broadcaster -> a
# %a -> in, co
# &in -> b
# %b -> co
# &co -> output""".split('\n')

with open('day20.txt') as f:
    raw = f.read().split('\n')

modules = {}
order = []
LOW = 0
HIGH = 1

# prepare modules
for line in raw:
    dest = line.split(' -> ')[1].split(', ')

    # broadcast
    if line[:len("broadcaster")] == "broadcaster":
        modules['broadcaster'] = ['broadcaster', [*dest]]
    else:
        name = line[1:3].strip()
        _type = 'flip-flop' if line[0] == "%" else 'conjunction'
        v = [dest, LOW] if _type == 'flip-flop' else [dest, {}]
        modules[name] = [_type, *v]
        order.append(name)

# program the conjunctions
for name, details in modules.items():
    print(f"35{details = }")
    for dest in details[1]:
        if dest == 'output' or dest == 'rx':
            continue
        if modules[dest][0] == 'conjunction':
            modules[dest][2][name] = LOW

_c = 0
lows = 0  # starts with 1 LOW button push
highs = 0


def push(signal, source, destinations):
    """Push signal (LOW, HIGH), source module and destination module(s) onto queue"""

    global _c, lows, highs
    print(f"PUSH: {_c:3} {'HIGH' if signal else 'LOW':>5}, {source:>12} >>> {destinations}")

    if signal == LOW:
        lows += len(destinations)
    else:
        highs += len(destinations)

    for d in destinations:
        if type(d) == list:
            print(f"#####     PUSH: {_c} {'HIGH' if signal else 'LOW'}, {source = }, {destinations = }")
            print(f"{destinations = }... this is the problem")
            raise Exception('oops. List')
        _c += 1
        heapq.heappush(q, [_c, signal, source, d])


is_trouble_shooting = False

q = []
for i in range(1000):
    push(LOW, 'button', ['broadcaster'])
    r = 0
    while q:
        r += 1
        _, signal, src, name = heapq.heappop(q)
        if name != 'output' and name != 'rx':
            module = modules[name]
        else:
            continue

        if is_trouble_shooting:
            print(f"        Q heappop ({r}): {signal = }, {src = }, {name = }, {module = }")

        if src == 'button':
            if is_trouble_shooting:
                print(f"TROUBLE 80: {module = }")
                print(f"#*#*#*#* 81: {module = }")
            push(LOW, 'broadcaster', module[1])
        elif module[0] == 'flip-flop' and signal == LOW:
            if is_trouble_shooting:
                print(f"     flip-flop: {modules[name] = }")

            modules[name][2] = 1 - modules[name][2]
            push(modules[name][2], name, modules[name][1])
        elif module[0] == 'conjunction':
            # may the SOURCE be with you
            if is_trouble_shooting:
                print(f"     conjunction: {modules[name] = }")
            modules[name][2][src] = signal
            s = 0
            for stat in modules[name][2].values():
                s += stat
                if is_trouble_shooting:
                    print(f"***** {s = }, {len(modules[name][2].values()) = }")
            if s == len(modules[name][2].values()):
                push(LOW, name, modules[name][1])
            else:
                push(HIGH, name, modules[name][1])

print(f"{lows = }, {highs = }, ({lows * highs = }) {lows * highs - 32000000 = }")
# flip-flop (%)
# default: initially off
# receive: if receive HIGH ignore
# receive: if receive LOW flips states AND sends HIGH if turns ON or LOW if turns off

# conjunction (&)
# default: LOW
# receive: upon receipt of pulse it remembers most recent state
# receive, part 2: if all HIGH send LOW, otherwise send HIGH

# broadcast module (broadcaster)
# rebroadcasts received pulse to all destination modules

# button module (button)
# single LOW to broadcaster
