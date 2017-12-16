movements = open('./day11.input.txt').read().split(',')

offsets = {
    'n': (0, -2),
    'ne': (1, -1),
    'se': (1, 1),
    's': (0, 2),
    'sw': (-1, 1),
    'nw': (-1, -1)
}

def distance(position):
    if abs(position[0]) >= abs(position[1]):
        return abs(position[1]) + (abs(position[0]) - abs(position[1]))
    else:
        return abs(position[0]) + (abs(position[1]) - abs(position[0]))/2

position = (0, 0)
max_distance = 0

for m in movements:
    position = (position[0] + offsets[m][0], position[1] + offsets[m][1])
    max_distance = max(max_distance, distance(position))
    
print('part 1:', distance(position))
print('part2:', max_distance)