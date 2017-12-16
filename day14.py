from day10 import knothash
from functools import reduce, lru_cache

@lru_cache()
def char2bits(c):
    return '{:04b}'.format(int(c, 16))

total = 0
rows = []
for linen in range(128):
    key = "ffayrhll-{}".format(linen)
    bits = ''.join(char2bits(c) for c in knothash(key))
    rows.append([{'zone': None, 'bit': b} for b in bits])
    total += sum(1 for b in bits if b == '1')

print('part 1', total)

# part 2
def visit(pos, current_zone, rows):
    cell = rows[pos[0]][pos[1]]
    if cell['zone'] == None and cell['bit'] == '1':
        cell['zone'] = current_zone
        for n in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
            neighbor = (pos[0] + n[0], pos[1] + n[1])
            if neighbor[0] < 0 or neighbor[0] >= 128 or neighbor[1] < 0 or neighbor[1] >= 128:
                continue
            visit(neighbor, current_zone, rows)

next_zone = 0
for ri, row in enumerate(rows):
    for ci, cell in enumerate(row):
        if cell['bit'] == '1' and cell['zone'] == None:
            # visit neighbord
            visit((ri, ci), next_zone, rows)
            next_zone += 1

print('part 2', next_zone)