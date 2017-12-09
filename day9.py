def load_input():
    with open('./day9.input.txt') as f:
        return f.read();

def part1():
    input = load_input()
    nesting = 0
    sum_part1 = 0
    sum_part2 = 0
    in_garbage = False
    idx = 0
    while idx < len(input):
        if input[idx] == '<' and not in_garbage:
            in_garbage = True
            idx += 1
            continue
        if in_garbage and input[idx] == '!': # skip next char
            idx += 2
            continue
        if in_garbage and input[idx] == '>':
            in_garbage = False
            idx += 1
            continue
        if in_garbage:
            sum_part2 += 1
            idx += 1
            continue
        if not in_garbage and input[idx] == '{': # open group
            nesting += 1
            sum_part1 += nesting
            idx += 1
            continue
        if not in_garbage and input[idx] == '}':
            nesting += -1
            idx += 1
            continue
        idx += 1
    print('at the end', sum_part1, sum_part2, nesting)

if __name__ == '__main__':
    part1()