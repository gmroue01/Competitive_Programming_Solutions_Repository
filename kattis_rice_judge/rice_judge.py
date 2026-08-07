N = int(input())
pref = input()
rices = []
for i in range(N):
    A, S = map(int, input().split())
    rices.append([A, S, A+S, i])


if pref == "antal":
    rices_sorted_by_score = sorted(
        rices, key=lambda x: (x[2], x[0]), reverse=True)
else:
    rices_sorted_by_score = sorted(
        rices, key=lambda x: (x[2], x[1]), reverse=True)

print(rices_sorted_by_score[0][-1])
