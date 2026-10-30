import sys



def main():
    data= sys.stdin.buffer.read().split()
    n,m = int(data[0]),int(data[1])

    parents = list(range(n))
    size = [1]*n
    def find(x):
        root = x

        while parents[root] != root:
            root = parents[root]

        while parents[x] != root:
            parents[x],x = root,parents[x]
        return root    

    idx = 2
    for _ in range(m):
        k = int(data[idx])
        idx += 1
        for i in range(k-1):
    
            ra,rb = find(int(data[idx+ i ]) - 1),find(int(data[idx+ i + 1]) -1)

            if ra != rb:
                if size[ra] < size[rb]:
                    ra,rb=rb,ra

                parents[rb] = ra
                size[ra] += size[rb]
        idx += k


    out = [size[find(i)] for i in range(n)]
         




    print(' '.join(map(str,out)))


main()