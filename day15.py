
def gen(start, factor, predicate):
    prev = start
    while True:
        val = (prev * factor) % 2147483647
        if predicate(val):
            yield val
        prev = val

gen = zip(gen(516, 16807, lambda x: x % 4 == 0), gen(190, 48271, lambda x: x % 8 == 0))
mask = (1 << 16) - 1
sum = 0
for i in range(5000000):
    a, b = next(gen)
    sum += 1 if (a & mask) == (b & mask) else 0
print('matches', sum)
