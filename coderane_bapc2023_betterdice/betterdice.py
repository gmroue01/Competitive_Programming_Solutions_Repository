n = int(input())
die1 = list(map(int, input().split()))
die2 = list(map(int, input().split()))

comb = []

for i in range(n):
    for j in range(n):
        comb.append([die1[i], die2[j]])
print(comb)

count = [0]*(n**2)


for i in range(n**2):
    e = comb[i]
    if e[0] > e[1]:
        count[i] += 1

print(count)

p = sum(count)/(n**2)

if (p > 0.5):
    print("first")
elif (p < 0.5):
    print("second")
else:
    print("tie")
