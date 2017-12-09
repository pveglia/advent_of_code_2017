import re
from collections import Counter

def load_file():
    with open('./day7.input.txt') as f:
        nodes = {}
        for line in f.readlines():
            match = re.match("([a-z]+) \((\d+)\)(?: -> ([a-z, ]+))?", line)
            nodes[match.group(1)] = {"weight": int(match.group(2)), "children": match.group(3) and match.group(3).split(', ') or []}
        return nodes


def tree_weight(node_name, nodes):
    node = nodes[node_name]
    if "computed_weight" in node:
        return node["computed_weight"]
    else:
        children_weight = [tree_weight(n, nodes) for n in node["children"]]
        if len(set(children_weight)) > 1:
            print(node_name, children_weight, node["children"])
            raise Exception()

        w = node["weight"] + sum(children_weight)
        node["computed_weight"] = w
        return w

def main():
    root = 'svugo'
    nodes = load_file()
    try:
        tree_weight(root, nodes)
    except Exception as e:
        pass

if __name__ == '__main__':
    main()