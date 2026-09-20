import sys



def main():
    data = sys.stdin.buffer.read().split()
    
    N = int(data[0])
    Q = int(data[1])

    parents = list(range(N))
    size = [1]*N
    
    answer = []
    idx = 2
    
    
    def find(x):
        root = x
        
        while parents[root] != root:
            root = parents[root]
        
        while parents[x] != root:
            parents[x],x = root, parents[x]
        
        return root
        
    def union(a,b):
        ra = find(a)
        rb = find(b)
        
        if ra != rb:
            if size[ra] < size[rb]:
                ra,rb=rb,ra
            parents[rb] = ra
            size[ra] += size[rb]
    
    def same(a,b):
        return find(a) == find(b)
    
    
    for _ in range(Q):
        s,a,b = data[idx],int(data[idx+1]),int(data[idx+2])
        idx += 3
        if s == b'?':
            if same(a,b):
                answer.append("yes")
            else:
                answer.append("no")
                
        else:
            union(a,b)
        
    
    for i in range(len(answer)):
        print(answer[i])
        
main()