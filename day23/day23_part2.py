from collections import defaultdict

def parse_input():
    with open("input.txt", "r") as f:
        l = [tuple(line.strip().split("-")) for line in f]
    return l

lans = parse_input()

def bron_kerbosch(R, P, X, adjacency, max_clique):
    if not P and not X:
        if len(R) > len(max_clique[0]):
            max_clique[0] = R.copy()
        return

    pivot = max(P.union(X), key=lambda v: len(adjacency[v]) if v in adjacency else 0)
    for v in P - adjacency[pivot]:
        bron_kerbosch(
            R.union({v}),
            P.intersection(adjacency[v]),
            X.intersection(adjacency[v]),
            adjacency,
            max_clique
        )
        P.remove(v)
        X.add(v)


def find_max_clique(edges):
    adjacency = defaultdict(set)
    adjacency_length = Counter()
    for edge in edges:
        a, b = edge
        adjacency[a].add(b)
        adjacency[b].add(a)
    for k,v in adjacency.items():
        adjacency_length[k]=len(v)
       
    max_clique = [set()]
    bron_kerbosch(set(), set(adjacency.keys()), set(), adjacency, max_clique)
    return max_clique[0]

max_clique = find_max_clique(lans)
print("Largest maximum clique:", ",".join(sorted(max_clique)))

