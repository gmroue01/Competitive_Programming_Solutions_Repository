n = int(input())
forks = list(map(int, input().split()))

forks_sorted = sorted(forks)

print(forks_sorted[0] + forks[1])
