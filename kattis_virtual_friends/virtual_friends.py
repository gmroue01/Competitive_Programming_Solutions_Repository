import sys


def find(x,parents):
    root =x 
    while parents[root] != root:
        root = parents[root]

    while parents[x] != root:
        parents[x],x = root,parents[x]

    return root

def union(a,b,parents,size):
    ra,rb = find(a,parents),find(b,parents)
    if ra != rb:
        if size[ra] < size[rb]:
            ra,rb=rb,ra
        parents[rb] = ra
        size[ra] += size[rb]
    return size[ra]

def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    idx = 1
    out = []
    for _ in range(n):
        F = int(data[idx])
        idx += 1
        parents = list(range(2*F))
        size = [1]*(2*F)

        ids = {}
        

        for _ in range(F):
            f1,f2 = data[idx],data[idx+1]
            idx += 2
            if f1 not in ids:
                ids[f1] = len(ids)
            if f2 not in ids:
                ids[f2] = len(ids)

            out.append(union(ids[f1],ids[f2],parents,size))

    print("\n".join(map(str,out)))            

main()