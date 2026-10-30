import sys



def main():
    data = sys.stdin.buffer.read().split()
    N,L  = int(data[0]),int(data[1])
    idx = 2

    parents = list(range(L))
    cycle= [False]*L
    out = []

    def find(x):
        root = x
        while parents[root] != root:
            root = parents[root]

        while parents[x] != root:
            parents[x],x = root, parents[x]
        return root

    for _ in range(N):
        a,b = int(data[idx]) - 1, int(data[idx+1])-1
        idx += 2
        ra,rb = find(a),find(b)
        print(cycle)
        if ra == rb:
            if cycle[ra]:
                out.append("SMECE")
            else:
                cycle[ra]=True
                out.append("LADICA")
        elif cycle[ra] and cycle[rb]:
            out.append("SMECE")
        else:
            parents[rb] = ra
            cycle[ra] = cycle[ra] or cycle[rb]
            out.append("LADICA")        


    print("\n".join(out))

main()