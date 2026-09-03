
from collections import Counter
n, r = map(int, input().split())


def complement(m):
    return tuple(1-b for b in m)






bitvec = [[0]*(2*n) for _ in range(r)]
somme = 0
for i in range(r):
    topic_ranking = list(map(int, input().split()))
    for j in range(2*n):
        if topic_ranking[j] > n:
            bitvec[i][j] = 1
        



motifs = []
for j in range(2*n):
    m = tuple(bitvec[i][j] for i in range(r))
    motifs.append(m)


compte = Counter(motifs)

possible = all(compte[m] == compte[complement(m)] for m in compte)


if possible:
    print("possible")
else:
    print("impossible")

