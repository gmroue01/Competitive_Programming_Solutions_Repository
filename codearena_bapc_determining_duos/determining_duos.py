n, r = map(int, input().split())


expected_score = 0.5*(n*r)*(3*n+1)


rank = []


for i in range(r):
    topic_ranking = list(map(int, input().split()))
    rank.append(topic_ranking)


possible = False
score = []
for i in range(n):
    current = rank[0][i]
    for j in range(1, n):
        if i != j:
            max_r = max(rank[1][j])
            max_r = max(max_r, r)
            score.append(max_r)


for s in score:
    if s == expected_score:
        possible = True


if possible:
    print("possible")
else:
    print("impossible")
