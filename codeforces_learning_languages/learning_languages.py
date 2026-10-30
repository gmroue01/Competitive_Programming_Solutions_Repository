import sys


def main():

    data = sys.stdin.buffer.read().split()

    n, m = int(data[0]), int(data[1])

    employee_languages = [[] for _ in range(n)]

    idx = 2
    for i in range(n):
        k = int(data[idx])

        employee_languages[i] = list(map(int, data[idx+1: idx + 1 + k]))
        idx += 1 + k
    employee_languages = sorted(
        employee_languages, key=lambda x: len(x), reverse=True)
    print(employee_languages)
    size = 0

    for j in range(n):
        nodes = []
        for i in range(j, n):
            print(f"{employee_languages[j]} and {employee_languages[i]}")
            value = set(employee_languages[j]) & set(employee_languages[i])
            print(value)
            print(nodes)
            if value and value not in nodes and value != set(employee_languages[j]):
                size += 1
                nodes.append(value)

    print(n-1-size)


main()
