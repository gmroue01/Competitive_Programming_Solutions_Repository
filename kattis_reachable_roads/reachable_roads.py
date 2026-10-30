import sys


def main():

    data = sys.stdin.buffer.read().split()

    n = int(data[0])
    idx = 1


    
    for i in range(n):
        m,r = int(data[idx]),int(data[idx+1])
        parents = list(range(m))

        def find(x):
            root = x

            while parents[root] != root:
                root = parents[root]

            while parents[x] != root:
                parents[x],x = root, parents[x]

            return root

        idx += 2
        components = m
        for j in range(r):
            

            a = int(data[idx + 2*j])
            b = int(data[idx + 2*j + 1])
            ra, rb = find(a), find(b)


            if ra != rb:
                parents[rb] = ra
                components -= 1
        print(components - 1)   

        idx += 2*r



main()