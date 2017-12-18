moves = open('./day16.input.txt').read().split(',')

programs = [chr(ord('a') + i) for i in range(16)]

encoutered = set()
countdown = None

print(programs)

for i in range(40):
    for pc, m in enumerate(moves):
        if m[0] == 's':
            # spin
            n = int(m[1:])
            programs = programs[-n:] + programs[:-n]
        if m[0] == 'x':
            pos1, pos2 = map(int, m[1:].split('/'))
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        if m[0] == 'p':
            p1, p2 = m[1:].split('/')
            pos1, pos2 = programs.index(p1), programs.index(p2)
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        key = "{}|{}".format(pc, ''.join(programs))
        if key in encoutered:
            print('already found', key, i)
            raise Exception()
        else:
            encoutered.add(key)
print(''.join(programs))