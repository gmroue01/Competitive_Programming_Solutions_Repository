import sys

def main():
    data = sys.stdin.buffer.read().split()
    N, K = int(data[0]), int(data[1])
    parents = list(range(N + 1))
    size = [1] * (N + 1)

    def find(x):
        root = x
        while parents[root] != root:
            root = parents[root]
        while parents[x] != root:                 # compression de chemin
            parents[x], x = root, parents[x]
        return root

    idx = 2
    for _ in range(K):
        ra, rb = find(int(data[idx])), find(int(data[idx + 1]))
        idx += 2
        if ra != rb:
            if size[ra] < size[rb]:               # union par taille
                ra, rb = rb, ra
            parents[rb] = ra
            size[ra] += size[rb]

    for i in range(1, N // 2 + 1):                # la moitié suffit, la condition est symétrique
        if find(i) != find(N + 1 - i):
            print("No")
            return
    print("Yes")

main()