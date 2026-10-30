import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])

    r1 = list(map(int,data[1:1+n]))
    r2 = list(map(int,data[1+n:2*n+1]))

    def check(M):
        for row in (r1,r2):
            b = [x for x in row if x > M]
            if len(b) & 1  or b[::2] != b[1::2]:
                return False
        return True

    vals = [0]+ sorted(set(r1) | set(r2))

    lo,hi = 0,len(vals)-1
    while lo < hi:
        mid = (lo+hi) // 2
        if check(vals[mid]):
            hi = mid
        else:
            lo = mid + 1

    print(vals[lo])

main()