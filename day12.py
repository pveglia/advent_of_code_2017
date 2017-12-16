links = {}
visited = set()
group = 0
groups = 0

for line in open('./day12.input.txt').readlines():
    fromid, tos = line.strip().split(' <-> ')
    tos = tos.split(', ')
    links[fromid] = tos

nodes = set(links.keys())

def visit(node):
    global group
    if node in visited:
        return
    else:       
        visited.add(node)
        group += 1
        for n in links[node]:
            visit(n)

visit('0')

print(group)

# part 2
visited = set()
not_visited = nodes - visited
while len(not_visited):
    print(not_visited)
    groups += 1
    visit(not_visited.pop())
    not_visited = nodes - visited
print('groups', groups)