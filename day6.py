def load_file():
    with open('./day6.input.txt') as f:
        return [int(b) for b in f.read().split('\t')]

def getMaxBucket(buckets):
    max = 0
    index = 0
    for idx, b in enumerate(buckets):
        if b > max:
            max = b
            index = idx
    return (index, max)

def part1():
    fingerprints = {}
    buckets = load_file()
    print(buckets)
    steps = 0
    fingerprints[tuple(buckets)] = 0
    while True:
        bmaxBucket, blocks = getMaxBucket(buckets) 
        buckets[bmaxBucket] = 0
        increment = blocks // len(buckets)
        for idx, _ in enumerate(buckets):
            buckets[idx] += increment
        for idx in range(blocks % len(buckets)):
            buckets[(bmaxBucket + 1 + idx) % len(buckets)] += 1
        steps += 1
        print('after step {}'.format(steps))
        print(buckets)
        if tuple(buckets) in fingerprints:
            print('found after {} steps'.format(steps))
            print('cycle size {}'.format(steps - fingerprints[tuple(buckets)]))
            break
        fingerprints[tuple(buckets)] = steps


if __name__ == '__main__':
    part1()