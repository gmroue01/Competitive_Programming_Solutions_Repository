import sys



def find(x,parents):
    root = x
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

    return parents,size

def main():
    data = sys.stdin.buffer.read().split()
    n,q = int(data[0]),int(data[1])
    idx = 2
    parents = list(range(2*n))
    size = [1]*(2*n)

    for _ in range(q):
        op = data[idx]
        if op == b't':
            a,b = int(data[idx+1]),int(data[idx+2])
            parents,size = union(a,b,parents,size)
            idx += 3
        else:
            a = int(data[idx+1])
            print(size[find(a,parents)])
            idx += 2

main()