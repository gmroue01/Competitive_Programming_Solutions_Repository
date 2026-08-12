n = int(input())
die1 = list(map(int, input().split()))
die2 = list(map(int, input().split()))

comb = []

for i in range(n):
    for j in range(n):
        comb.append([die1[i], die2[j]])


count = [0]*(n**2)

r1 = 0
r2 = 0
for i in range(n**2):
    e = comb[i]
    if e[0] > e[1]:
        r1 += 1
    elif e[0] < e[1]:
        r2 += 1

if (r1 > r2):
    print("first")
elif (r1 < r2):
    print("second")
else:
    print("tie")
