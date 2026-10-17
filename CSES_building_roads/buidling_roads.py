import sys












def main():
    input = sys.stdin.readline
    n,m = map(int,input().split())


    parents = list(range(n))
    size = [1]*n
    def find(i):
        root = i
        while parents[root] != root:
            root = parents[root]

        while parents[i] != root:
            parents[i],i = root, parents[i]

        return root


    def union(a,b):
        ra,rb = find(a),find(b)
        if ra != rb:

            if size[ra] < size[rb]:
                ra,rb = rb,ra
            parents[rb] = ra
            size[ra] += size[rb]




        
    for _ in range(m):

        i,j = map(int,input().split())
        i = i-1
        j = j-1
 
        union(i,j)

    roots = [x for x in range(n) if parents[x] == x]
    print(len(roots)-1)


    for k in range(len(roots)-1):
        index_1 = parents.index(roots[k])
        index_2 = parents.index(roots[k+1])
        print(f"{index_1+1} {index_2+1}")

             





main()
