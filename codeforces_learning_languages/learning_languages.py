import sys


def main():

    data = sys.stdin.buffer.read().split()

    n, m = int(data[0]), int(data[1])
    parents = list(range(n))
    size = [1]*n

    def find(x):
        root = x

        while parents[root] != root:
            root = parents[root]

        while parents[x] != root:
            parents[x],x = root, parents[x]

        return root

    
    employee_languages = [[] for _ in range(n)]

    idx = 2
    for i in range(n):
        k = int(data[idx])
        employee_languages[i] = list(map(int, data[idx+1: idx + 1 + k]))
        idx += 1 + k

    employee_languages = sorted(employee_languages,key = lambda x : len(x),reverse=True)
    if sum([len(v) for v in employee_languages]) == 0:
        print(n)

    else:
        for j in range(n):
            for i in range(j+1, n):
    
                value = set(employee_languages[j]) & set(employee_languages[i])
                if value:
                    ra,rb = find(j),find(i)

                    if ra != rb:
                        if size[ra] < size[rb]:
                            ra,rb=rb,ra
                        parents[rb] = ra
                        size[ra] += size[rb]
        print(len(set(parents)) -1)


main()
