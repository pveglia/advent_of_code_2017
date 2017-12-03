import itertools
import sys

right = [1, 0]
up = [0, -1]
left = [-1, 0]
down = [0, 1]

moves = [up, left, down, right]

def move(pos, direction):
    return [pos[0] + direction[0], pos[1] + direction[1]]

def part1():
    print(sys.argv)
    input = int(sys.argv[1])
    positions = {1: [0, 0]}
    counter = 2
    last_pos = [0, 0]
    try:
        for i in itertools.count(2, step=2):
            print(i)
            # go one step right
            positions[counter] = move(last_pos, right)
            last_pos = positions[counter]
            counter += 1
            for direction in moves:
                steps = i - 1  if direction == up else i
                for _ in range(steps):
                    positions[counter] = move(last_pos, direction)
                    last_pos = positions[counter]
                    counter += 1
                    if counter > input:
                        raise Exception()
    except Exception:
        print(positions)
        print(sum(map(abs, positions[input])))

def toKey(pos):
    return ":".join(str(i) for i in pos)

neighbors = [[0,-1], [1,-1], [1,0], [1,1], [0,1], [-1,1], [-1,0], [-1,-1]]

def sumNeighbors(pos, values):
    sum = 0
    for n in neighbors:
        nkey = toKey([pos[0] + n[0], pos[1] + n[1]])
        if nkey in values:
            sum += values[nkey]
    return sum

def part2():
    print(sys.argv)
    input = int(sys.argv[1])
    positions = {1: [0, 0]}
    last_pos = [0, 0]
    pos2value = {toKey(last_pos): 1}
    sum_value = 0
    try:
        for i in itertools.count(2, step=2):
            print(i)
            # go one step right
            last_pos = move(last_pos, right)i += 1;
            sum_value = sumNeighbors(last_pos, pos2value)
            pos2value[toKey(last_pos)] = sum_value
            if sum_value > input:
                raise Exception()
            for direction in moves:
                steps = i - 1  if direction == up else i
                for _ in range(steps):
                    last_pos = move(last_pos, direction)
                    sum_value = sumNeighbors(last_pos, pos2value)
                    pos2value[toKey(last_pos)] = sum_value
                    if sum_value > input:
                        raise Exception()
    except Exception as e:
        print(e)
        print(pos2value)
        print(sum_value)
        # print(sum(map(abs, positions[input])))


if __name__ == '__main__':
    part2()