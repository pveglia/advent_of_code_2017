def part1():
    correct_lines = 0
    with open('day4.input.txt') as f:
        lines = f.readlines()
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            correct_lines += 1
    print(correct_lines)

def part2():
    correct_lines = 0
    with open('day4.input.txt') as f:
        lines = f.readlines()
    for line in lines:
        words = line.split()
        if len(words) == len(set(["".join(sorted(w)) for w in words])):
            correct_lines += 1
    print(correct_lines)
        
if __name__ == '__main__':
    part2()
    