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

raw = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a""".split('\n')

# with open('day20.txt') as f:
#     raw = f.read().split('\n')


modules = {}
order = []

for line in raw:
    if line[:len("broadcaster")] == "broadcaster":
        broadcaster = line.split('-> ')[1].split(', ')
    elif line[0] == "%":
        
    elif line[0] == "&":
        pass
    else:
        raise Exception(f"{line} not processed")