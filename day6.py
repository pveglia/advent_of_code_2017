def load_file():
    with open('./day6.input.txt') as f:
        return [int(b) for b in f.read().split('\t')]

def part1():
    fingerprints = {}
    buckets = load_file()
    steps = 0
    fingerprints[tuple(buckets)] = 0
    while True:
        bmaxBucket, blocks = max(enumerate(buckets), key=lambda i: i[1])

        buckets[bmaxBucket] = 0
        increment = blocks // len(buckets)
        for idx, _ in enumerate(buckets):
            buckets[idx] += increment
        for idx in range(blocks % len(buckets)):
            buckets[(bmaxBucket + 1 + idx) % len(buckets)] += 1
        steps += 1
        if tuple(buckets) in fingerprints:
            break
        fingerprints[tuple(buckets)] = steps
    print('found after {} steps'.format(steps))
    print('cycle size {}'.format(steps - fingerprints[tuple(buckets)]))


if __name__ == '__main__':
    part1()