from collections import defaultdict

firewalls = defaultdict(int)

for line in open('./day13.input.txt').readlines():
    layer, depth = map(int, line.strip().split(': '))
    firewalls[layer] = depth

max_layer = max(firewalls.keys())
print(max_layer)

delay = 0
while True:
    caught = False
    for step in range(max_layer + 1):
        caught = firewalls[step] != 0 and (step + delay) % (firewalls[step] * 2 - 2) == 0
        if caught:
            delay += 1
            break
    # print(severity)
    if not caught:
        print('good one', delay)
        break
