def part1():
    instructions = None
    with open('./day5.input.txt') as f:
        instructions = [int(l) for l in f.readlines()]
    ic = 0
    steps = 0
    while(True):
        nextIndex = ic + instructions[ic]
        instructions[ic] += 1
        ic = nextIndex
        steps += 1
        if ic < 0 or ic >= len(instructions):
            print(steps)
            break

def part2():
    instructions = None
    with open('./day5.input.txt') as f:
        instructions = [int(l) for l in f.readlines()]
    ic = 0
    steps = 0
    while(True):
        nextIndex = ic + instructions[ic]
        instructions[ic] += -1 if instructions[ic] >= 3 else 1
        ic = nextIndex
        steps += 1
        if ic < 0 or ic >= len(instructions):
            print(steps)
            break

if __name__ == '__main__':
    part1()
    part2()