from collections import defaultdict
import operator

ops = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '<=': operator.le,
    '>': operator.gt,
    '>=': operator.ge,
    'inc': operator.add,
    'dec': lambda a, b: a - b
}

regs = defaultdict(int)
max_value = 0
for dst, op, q, _, cr, cop, cv in [l.split() for l in open('./day8.input.txt').readlines()]:
    if ops[cop](regs[cr], int(cv)):
        computed = ops[op](regs[dst], int(q))
        regs[dst] = computed
        if computed > max_value:
            max_value = computed

print('part 1:', max(regs.values()))
print('part 2:', max_value)
