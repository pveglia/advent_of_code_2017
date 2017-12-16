from functools import reduce
from itertools import zip_longest

def reverse(list, start_pos, n):
    ll = len(list)
    s = start_pos
    e = start_pos + n -1
    while s < e:
        list[s%ll], list[e%ll] = list[e%ll], list[s%ll]
        s += 1
        e += -1
    return list

def group(l, n):
    args = [iter(l)] * n
    return list(zip_longest(*args))

def knothash(input):
    lengths = [ord(i) for i in input] + [17, 31, 73, 47, 23]
    l = list(range(256))
    ll = len(l)
    current = 0
    skip = 0
    for _ in range(64):
        for i in lengths:
            reverse(l, current, i)
            current += (i + skip) % ll
            skip += 1
    return("".join([format(reduce(lambda acc, i: acc ^ i, g), '02x') for g in group(l, 16)]))


