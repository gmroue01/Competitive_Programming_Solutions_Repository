import sys


def main():
    data = sys.stdin.buffer.read().split()

    n= int(data[0])
    parents = list(range(n))
 

    def find(x):
        root = x
        while parents[root] != root:
            root = parents[root]

        while parents[x] != root:
            parents[x],x=root,parents[x]
        return root
    idx = 1
    removable = []
    for _ in range(n-1):
        a,b = int(data[idx])-1,int(data[idx+1])-1
        idx += 2
        ra,rb = find(a),find(b)
        if ra == rb:
            removable.append((a,b))
        else:
            parents[rb] = ra


    
    roots = []
    seen = set()

    for v in range(n):
        r =  find(v)
        if r not in seen:
            seen.add(r)
            roots.append(r)
    out = [str(len(removable))]

    for i, (a,b) in enumerate(removable):
        u,v = roots[0] , roots[i+1]
        out.append(f"{a+1} {b+1} {u+1} {v+1}")
        parents[find(v)] = find(u)

    print("\n".join(out))    









main()