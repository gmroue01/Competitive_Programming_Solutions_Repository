import sys



def main():
    data = sys.stdin.buffer.read().split()
    n,m = int(data[0]),int(data[1])

    idx = 2
    commands = [(int(data[2 + 3*j]), int(data[3 + 3*j]), int(data[4 + 3*j])) for j in range(n)]

    parents = list(range(n+1))
    size = [1]*(n+1)

    def find(x):
        root =x 

        while parents[root] !=  root:
            root = parents[root]

        while parents[x] != root:
            parents[x],x = root,parents[x]

        return root

    def union(a,b):
        ra,rb = find(a),find(b)

        if ra != rb:
            if size[ra] <= size[rb]:
                ra,rb=rb,ra

            parents[rb] = ra
            size[ra] += size[rb]

    def same(a,b):
        return find(a) == find(b)

    def move(p,q):
        # Move p to the set containing q ; p -> q 
        rp, rq =find(p),find(q)

        if rp == rq:
            return
        size[rp] -= 1
        new = len(parents)
        parents.append(rq)
        size.append(0)
        node[p] = new

        
        size[rq] += 1
        size[rp] -= 1

            

main()